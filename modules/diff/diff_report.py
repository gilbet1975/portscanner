from modules.diff.diff import diff_scans
from datetime import datetime
import os

def print_diff(file_a, file_b, save_to_file=False):
    new_open, closed, changed_banner = diff_scans(file_a, file_b)

    report_lines = []
    report_lines.append("=== DIFF ANALYZER ===")
    report_lines.append(f"Comparing:\n  A: {file_a}\n  B: {file_b}\n")

    report_lines.append("New open ports:")
    if new_open:
        for p in sorted(new_open):
            report_lines.append(f"  + {p}")
    else:
        report_lines.append("  None")

    report_lines.append("\nClosed ports:")
    if closed:
        for p in sorted(closed):
            report_lines.append(f"  - {p}")
    else:
        report_lines.append("  None")

    report_lines.append("\nChanged banners:")
    if changed_banner:
        for p in sorted(changed_banner):
            report_lines.append(f"  * {p}")
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


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python diff_report.py <file_a> <file_b> [--save]")
    else:
        save_flag = "--save" in sys.argv
        print_diff(sys.argv[1], sys.argv[2], save_to_file=save_flag)