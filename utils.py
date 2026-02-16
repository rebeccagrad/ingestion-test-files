"""Utility functions for common operations."""

import hashlib
import re
from datetime import datetime


def sanitize_input(text: str) -> str:
    """Remove potentially unsafe characters from input."""
    return re.sub(r"[<>&\"']", "", text.strip())


def generate_hash(content: str) -> str:
    """Generate a SHA-256 hash of the given content."""
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def format_timestamp(dt: datetime = None) -> str:
    """Format a datetime as ISO 8601 string."""
    if dt is None:
        dt = datetime.utcnow()
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def chunk_list(items: list, size: int) -> list:
    """Split a list into chunks of the given size."""
    return [items[i:i + size] for i in range(0, len(items), size)]
