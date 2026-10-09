"""TF-IDF similarity demonstration; not a hiring decision or production metric."""
from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def rank(resumes: pd.DataFrame, job_description: str, top_k: int = 5) -> pd.DataFrame:
    texts = [job_description] + resumes["cleaned_text"].fillna("").tolist()
    matrix = TfidfVectorizer().fit_transform(texts)
    scores = cosine_similarity(matrix[0:1], matrix[1:]).ravel()
    result = resumes[["candidate_id"]].copy()
    result["similarity"] = scores
    return result.sort_values("similarity", ascending=False).head(top_k).reset_index(drop=True)


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    resumes = pd.read_csv(root / "data/processed/resumes_processed.csv")
    jds = pd.read_csv(root / "data/processed/job_descriptions_processed.csv")
    print(rank(resumes, jds.loc[0, "cleaned_text"]).to_string(index=False))
