"""Generate plain-text and PDF analysis reports."""
from __future__ import annotations

from io import BytesIO


def report_text(result: dict) -> str:
    quality = result["quality"]
    sections = "\n".join(f"- {name}: {'Found' if found else 'Missing'}" for name, found in quality["sections"].items())
    return "\n".join([
        "AI RESUME ANALYZER REPORT", "=" * 26, "", f"Estimated match score: {result['score']:.2f}%",
        "", "MATCHED SKILLS", ", ".join(result["matched_skills"]) or "None detected",
        "", "MISSING SKILLS", ", ".join(result["missing_skills"]) or "None detected",
        "", "ADDITIONAL RESUME SKILLS", ", ".join(result["additional_skills"]) or "None detected",
        "", "RESUME SECTIONS", sections, "", "IMPROVEMENT SUGGESTIONS",
        *(f"- {item}" for item in quality["suggestions"]), "",
        "Note: This is an estimated lexical similarity score, not an ATS guarantee or hiring probability.",
    ])


def report_pdf(result: dict) -> bytes:
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    buffer = BytesIO()
    page = canvas.Canvas(buffer, pagesize=letter)
    page.setTitle("AI Resume Analyzer Report")
    y = 750
    for line in report_text(result).splitlines():
        if y < 45:
            page.showPage(); y = 750
        page.drawString(45, y, line[:110])
        y -= 15
    page.save()
    return buffer.getvalue()
