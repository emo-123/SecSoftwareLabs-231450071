# HW-3: Mini Security Event API

## Ödevin Amacı
Bu ödevde HTTP, REST API, JSON, status code, timeout ve hata yönetimi konularını uygulamak için küçük bir güvenlik olay servisi yazdım. Bir tarafta güvenlik olaylarını JSON olarak sunan bir **server**, diğer tarafta bu veriyi HTTP GET ile çekip işleyen bir **client** var. Client, high severity olayları `high_events.csv` dosyasına kaydediyor.

Sadece Python'ın hazır kütüphaneleri kullanıldı (`http.server`, `urllib`, `json`, `csv`), ek paket kurmak gerekmiyor.

## Klasör Yapısı
```
homework3/
├── server.py
├── client.py
├── high_events.csv
└── README.md
```

## Server Nasıl Çalıştırılır
Terminal 1'de:
```
python server.py
```
Server `http://127.0.0.1:8081` adresinde çalışır. Terminal açık kalmalıdır (Durdurmak için `Ctrl+C`).

## Client Nasıl Çalıştırılır
Server açıkken ikinci bir terminalde:
```
python client.py
```

## Kullanılan Endpointler
| Endpoint | Açıklama |
|---|---|
| `GET /api/events` | Tüm güvenlik olaylarını döndürür (10 olay) |
| `GET /api/events/high` | Sadece severity değeri `high` olanları döndürür |
| `GET /api/summary` | Toplam ve severity bazlı sayıları döndürür |
| Diğer her path | `404` ve `{"error": "Endpoint not found"}` |

Summary örneği:
```json
{"total": 10, "low": 4, "medium": 3, "high": 3}
```

## Örnek Çıktı
```
API bağlantısı başarılı.
Toplam olay: 10
Severity dağılımı:
LOW    : 4
MEDIUM : 3
HIGH   : 3

HIGH SEVERITY EVENTS
ID: 2
Type: bruteforce

ID: 5
Type: malware

ID: 8
Type: suspicious-login

CSV oluşturuldu: high_events.csv
```

`high_events.csv`:
```
id,severity,type
2,high,bruteforce
5,high,malware
8,high,suspicious-login
```

## Test Edilen Hata Senaryoları
1. **Normal çalışma:** Server açıkken client çalıştırıldı, olaylar ve severity dağılımı ekrana yazıldı, CSV oluştu.
2. **Yanlış endpoint:** `/api/abc` çağrıldığında server 404 ve JSON hata mesajı döndürdü. Client'ta URL bozulduğunda `HTTP hatası: 404` yazdı (`HTTPError`).
3. **Server kapalı:** Server kapatılıp client çalıştırıldığında program çökmedi, `API sunucusuna bağlanılamadı.` mesajını yazdı (`URLError`).

Ayrıca client'ta `timeout=3` kullanıldı. Content-Type kontrolü ve `json.loads` için de hata yakalama eklendi.
