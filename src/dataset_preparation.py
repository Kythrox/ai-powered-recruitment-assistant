"""Prepare and validate Month-1 resume and JD CSV datasets."""
from pathlib import Path
import pandas as pd
from .resume_processing import process_resumes
from .text_cleaning import clean_text


def prepare(resumes_path: str | Path, jds_path: str | Path, output_dir: str | Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    output_dir = Path(output_dir)
    resumes = process_resumes(resumes_path, output_dir / "resumes_processed.csv")
    jds = pd.read_csv(jds_path)
    jds["cleaned_text"] = jds["job_description"].fillna("").map(clean_text)
    jds.to_csv(output_dir / "job_descriptions_processed.csv", index=False)
    return resumes, jds
