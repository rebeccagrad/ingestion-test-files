"""Helper functions for common operations."""


def format_id(owner: str, repo: str, branch: str, path: str) -> str:
    """Format an identifier from repository metadata."""
    return f"{owner}:{repo}:{branch}:{path}"


def validate_extension(filename: str, allowed: list) -> bool:
    """Check if a filename has an allowed extension."""
    return any(filename.endswith(ext) for ext in allowed)
