def load_scan_file(path):
    ports = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # Only rows with the status Open
            if line.startswith("OPEN"):
                parts = line.split(" ", 2)

                port = int(parts[1])
                banner = parts[2] if len(parts) > 2 else ""

                ports[port] = banner

    return ports


def diff_scans(file_a, file_b):
    scan_a = load_scan_file(file_a)
    scan_b = load_scan_file(file_b)

    ports_a = set(scan_a.keys())
    ports_b = set(scan_b.keys())

    # New open ports
    new_open = ports_b - ports_a

    # Recently closed ports
    closed = ports_a - ports_b

    # Ports with changes on the banner
    changed_banner = []
    for port in ports_a & ports_b:
        if scan_a[port] != scan_b[port]:
            changed_banner.append(port)

    return new_open, closed, changed_banner
