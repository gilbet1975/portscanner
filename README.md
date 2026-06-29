<p align="center">
  <img src="logo.svg" width="700" alt="Portscanner Toolkit Logo">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/github/v/release/gilbet1975/portscanner?style=for-the-badge">
  <img src="https://img.shields.io/github/last-commit/gilbet1975/portscanner?style=for-the-badge">
  <img src="https://img.shields.io/github/languages/top/gilbet1975/portscanner?style=for-the-badge">
</p>

# 🔍 Portscanner Toolkit  
### A fast, modular, extensible network security toolkit  
by **@gilbet1975**

---

## 🚀 Overview

The **Portscanner Toolkit** is a high‑performance, multi‑threaded network scanner with a powerful diff analyzer and multiple export formats (TXT, JSON, HTML).  
It is designed for:

- Security researchers  
- Network administrators  
- Home lab enthusiasts  
- Students learning networking & cybersecurity  

The toolkit is fully modular, easy to extend, and built with clean architecture principles.

---

# ✨ Feature Highlights (v1.1.0)

## 🔥 Multi‑Threaded Port Scanner
- Ultra‑fast TCP scanning  
- Configurable port ranges  
- Banner grabbing (planned)  
- Automatic timestamped log files  
- JSON output for structured analysis  

## 🔄 Diff Analyzer (TXT, JSON, HTML)
Compare two scans and detect:

- ➕ Newly opened ports  
- ➖ Closed ports  
- ✳️ Changed banners (planned)  

Export formats:

| Format | Description |
|--------|-------------|
| **TXT** | Human‑readable diff |
| **JSON** | Machine‑readable diff for automation |
| **HTML** | Beautiful, styled diff report |

## 🧰 Unified CLI
| Command | Description |
|--------|-------------|
| `--scan` | Run a port scan |
| `--diff` | Compare two scan logs |
| `--save` | Save diff output |
| `--html` | Export diff as HTML |

---

# 🖼️ Screenshots (Placeholders)

### 🔍 Port Scan Output  
![Port Scan Placeholder](https://via.placeholder.com/900x300?text=Port+Scan+Output)

### 🔄 Diff Analyzer Output  
![Diff Analyzer Placeholder](https://via.placeholder.com/900x300?text=Diff+Analyzer+Output)

### 🧾 HTML Report  
![HTML Report Placeholder](https://via.placeholder.com/900x300?text=HTML+Diff+Report)

---

# 🧬 Architecture Overview
```
portscanner/
│
├── main.py                 # CLI entry point
├── logo.svg                # Project logo
├── README.md               # Documentation
│
├── modules/
│   ├── scanner/
│   │   ├── threader.py     # Worker threads
│   │   ├── writer.py       # Log writer
│   │   ├── utils.py        # Banner grabbing (planned)
│   │   └── scanner.py      # Core scanning logic
│   │
│   ├── diff/
│   │   ├── diff.py         # Diff logic (TXT)
│   │   └── diff_report.py  # JSON + HTML diff export
│   │
│   ├── output/
│   │   ├── json_writer.py  # JSON output generator
│   │   └── metadata.py     # Scan metadata system
│
└── logs/                   # Auto-generated logs & reports
```

---

# 🧪 Usage

## 🔍 Basic Port Scan
```bash
python main.py --scan --host 192.168.1.10 --threads 50
```

## 🧵 Multi‑Threaded Scan
```bash
python main.py --scan --host 10.0.0.5 --threads 200
```

## 🏷️ Custom Output Filename
```bash
python main.py --scan --output myscan.txt
```

## 📦 JSON Output
Every scan automatically generates:
- a human‑readable .txt log
- a structured .json file

### Example JSON
```json
{
    "host": "127.0.0.1",
    "timestamp": "2026-06-27T20:35:00.123456",
    "duration_ms": 123,
    "threads": 10,
    "open_ports": [80, 443],
    "metadata": {
        "scanner_version": "1.0.0",
        "log_file": "logs/scan_20260627-203500.txt"
    }
}
```

## 🔄 Diff Analyzer
Compare two scans
```bash
python main.py --diff logs/scan_old.txt logs/scan_new.txt
```

### Save diff report
```bash
python main.py --diff scan1.txt scan2.txt --save
```

### Export as HTML
```bash
python main.py --diff scan1.txt scan2.txt --html
```

## 📊 Feature Matrix
| Feature | Status | Version |
|---------|--------|---------|
| Multi-threaded TCP scan | ✅ | 1.0.0 |
| JSON scan output | ✅ | 1.0.0 |
| TXT diff analyzer |  ✅ | 1.1.0 |
| JSON diff analyzer | ✅ | 1.1.0 |
| HTML diff export | ✅ | 1.1.0 |
| Banner grabbing | 🔄 | In progress | 1.2.0 |
| UDP scan | 🔄 | Planned | 1.3.0 |
| GUI | 🔄 | Planned | 2.0.0 |

## 🛣️ Roadmap
### Phase 1 — Core Scanner (Completed)
- [x] Multi-threaded scanning
- [x] Logging system
- [x] JSON output

### Phase 2 — Output & Analysis (Completed in v1.1.0)
- [x] JSON diff analyzer
- [x] HTML diff export
- [x] Improved diff formatting

### Phase 3 — Advanced Scanning
- [ ] UDP scan mode
- [ ] Banner grabbing
- [ ] Auto-diff mode

### Phase 4 — User Interface
- [ ] GUI (Tkinter / PyQt)
- [ ] Live scan progress
- [ ] Visual diff comparison

### Phase 5 — Reporting & Export
- [ ] Markdown export
- [ ] PDF export
- [ ] Custom templates

### Phase 6 — Extensibility
- [ ] Plugin system
- [ ] Plugin registry
- [ ] Example plugins

## 🧾 Release History
### v1.1.0 — Diff Analyzer Upgrade
- Added HTML diff export
- Added JSON diff export
- Improved TXT diff formatting
- Stabilized f‑string handling
- Modularized diff output system

### v1.0.0 — Initial Release
- Multi-threaded scanner
- JSON output
- Logging system
- CLI interface

## 🤝 Contributing
Contributions are welcome!
Feel free to open:
- Issues
- Feature requests
- Pull requests

## 📜 License
This project is licensed under the MIT License.

## ⭐ Author
Gilles Bettendorf  
GitHub: @gilbet1975
