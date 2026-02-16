# Processor Documentation

The processor module handles data transformation and validation.

## Usage

```python
from processor import DataProcessor

processor = DataProcessor(source="api")
results = processor.run()
```

## API Reference

### `DataProcessor.run()`

Executes the processing pipeline and returns results.

**Returns:** `dict` with keys `status`, `count`, and `errors`.
