from modules.scanner.threader import worker
from modules.scanner.writer import write_result
from modules.diff.diff_report import print_diff

from datetime import datetime
from queue import Queue
import threading
import argparse
import os


def run_scan(host, start_port, end_port, thread_count, output_file):
    # Write scan header
    write_result(output_file, f"--- Scan started on {host} ---")

    # Queue for Ports
    queue = Queue()

    # Load ports into queue
    for port in range(start_port, end_port + 1):
        queue.put(port)

    # Start threads
    for _ in range(thread_count):
        t = threading.Thread(target=worker, args=(host, output_file, queue))
        t.daemon = True
        t.start()

    # Wait until execution ends
    queue.join()

    # Write scan footer
    end_str = datetime.now().strftime("%Y%m%d-%H%M%S")
    write_result(output_file, f"--- Scan finished at {end_str} ---")


def main():
    parser = argparse.ArgumentParser(description="Portscanner Toolkit")

    # Scanner mode
    parser.add_argument("--scan", action="store_true",
                        help="Run a port scan")

    parser.add_argument("--host", type=str, default="127.0.0.1",
                        help="Target host to scan")

    parser.add_argument("--start", type=int, default=1,
                        help="Start port")

    parser.add_argument("--end", type=int, default=65535,
                        help="End port")

    parser.add_argument("--threads", type=int, default=100,
                        help="Number of threads")

    parser.add_argument("--output", type=str, default=None,
                        help="Optional custom output filename")

    # Diff mode
    parser.add_argument("--diff", nargs=2,
                        help="Compare two scan log files")

    parser.add_argument("--save", action="store_true",
                        help="Save diff report to file")

    args = parser.parse_args()

    # -------------------------
    # Diff Analyzer Mode
    # -------------------------
    if args.diff:
        file_a, file_b = args.diff
        print_diff(file_a, file_b, save_to_file=args.save)
        return

    # -------------------------
    # Scanner Mode
    # -------------------------
    if args.scan:
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)

        if args.output:
            output_file = os.path.join(log_dir, args.output)
        else:
            date_str = datetime.now().strftime("%Y%m%d-%H%M%S")
            output_file = os.path.join(log_dir, f"scan_{date_str}.txt")

        run_scan(
            host=args.host,
            start_port=args.start,
            end_port=args.end,
            thread_count=args.threads,
            output_file=output_file
        )
        return

    parser.print_help()


if __name__ == "__main__":
    main()