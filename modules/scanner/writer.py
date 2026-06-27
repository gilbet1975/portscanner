from datetime import datetime
from modules.scanner.utils import grab_banner

def write_result(path, text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}]: {text}\n")