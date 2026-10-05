# SecSoftwareLabs-231450071

## Klasör Yapısı
```
SecSoftwareLabs-231450071
├── README.md
├── datasets/
└── Homework-1/
    ├── week01_setup_check.py
    └── week02_log_parser.py
```

---

# Homework-1

## Amaç
- `week01_setup_check.py`: Python geliştirme ortamının hazır olduğunu kontrol eder.
- `week02_log_parser.py`: auth.log dosyasını okur, başarılı ve başarısız girişleri sayar, en çok başarısız giriş yapan IP'yi bulur.

## Gereksinimler
Python 3.11+

## Çalıştırma
```
cd Homework-1
python week01_setup_check.py
python week02_log_parser.py
```

## Örnek Çıktı
`week01_setup_check.py`:
```
Python: 3.14.3 ...
Kurulum hazır.
```

`week02_log_parser.py`:
```
Status counts: {'SUCCESS': 39, 'FAILED': 21}
Top failed IP: ('10.10.1.25', 8)
```
