"""Evaluate synthetic skill-overlap relevance; not a hiring metric."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def evaluate(k=5):
    resumes = [json.loads(x) for x in (ROOT / "data/raw/resumes.jsonl").read_text().splitlines()]
    jobs = [json.loads(x) for x in (ROOT / "data/raw/job_descriptions.jsonl").read_text().splitlines()]
    rankings = json.loads((ROOT / "data/processed/retrieval_results.json").read_text())
    skills = {row["candidate_id"]: set(row["skills"]) for row in resumes}
    values = []
    for job, ranking in zip(jobs, rankings):
        relevant = {candidate for candidate, values in skills.items()
                    if len(set(job["required_skills"]) & values) >= 2}
        hits = sum(row["candidate_id"] in relevant for row in ranking["results"][:k])
        values.append(hits / max(1, min(k, len(relevant))))
    summary = {"cutoff": k, "queries": len(values),
               "mean_recall_at_k": sum(values) / len(values)}
    (ROOT / "data/processed/evaluation.json").write_text(json.dumps(summary, indent=2))
    return summary


if __name__ == "__main__":
    print(evaluate())
