"""Transparent lexical matching with TF-IDF and cosine similarity."""
from __future__ import annotations

import re
from nltk.tokenize import wordpunct_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def preprocess(text: str) -> str:
    tokens = wordpunct_tokenize(text.lower())
    return " ".join(token for token in tokens if re.fullmatch(r"[a-z0-9+#.]+", token))


def similarity_score(resume_text: str, job_text: str) -> float:
    """Return a 0-100 estimated similarity score."""
    if not resume_text.strip() or not job_text.strip():
        return 0.0
    documents = [preprocess(resume_text), preprocess(job_text)]
    if not any(documents):
        return 0.0
    try:
        matrix = TfidfVectorizer(stop_words="english").fit_transform(documents)
    except ValueError as exc:
        if "empty vocabulary" in str(exc).lower():
            return 0.0
        raise
    if matrix.shape[1] == 0:
        return 0.0
    return round(float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0] * 100), 2)
