import threading
from queue import Queue
from modules.scanner.scanner import scan_port
from modules.scanner.utils import grab_banner
from modules.scanner.writer import write_result

def worker(host, output_file, queue):
    while not queue.empty():
        port = queue.get()
        if scan_port(host, port):
            banner = grab_banner(host, port)
            if banner:
                write_result(output_file, f"OPEN {port} — {banner}")
            else:
                write_result(output_file, f"OPEN {port}")
        queue.task_done()