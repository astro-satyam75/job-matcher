import streamlit as st
import pandas as pd

from src.parser import parse_resume
from src.fetch_jobs import fetch_remote_jobs
from src.matcher import compute_similarity
from src.skills import extract_skills


st.set_page_config(
    page_title="AI Remote Job Matcher",
    layout="wide"
)

st.title("🌍 AI Remote Job Matcher")

st.caption(
    "⚡ Live remote jobs matched using AI semantic similarity"
)

st.write(
    "Upload your resume and find matching remote jobs instantly"
)

# =========================
# Sidebar
# =========================

st.sidebar.header("Settings")

top_n = st.sidebar.slider(
    "Number of jobs to show",
    5,
    50,
    10
)

min_score = st.sidebar.slider(
    "Minimum Match %",
    0,
    100,
    0
)

# =========================
# Resume Upload
# =========================

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

# =========================
# Main Logic
# =========================

if uploaded_file:

    with st.spinner("📄 Parsing resume..."):

        resume_text = parse_resume(uploaded_file)

    st.success("Resume uploaded successfully ✅")

    if st.button("Analyze Jobs"):

        # =========================
        # Fetch Jobs
        # =========================

        with st.spinner("🌐 Fetching live remote jobs..."):

            jobs_df = fetch_remote_jobs()

        # =========================
        # Compute Similarity
        # =========================

        with st.spinner("🧠 Matching jobs using AI..."):

            results = compute_similarity(
                resume_text,
                jobs_df
            )

        # =========================
        # Filter Results
        # =========================

        results["match_percent"] = (
            results["match_score"] * 100
        )

        # results = results[
        #     results["match_percent"] >= min_score
        # ]

        results = results.head(top_n)

        # =========================
        # Resume Skills
        # =========================

        resume_skills = extract_skills(
            resume_text
        )

        # =========================
        # Results
        # =========================

        st.subheader("🔝 Top Job Matches")

        st.write(
            f"Total Jobs Found: {len(results)}"
        )

        for _, row in results.iterrows():

            job_description = row["description"]

            job_skills = extract_skills(
                job_description
            )

            missing_skills = (
                job_skills - resume_skills
            )

            score = round(
                row["match_percent"],
                2
            )

            # =========================
            # Layout
            # =========================

            col1, col2 = st.columns([4, 1])

            with col1:

                st.markdown(
                    f"## {row['title']}"
                )

                st.write(
                    f"🏢 {row['company']}"
                )

                st.write(
                    f"🌍 {row['location']}"
                )

                if missing_skills:

                    st.error(
                        "Missing Skills: "
                        + ", ".join(missing_skills)
                    )

                else:

                    st.success(
                        "Strong Match - No major skill gaps"
                    )

                with st.expander(
                    "📄 View Job Description"
                ):

                    st.write(
                        job_description
                    )

                if row["apply_link"]:

                    st.link_button(
                        "🚀 Apply Now",
                        row["apply_link"]
                    )

            with col2:

                st.metric(
                    "Match %",
                    f"{score}%"
                )

                st.progress(
                    min(score / 100, 1.0)
                )

            st.divider()

        # =========================
        # Market Insights
        # =========================

        st.subheader("📊 Skill Insights")

        all_skills = []

        for desc in results[
            "description"
        ]:

            extracted = extract_skills(desc)

            all_skills.extend(
                list(extracted)
            )

        if all_skills:

            skill_df = pd.DataFrame(
                all_skills,
                columns=["skill"]
            )

            skill_counts = (
                skill_df["skill"]
                .value_counts()
                .reset_index()
            )

            skill_counts.columns = [
                "skill",
                "count"
            ]

            st.bar_chart(
                skill_counts.set_index(
                    "skill"
                )
            )

        st.success(
            "Analysis complete ✅"
        )