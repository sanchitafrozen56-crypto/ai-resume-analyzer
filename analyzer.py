"""Resume quality checks based on observable text, never invented claims."""
from __future__ import annotations

import re

SECTION_ALIASES = {
    "Education": ("education", "academic background"), "Skills": ("skills", "technical skills"),
    "Experience": ("experience", "employment", "work history"), "Projects": ("projects", "project experience"),
    "Certifications": ("certifications", "certificates", "credentials"),
}
ACTION_VERBS = {"built", "created", "developed", "designed", "implemented", "optimized", "automated", "analyzed", "led", "improved", "deployed", "reduced", "increased"}


def analyze_resume(text: str) -> dict:
    lower = text.lower()
    sections = {name: any(re.search(r"\b" + re.escape(alias) + r"\b", lower) for alias in aliases) for name, aliases in SECTION_ALIASES.items()}
    words = re.findall(r"\b\w+\b", lower)
    action_verbs = sorted({word for word in words if word in ACTION_VERBS})
    quantified = len(re.findall(r"(?:\b\d+%|\b\d+[+]?\b|\$\d+)", text))
    suggestions: list[str] = []
    if not sections["Skills"]: suggestions.append("Add a clearly labeled Skills section with tools relevant to the target role.")
    if not sections["Projects"]: suggestions.append("Add projects with your contribution, technologies, and measurable outcomes.")
    if not sections["Experience"]: suggestions.append("Add relevant experience, internships, or leadership work if applicable.")
    if not action_verbs: suggestions.append("Start bullet points with precise action verbs such as built, analyzed, or automated.")
    if quantified == 0: suggestions.append("Quantify genuine outcomes where possible; never invent metrics.")
    if len(words) < 120: suggestions.append("Expand concise bullets with context, methods, and results while staying relevant.")
    return {"sections": sections, "action_verbs": action_verbs, "quantified_achievements": quantified, "suggestions": suggestions}
