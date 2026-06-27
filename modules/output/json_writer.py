import json
from pathlib import Path
from datetime import datetime

class JSONWriter:
    def __init__(self, output_dir="logs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def write(self, data: dict, prefix: str = "scan"):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{prefix}_{timestamp}.json"
        filepath = self.output_dir / filename

        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)

        return filepath