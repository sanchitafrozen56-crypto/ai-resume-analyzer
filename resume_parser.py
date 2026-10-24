"""Safe, temporary extraction of text from PDF and DOCX resumes."""
from __future__ import annotations

from io import BytesIO
from pathlib import Path


def extract_text(file_bytes: bytes, filename: str) -> str:
    """Extract text from a PDF or DOCX byte payload without writing it to disk."""
    if not file_bytes:
        raise ValueError("The uploaded file is empty.")
    suffix = Path(filename).suffix.lower()
    if suffix == ".pdf":
        return _extract_pdf(file_bytes)
    if suffix == ".docx":
        return _extract_docx(file_bytes)
    raise ValueError("Unsupported file type. Upload a PDF or DOCX file.")


def _extract_pdf(file_bytes: bytes) -> str:
    from PyPDF2 import PdfReader

    try:
        reader = PdfReader(BytesIO(file_bytes))
        text = "\n".join(page.extract_text() or "" for page in reader.pages).strip()
    except Exception as exc:
        raise ValueError("The PDF could not be read. It may be encrypted or malformed.") from exc
    if not text:
        raise ValueError(
            "No selectable text was found in this PDF. It may be a scanned/image-only PDF. "
            "Export it as a text PDF or upload the resume as a DOCX file."
        )
    return text


def _extract_docx(file_bytes: bytes) -> str:
    from docx import Document

    try:
        document = Document(BytesIO(file_bytes))
        parts = [paragraph.text.strip() for paragraph in document.paragraphs]
        parts.extend(cell.text.strip() for table in document.tables for row in table.rows for cell in row.cells)
        text = "\n".join(part for part in parts if part).strip()
    except Exception as exc:
        raise ValueError("The DOCX could not be read. It may be malformed.") from exc
    if not text:
        raise ValueError("No readable text was found in the DOCX.")
    return text
