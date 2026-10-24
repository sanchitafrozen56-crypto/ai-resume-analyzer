from io import BytesIO

from docx import Document

from analyzer import analyze_resume
from matcher import similarity_score
from resume_parser import extract_text
from skill_extractor import extract_skills, skill_gap


def test_skill_aliases_and_gap():
    resume = "Built Python pipelines with ML, pandas and SQL."
    job = "Python developer needed for machine learning, SQL and Docker."
    assert extract_skills(resume) >= {"Python", "Machine Learning", "Pandas", "SQL"}
    gap = skill_gap(resume, job)
    assert "Machine Learning" in gap["matched"]
    assert "Docker" in gap["missing"]


def test_similarity_is_transparent_and_bounded():
    score = similarity_score("Python SQL data analysis", "Python SQL data analysis")
    assert score == 100.0
    assert 0 <= similarity_score("", "Python") <= 100
    assert similarity_score("the and or", "! ?") == 0.0


def test_docx_extraction_from_memory():
    document = Document()
    document.add_paragraph("Education\nPython projects")
    output = BytesIO()
    document.save(output)
    assert "Python projects" in extract_text(output.getvalue(), "sample.docx")


def test_resume_quality_suggestions_are_evidence_based():
    result = analyze_resume("Built a Python tool that improved processing by 20%.")
    assert result["quantified_achievements"] == 1
    assert result["sections"]["Skills"] is False
    assert any("Skills" in suggestion for suggestion in result["suggestions"])


def test_parser_rejects_invalid_files():
    try:
        extract_text(b"data", "resume.txt")
    except ValueError as exc:
        assert "Unsupported" in str(exc)
    else:
        raise AssertionError("Invalid file type should be rejected")
