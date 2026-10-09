"""TF-IDF cosine-similarity retrieval baseline."""
import json
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return [json.loads(line) for line in (ROOT / "data" / "processed" / name).read_text().splitlines() if line]


def run():
    resumes = load("resumes_processed.jsonl")
    results = []
    for job in load("job_descriptions_processed.jsonl"):
        matrix = TfidfVectorizer().fit_transform(
            [job["normalized_text"]] + [row["normalized_text"] for row in resumes])
        scores = cosine_similarity(matrix[0:1], matrix[1:]).ravel()
        indices = scores.argsort()[::-1][:5]
        results.append({"jd_id": job["jd_id"], "results": [
            {"candidate_id": resumes[i]["candidate_id"], "score": round(float(scores[i]), 6)}
            for i in indices]})
    (ROOT / "data" / "processed" / "retrieval_results.json").write_text(
        json.dumps(results, indent=2), encoding="utf-8")


if __name__ == "__main__":
    run()
    print("retrieved")
