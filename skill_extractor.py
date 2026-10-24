"""Maintainable skill taxonomy and case-insensitive extraction."""
from __future__ import annotations

import re
from typing import Iterable

SKILL_ALIASES: dict[str, tuple[str, ...]] = {
    "Python": ("python",), "Java": ("java",), "C++": ("c++", "cpp"),
    "SQL": ("sql",), "JavaScript": ("javascript", "js"), "TypeScript": ("typescript", "ts"),
    "HTML/CSS": ("html", "css"), "React": ("react",), "Git": ("git", "github"),
    "Docker": ("docker",), "AWS": ("aws", "amazon web services"), "Azure": ("azure",),
    "Pandas": ("pandas",), "NumPy": ("numpy",), "scikit-learn": ("scikit-learn", "sklearn"),
    "TensorFlow": ("tensorflow",), "PyTorch": ("pytorch",), "Machine Learning": ("machine learning", "ml"),
    "Deep Learning": ("deep learning",), "NLP": ("natural language processing", "nlp"),
    "Computer Vision": ("computer vision",), "Statistics": ("statistics", "statistical analysis"),
    "Data Analysis": ("data analysis", "data analytics"), "Data Visualization": ("data visualization", "data viz"),
    "Tableau": ("tableau",), "Power BI": ("power bi",), "Excel": ("excel",),
    "Streamlit": ("streamlit",), "REST APIs": ("rest api", "restful api", "rest apis"),
    "Problem Solving": ("problem solving",), "Communication": ("communication",),
}


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def extract_skills(text: str, taxonomy: dict[str, tuple[str, ...]] | None = None) -> set[str]:
    source = normalize_text(text)
    found: set[str] = set()
    for canonical, aliases in (taxonomy or SKILL_ALIASES).items():
        if any(re.search(r"(?<![\w+#])" + re.escape(alias.lower()) + r"(?![\w+#])", source) for alias in aliases):
            found.add(canonical)
    return found


def skill_gap(resume_text: str, job_text: str) -> dict[str, set[str]]:
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)
    return {
        "resume": resume_skills,
        "required": job_skills,
        "matched": resume_skills & job_skills,
        "missing": job_skills - resume_skills,
        "additional": resume_skills - job_skills,
    }


def format_skills(skills: Iterable[str]) -> list[str]:
    return sorted(skills, key=str.casefold)
