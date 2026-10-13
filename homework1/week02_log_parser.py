from collections import Counter
from pathlib import Path

LOG = Path(__file__).parents[1] / "datasets" / "auth.log"

def parse_line(line: str) -> dict:
    timestamp, *fields = line.split()
    record = {"timestamp": timestamp}
    for field in fields:
        key, value = field.split("=", 1)
        record[key] = value
    return record

def main():
    records = []
    with LOG.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(parse_line(line))

    statuses = Counter(r["status"] for r in records)
    status_counts = {"SUCCESS": statuses["SUCCESS"], "FAILED": statuses["FAILED"]}

    failed_ips = Counter(r["src_ip"] for r in records if r["status"] == "FAILED")
    top_failed_ip = failed_ips.most_common(1)[0] if failed_ips else None

    print("Status counts:", status_counts)
    print("Top failed IP:", top_failed_ip)

if __name__ == "__main__":
    main()
