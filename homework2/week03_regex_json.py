import json
import csv
import re
from pathlib import Path

# veri dosyasi bir ust klasordeki datasets icinde
veri_dosyasi = Path(__file__).parents[1] / "datasets" / "events.jsonl"
cikti_dosyasi = Path(__file__).parent / "failed_events.csv"

# her oktet 0-255 arasinda olmali
ip_regex = re.compile(r"^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$")

kolonlar = ["timestamp", "event_id", "src_ip", "user", "status"]


def ip_gecerli_mi(ip):
    return ip_regex.match(str(ip)) is not None


def main():
    olaylar = []
    with open(veri_dosyasi, "r", encoding="utf-8") as f:
        for satir in f:
            satir = satir.strip()
            if satir == "":
                continue
            try:
                olaylar.append(json.loads(satir))
            except json.JSONDecodeError:
                print("Hatali JSON satiri atlandi:", satir)

    basarisizlar = []
    for olay in olaylar:
        if olay.get("status") == "FAILED" and ip_gecerli_mi(olay.get("src_ip", "")):
            basarisizlar.append(olay)

    # extrasaction ignore -> fazladan alan varsa hata vermesin
    with open(cikti_dosyasi, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=kolonlar, extrasaction="ignore")
        writer.writeheader()
        for olay in basarisizlar:
            writer.writerow(olay)

    print("Total events:", len(olaylar))
    print("Failed events:", len(basarisizlar))
    print("CSV olusturuldu:", cikti_dosyasi.name)


if __name__ == "__main__":
    main()
