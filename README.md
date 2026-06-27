# 🔍 Portscanner Toolkit  
### A fast, modular, and extensible network security toolkit  
by **@gilbet1975**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/github/last-commit/gilbet1975/portscanner?style=for-the-badge">
  <img src="https://img.shields.io/github/languages/top/gilbet1975/portscanner?style=for-the-badge">
</p>

---

## 🚀 Overview

The **Portscanner Toolkit** is a high‑performance, multi‑threaded network scanner with a built‑in diff analyzer.  
It is designed for:

- Security researchers  
- Network administrators  
- Home lab enthusiasts  
- Anyone who wants fast, clear insights into open ports and service changes  

The toolkit is fully modular and easy to extend.

---

## ✨ Features

### 🔥 Multi‑Threaded Port Scanner
- Extremely fast TCP scanning  
- Configurable port ranges  
- Banner grabbing (service identification)  
- Automatic timestamped log files  

### 🔥 Diff Analyzer
Compare two scan results and detect:

- ➕ Newly opened ports  
- ➖ Ports that have closed  
- ✳️ Changed banners (e.g., version updates)  

Optional: Save the diff report automatically.

### 🔥 Unified CLI

| Command | Description |
|--------|-------------|
| `--scan` | Run a port scan |
| `--diff` | Compare two scan logs |
| `--save` | Save diff output |

---

## 🖼️ Screenshots (Placeholders)

> Replace these with real screenshots later.

### Port Scan Output  
![Scan Screenshot](docs/screenshots/scan_example.png)

### Diff Analyzer Output  
![Diff Screenshot](docs/screenshots/diff_example.png)

---

## 📦 Installation

```bash
git clone https://github.com/gilbet1975/portscanner.git
cd portscanner
```
---

## 🧪 Usage

### Run a Port Scan
```bash
python main.py --scan --host 192.168.1.10 --start 1 --end 2000 --threads 300
```

### Run the Diff Analyzer
```bash
python main.py --diff logs/scan_old.txt logs/scan_new.txt
```

### Save the Diff Report
```bash
python main.py --diff scan1.txt scan2.txt --save
```

## 📁 Project Structure
```markdown
modules/
  scanner/
    scanner.py        # Port scanning logic
    threader.py       # Worker threads
    utils.py          # Banner grabbing
    writer.py         # Log writer
  diff/
    diff.py           # Diff logic
    diff_report.py    # Report formatting
logs/                 # Auto-generated logs
main.py               # CLI entry point
```

## 🛣️ Roadmap
- [ ] JSON output for scanner
- [ ] JSON output for diff analyzer
- [ ] GUI (Tkinter or PyQt)
- [ ] UDP scan mode
- [ ] Auto‑diff: “Compare last scan with previous one”
- [ ] Export as HTML report
- [ ] Plugin system for custom scanners

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
