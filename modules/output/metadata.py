from datetime import datetime

class ScanMetadata:
    def __init__(self, host: str, threads: int, log_file: str, version="1.0.0"):
        self.host = host
        self.threads = threads
        self.log_file = log_file
        self.version = version

        self.start_time = datetime.now()
        self.end_time = None

    def finish(self):
        """Mark scan as finished and compute duration."""
        self.end_time = datetime.now()

    @property
    def timestamp(self):
        return self.start_time.isoformat()

    @property
    def duration_ms(self):
        if not self.end_time:
            return None
        delta = self.end_time - self.start_time
        return int(delta.total_seconds() * 1000)

    def to_dict(self):
        """Return metadata as dictionary for JSON export."""
        return {
            "host": self.host,
            "timestamp": self.timestamp,
            "duration_ms": self.duration_ms,
            "threads": self.threads,
            "metadata": {
                "scanner_version": self.version,
                "log_file": self.log_file
            }
        }