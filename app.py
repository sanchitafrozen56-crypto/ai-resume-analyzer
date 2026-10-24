"""Streamlit entry point for the AI Resume Analyzer."""
from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from analyzer import analyze_resume
from matcher import similarity_score
from report_generator import report_pdf, report_text
from resume_parser import extract_text
from skill_extractor import format_skills, skill_gap

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

ROLE_STARTERS = {
    "Python Developer": "Python developer with experience in Python, APIs, SQL, Git, testing, and Docker.",
    "Data Analyst": "Data analyst with experience in Python, SQL, pandas, statistics, Excel, and data visualization.",
    "Software Developer": "Software developer with experience in programming, Git, REST APIs, databases, testing, and cloud tools.",
    "AI/ML Engineer": "AI/ML engineer with experience in Python, machine learning, scikit-learn, pandas, SQL, and model deployment.",
    "Other": "Paste the complete job description here, including responsibilities, tools, and qualifications.",
}

st.markdown("""
<style>
:root { --ink:#17202a; --muted:#607080; --accent:#0b7285; --soft:#e6f4f1; }
.block-container { max-width: 1200px; padding-top: 2rem; }
.hero { padding: 1.5rem 0 1rem; border-bottom: 1px solid #d9e2e8; margin-bottom: 1.5rem; }
.hero h1 { color: var(--ink); letter-spacing: -0.03em; margin-bottom: .25rem; }
.hero p { color: var(--muted); font-size: 1.05rem; }
[data-testid="stMetricValue"] { color: var(--accent); }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>AI Resume Analyzer</h1><p>Evidence-based resume and job description comparison for clearer applications.</p></div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("Analyze")
    uploaded = st.file_uploader("Resume file", type=["pdf", "docx"], help="Processed temporarily in memory; it is not saved by this app.")
    role = st.selectbox("Target role", ["Python Developer", "Data Analyst", "Software Developer", "AI/ML Engineer", "Other"])
    st.caption("Your resume is processed temporarily in memory and is not persisted by default.")

job_text = st.text_area("Job description", height=260, placeholder=ROLE_STARTERS[role])
analyze = st.button("Analyze resume", type="primary", use_container_width=True)

if analyze:
    if uploaded is None:
        st.error("Upload a PDF or DOCX resume first.")
    elif not job_text.strip():
        st.error("Paste a job description first.")
    else:
        try:
            resume_text = extract_text(uploaded.getvalue(), uploaded.name)
        except ValueError as exc:
            st.error(str(exc))
        else:
            gap = skill_gap(resume_text, job_text)
            quality = analyze_resume(resume_text)
            result = {
                "score": similarity_score(resume_text, job_text),
                "matched_skills": format_skills(gap["matched"]),
                "missing_skills": format_skills(gap["missing"]),
                "additional_skills": format_skills(gap["additional"]),
                "quality": quality,
            }
            st.session_state["result"] = result

result = st.session_state.get("result")
if result:
    st.divider()
    st.subheader("Analysis dashboard")
    st.caption("The match score is TF-IDF cosine similarity: an estimate of textual overlap, not an ATS guarantee or hiring probability.")
    score_col, matched_col, missing_col = st.columns(3)
    score_col.metric("Estimated match", f"{result['score']:.1f}%")
    score_col.progress(min(result["score"] / 100, 1.0))
    matched_col.metric("Matched skills", len(result["matched_skills"]))
    missing_col.metric("Skills to review", len(result["missing_skills"]))

    left, right = st.columns(2)
    with left:
        st.markdown("#### Skill coverage")
        st.write(", ".join(result["matched_skills"]) or "No configured skills detected in both texts.")
        st.markdown("#### Missing from resume")
        st.write(", ".join(result["missing_skills"]) or "No missing configured skills detected.")
        st.markdown("#### Additional resume skills")
        st.write(", ".join(result["additional_skills"]) or "No additional configured skills detected.")
    with right:
        st.markdown("#### Resume structure")
        section_df = pd.DataFrame({"Section": list(result["quality"]["sections"].keys()), "Found": ["Found" if value else "Missing" for value in result["quality"]["sections"].values()]})
        fig = px.bar(section_df, x="Found", y="Section", color="Found", color_discrete_map={"Found": "#0b7285", "Missing": "#e9a23b"}, orientation="h")
        fig.update_layout(height=270, showlegend=False, margin=dict(l=0, r=0, t=10, b=10))
        st.plotly_chart(fig, use_container_width=True)
        st.write(f"Action verbs detected: {', '.join(result['quality']['action_verbs']) or 'None'}")
        st.write(f"Quantified achievements detected: {result['quality']['quantified_achievements']}")

    st.markdown("#### Practical improvements")
    for suggestion in result["quality"]["suggestions"]:
        st.info(suggestion)

    st.markdown("#### Download report")
    d1, d2 = st.columns(2)
    d1.download_button("Download TXT", report_text(result), "resume-analysis.txt", "text/plain", use_container_width=True)
    d2.download_button("Download PDF", report_pdf(result), "resume-analysis.pdf", "application/pdf", use_container_width=True)
else:
    st.info("Upload a resume and paste a job description to begin.")
