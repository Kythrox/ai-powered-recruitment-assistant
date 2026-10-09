"""Deterministic text normalization used by the preparation notebooks."""
import re


def clean_text(text: str) -> str:
    """Lowercase, normalize whitespace, and retain common skill punctuation."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#.\- ]", " ", text)
    return re.sub(r"\s+", " ", text).strip()
