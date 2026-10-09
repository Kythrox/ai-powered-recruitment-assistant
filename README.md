# AI-Powered Recruitment Assistant

## Month 1 foundation
This repository contains a synthetic-only foundation for resume and job-description preparation. It uses labels `Candidate_001` through `Candidate_050` and `JD_001` through `JD_020`. Contact fields are clearly synthetic test values. No real candidate, employer, hiring, historical, or performance data is included.

## Contents
- `data/sample_data/`: canonical 50-row resume and 20-row job-description CSV fixtures.
- `data/processed/`: cleaned CSV outputs with the same records.
- `data/resumes/` and `data/job_descriptions/`: representative raw TXT samples.
- `sample_data/sample_resumes/` and `sample_data/sample_job_descriptions/`: small teaching samples.
- `src/`: extraction, cleaning, processing, dataset preparation, and TF-IDF demonstration modules.
- `notebooks/`: regex preparation, NLP preparation, TF-IDF similarity, and dataset exploration.
- `docs/` and `reports/`: project documentation and Month-1 report content.

## Run
```powershell
pip install -r requirements.txt
python -c "from src.dataset_preparation import prepare; prepare('data/sample_data/resumes.csv','data/sample_data/job_descriptions.csv','data/processed')"
python -m src.similarity_demo
```
Run notebooks from the repository root, in numbered order. All paths are relative. Similarity is an educational baseline, not a hiring decision or validated metric.

## Data safety
`config/company_facts.json` is intentionally empty because no company facts were supplied. Do not add claims without an authorized source. Synthetic labels are not identities or protected attributes.
