"""Normalize raw text into processed JSONL records."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def normalize(text):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9+#.\- ]", " ", text.lower())).strip()


def process():
    raw, out = ROOT / "data" / "raw", ROOT / "data" / "processed"
    out.mkdir(parents=True, exist_ok=True)
    for source, target, field in [("resumes.jsonl", "resumes_processed.jsonl", "resume_text"),
                                  ("job_descriptions.jsonl", "job_descriptions_processed.jsonl", "description")]:
        rows = [json.loads(line) for line in (raw / source).read_text(encoding="utf-8").splitlines() if line]
        (out / target).write_text("".join(json.dumps({**row, "normalized_text": normalize(row[field])}) + "\n"
                                          for row in rows), encoding="utf-8")


if __name__ == "__main__":
    process()
    print("processed")
