# Homework-2 – JSON, Regex, CSV ve Veri Doğrulama

## Amaç
Olay kayıtlarından başarısız girişleri bulup CSV'ye kaydetmek.

## Veri Seti
`datasets/events.jsonl`

## Çalıştırma
cd homework2  
python week03_regex_json.py

## Programın Amacı
- events.jsonl dosyasını satır satır okur ve her satırı JSON olarak çevirir.
- Hatalı JSON satırlarını atlar, program durmaz.
- status değeri FAILED olan ve IP adresi geçerli olan kayıtları seçer.
- Seçilen kayıtları failed_events.csv dosyasına yazar.

## Örnek Çıktı
Total events: 35  
Failed events: 16  
CSV olusturuldu: failed_events.csv
