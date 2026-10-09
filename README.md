# Month-1 foundation

This project contains the exact Month-1 preparation structure for a synthetic recruitment-assistant prototype. It uses only synthetic identifiers (`Candidate_001`–`Candidate_050`, `JD_001`–`JD_020`) and supplied facts. No real people, company history, hiring outcomes, or fabricated metrics are included.

## Structure
- `data/sample_data/`: 50 resume CSV rows and 20 job-description CSV rows.
- `data/processed/`: cleaned CSV outputs.
- `src/`: `text_extraction.py`, `text_cleaning.py`, `resume_processing.py`, `dataset_preparation.py`, and `similarity_demo.py`.
- `notebooks/`: four notebooks in the required order.
- `docs/`: project overview, data dictionary, and setup notes.

## Run
From the repository root:

```powershell
pip install -r requirements.txt
python -c "from src.dataset_preparation import prepare; prepare('data/sample_data/resumes.csv','data/sample_data/job_descriptions.csv','data/processed')"
python -m src.similarity_demo
```

Notebook paths are relative to the repository root. Similarity is an educational TF-IDF demonstration, not a hiring recommendation or validated performance measure.
