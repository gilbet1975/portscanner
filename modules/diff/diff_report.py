from modules.diff.diff import diff_scans
from datetime import datetime
import json
import os

# ANSI Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def print_diff(file_a, file_b, save_to_file=False):
    new_open, closed, changed_banner = diff_scans(file_a, file_b)

    report_lines = []
    report_lines.append(f"{BLUE}=== DIFF ANALYZER ==={RESET}")
    report_lines.append(f"Comparing:\n  A: {file_a}\n  B: {file_b}\n")

    report_lines.append("New open ports:")
    if new_open:
        for p in sorted(new_open):
            report_lines.append(f"  {GREEN}+ {p}{RESET}")
    else:
        report_lines.append("  None")

    report_lines.append("\nClosed ports:")
    if closed:
        for p in sorted(closed):
            report_lines.append(f"  {RED}- {p}{RESET}")
    else:
        report_lines.append("  None")

    report_lines.append("\nChanged banners:")
    if changed_banner:
        for p in sorted(changed_banner):
            report_lines.append(f"  {YELLOW}* {p}{RESET}")
    else:
        report_lines.append("  None")

    report_lines.append("\n=== END OF REPORT ===\n")

    # CLI output
    print("\n".join(report_lines))

    # Save report
    if save_to_file:
        os.makedirs("logs", exist_ok=True)
        date_str = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_path = os.path.join("logs", f"diff_report_{date_str}.txt")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(report_lines))
        print(f"\nReport saved to: {output_path}")

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def diff_json(file_a, file_b):
    a = load_json(file_a)
    b = load_json(file_b)

    ports_a = set(a.get("open_ports", []))
    ports_b = set(b.get("open_ports", []))

    added = sorted(list(ports_b - ports_a))
    removed = sorted(list(ports_a - ports_b))

    return {
        "file_a": file_a,
        "file_b": file_b,
        "added_ports": added,
        "removed_ports": removed,
        "metadata_diff": {
            "duration_ms": b["duration_ms"] - a["duration_ms"],
            "threads": b["threads"] - a["threads"]
        }
    }

def save_json_diff(result):
    os.makedirs("logs", exist_ok=True)
    date_str = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_path = os.path.join("logs", f"diff_report_{date_str}.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

    print(f"\nJSON diff saved to: {output_path}")

def print_json_diff(result):
    print(f"\n{BLUE}=== JSON DIFF REPORT ==={RESET}")
    print(f"Comparing:\n  {result['file_a']}\n  {result['file_b']}")

    print("\nNew open ports:")
    if result["added_ports"]:
        for p in result["added_ports"]:
            print(f"  {GREEN}+ {p}{RESET}")
    else:
        print("  None")

    print("\nClosed ports:")
    if result["removed_ports"]:
        for p in result["removed_ports"]:
            print(f"  {RED}- {p}{RESET}")
    else:
        print("  None")

    print("\nMetadata changes:")
    for key, value in result["metadata_diff"].items():
        print(f"  {key}: {value}")


def export_html_diff(result, output_path):

    added_html = "".join(f'<p class="added">+ {p}</p>' for p in result["added_ports"])
    removed_html = "".join(f'<p class="removed">- {p}</p>' for p in result["removed_ports"])
    meta_html = "".join(f'<p class="meta">{k}: {v}</p>' for k, v in result["metadata_diff"].items())

    html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Diff Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; background: #f5f5f5; padding: 20px; }}
            h1 {{ color: #2c3e50; }}
            .added {{ color: green; }}
            .removed {{ color: red; }}
            .meta {{ color: #555; }}
            .box {{ background: white; padding: 15px; border-radius: 8px; margin-bottom: 20px; }}
        </style>
    </head>
    <body>
        <h1>Diff Report</h1>

        <div class="box">
            <h2>Compared Files</h2>
            <p>A: {result['file_a']}</p>
            <p>B: {result['file_b']}</p>
        </div>

        <div class="box">
            <h2>New Open Ports</h2>
            {added_html}
        </div>

        <div class="box">
            <h2>Closed Ports</h2>
            {removed_html}
        </div>

        <div class="box">
            <h2>Metadata Changes</h2>
            {meta_html}
        </div>
    </body>
    </html>
    """

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"HTML diff exported to: {output_path}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python diff_report.py <file_a> <file_b> [--save]")
        sys.exit(1)

    file_a = sys.argv[1]
    file_b = sys.argv[2]
    save_flag = "--save" in sys.argv

    # JSON-file recognized
    if file_a.endswith(".json") and file_b.endswith(".json"):
        result = diff_json(file_a, file_b)
        print_json_diff(result)

        if save_flag:
            save_json_diff(result)

    else:
        # Standard TXT-Diff
        print_diff(file_a, file_b, save_to_file=save_f)