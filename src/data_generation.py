"""Generate deterministic synthetic resumes and job descriptions."""
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ["python", "sql", "statistics", "machine learning", "nlp", "pandas",
          "scikit-learn", "docker", "aws", "api design", "testing", "git"]
ROLES = ["Data Analyst", "ML Engineer", "NLP Engineer", "Backend Engineer",
         "Analytics Engineer"]


def generate(seed=7):
    rng = random.Random(seed)
    resumes, jobs = [], []
    for i in range(1, 51):
        skills = sorted(rng.sample(SKILLS, 4 + i % 4))
        role = ROLES[(i - 1) % len(ROLES)]
        resumes.append({"candidate_id": f"Candidate_{i:03d}",
                        "resume_text": f"Synthetic {role} profile with experience in {', '.join(skills)}.",
                        "skills": skills})
    for i in range(1, 21):
        skills = sorted(rng.sample(SKILLS, 3 + i % 3))
        title = ROLES[(i - 1) % len(ROLES)]
        jobs.append({"jd_id": f"JD_{i:03d}", "title": title,
                     "description": f"Synthetic {title} role requiring {', '.join(skills)}.",
                     "required_skills": skills})
    return resumes, jobs


def write(seed=7):
    resumes, jobs = generate(seed)
    directory = ROOT / "data" / "raw"
    directory.mkdir(parents=True, exist_ok=True)
    for path, rows in [(directory / "resumes.jsonl", resumes),
                       (directory / "job_descriptions.jsonl", jobs)]:
        path.write_text("".join(json.dumps(row) + "\n" for row in rows),
                        encoding="utf-8")


if __name__ == "__main__":
    write()
    print("generated")
