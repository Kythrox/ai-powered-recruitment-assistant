"""Small, dependency-light text extraction helpers for Month 1."""
from pathlib import Path


def read_text(path: str | Path) -> str:
    """Read UTF-8 text from a relative or absolute path."""
    return Path(path).read_text(encoding="utf-8")


def extract_resume_text(record: dict) -> str:
    """Return the text field from a resume-like record."""
    return str(record.get("resume_text", "")).strip()
