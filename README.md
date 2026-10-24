# AI Resume Analyzer

A modular Streamlit application that compares a resume with a target job description using explainable NLP techniques. It is designed as a portfolio project for demonstrating Python, document parsing, information extraction, machine learning, and product-minded UI design.

## Problem statement

Applicants often have the right experience but do not know which job requirements are missing or whether their resume communicates the evidence clearly. This tool provides a private, temporary first-pass comparison without pretending to predict hiring outcomes.

## Features

- PDF and DOCX extraction entirely in memory
- Role-aware job description input for Python, data, software, and AI/ML roles
- Configurable skill taxonomy with aliases such as `ML` and `Machine Learning`
- TF-IDF vectorization plus cosine similarity for a transparent estimated match score
- Matched, missing, and additional skill groups
- Resume section, action-verb, and quantified-achievement checks
- Plotly dashboard and TXT/PDF downloadable report
- Focused unit tests and graceful handling for empty, invalid, and unreadable inputs

## Technology stack

Python, Streamlit, scikit-learn, PyPDF2, python-docx, pandas, Plotly, ReportLab, and pytest.

## Architecture

```text
Upload -> resume_parser.py -> text
Job description ------------------+
                                   v
                         skill_extractor.py -> skill gap
                         matcher.py -> similarity score
                         analyzer.py -> quality checks
                                   v
                         app.py -> dashboard/report_generator.py
```

The score is calculated by normalizing both texts, creating TF-IDF vectors with `TfidfVectorizer`, and measuring their cosine similarity. It is lexical similarity, not a trained model, ATS certification, or hiring probability. The matcher can later be extended with embeddings while keeping its interface stable.

## Run locally

```powershell
cd ai-resume-analyzer
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m pytest -q
streamlit run app.py
```

Open the local URL printed by Streamlit, upload a resume, paste a job description, and select **Analyze resume**.

## Example input and output

Example resume text: `Built Python and pandas projects; analyzed SQL datasets.`

Example job text: `Python developer with SQL, pandas, Docker, and machine learning experience.`

The output identifies Python, SQL, and pandas as matched skills, Docker and Machine Learning as missing configured skills, and reports a bounded estimated similarity percentage.

## Screenshots

Add portfolio screenshots here after running the app, for example `docs/dashboard.png` and `docs/report.png`.

## Limitations and future improvements

- PDF extraction quality depends on whether the PDF contains selectable text.
- Skill detection is taxonomy-based and should be extended for a specific industry.
- Lexical similarity does not understand semantic equivalence beyond configured aliases.
- Future work could add optional embeddings, section-aware weighting, multilingual extraction, and user-controlled taxonomy editing.

## Streamlit Community Cloud

Push this repository to GitHub, choose **Deploy an app** in Streamlit Community Cloud, select the repository and branch, set the main file to `app.py`, and deploy. `requirements.txt` is included at the repository root.

## GitHub metadata

Suggested description: `Explainable AI resume and job description matcher built with Python, Streamlit, and TF-IDF.`

Suggested topics: `python`, `machine-learning`, `natural-language-processing`, `streamlit`, `scikit-learn`, `resume-analyzer`, `career-tools`.

## Upload to GitHub

```powershell
git init
git add .
git commit -m "Build AI resume analyzer"
git branch -M main
git remote add origin https://github.com/<username>/<repository>.git
git push -u origin main
```
