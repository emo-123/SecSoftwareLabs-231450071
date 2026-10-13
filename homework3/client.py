from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from pathlib import Path
import json
import csv

URL = "http://127.0.0.1:8081/api/events"
OUTPUT = Path(__file__).parent / "high_events.csv"


def get_events():
    with urlopen(URL, timeout=3) as response:
        content_type = response.headers.get_content_type()
        if content_type != "application/json":
            raise ValueError("JSON response bekleniyordu")
        body = response.read().decode("utf-8")
        return json.loads(body)


def save_csv(high_events):
    with OUTPUT.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "severity", "type"])
        for event in high_events:
            writer.writerow([event["id"], event["severity"], event["type"]])


def main():
    try:
        events = get_events()
    except HTTPError as error:
        print("HTTP hatası:", error.code)
        return
    except URLError as error:
        print("API sunucusuna bağlanılamadı.")
        print("Sebep:", error.reason)
        return
    except TimeoutError:
        print("Sunucu zamanında cevap vermedi (timeout).")
        return
    except (ValueError, json.JSONDecodeError) as error:
        print("Gelen veri geçersiz:", error)
        return

    print("API bağlantısı başarılı.")
    print("Toplam olay:", len(events))

    counts = {"low": 0, "medium": 0, "high": 0}
    high_events = []

    for event in events:
        severity = event.get("severity")
        if severity in counts:
            counts[severity] += 1
        if severity == "high":
            high_events.append(event)

    print("Severity dağılımı:")
    print("LOW    :", counts["low"])
    print("MEDIUM :", counts["medium"])
    print("HIGH   :", counts["high"])

    print()
    print("HIGH SEVERITY EVENTS")
    for event in high_events:
        print("ID:", event.get("id"))
        print("Type:", event.get("type"))
        print()

    save_csv(high_events)
    print("CSV oluşturuldu:", OUTPUT.name)


if __name__ == "__main__":
    main()
