"""Load and clean the synthetic resume CSV."""
from pathlib import Path
import pandas as pd
from .text_cleaning import clean_text


def process_resumes(input_path: str | Path, output_path: str | Path) -> pd.DataFrame:
    frame = pd.read_csv(input_path)
    frame["cleaned_text"] = frame["resume_text"].fillna("").map(clean_text)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output_path, index=False)
    return frame
