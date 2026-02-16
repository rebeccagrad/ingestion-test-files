"""Sample Python module for data processing."""

class DataProcessor:
    def __init__(self, source: str):
        self.source = source
        self.records = []

    def process(self, data: list[dict]) -> int:
        for record in data:
            if record.get("active"):
                self.records.append(record)
        return len(self.records)

if __name__ == "__main__":
    processor = DataProcessor("github")
    count = processor.process([{"name": "test", "active": True}])
    print(f"Processed {count} records")
