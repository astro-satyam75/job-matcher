import streamlit as st
from src.model import compute_similarity
from src.insights import get_skill_counts

st.caption("⚡ ML-powered job matching using TF-IDF + cosine similarity")
st.set_page_config(page_title="AI Job Matcher", layout="wide")

st.title("🌍 Remote Job Matcher")
st.write("Paste your resume and find matching remote jobs + skill gaps")

# Sidebar (small upgrade)
st.sidebar.header("Settings")
top_n = st.sidebar.slider("Number of jobs to show", 3, 10, 5)

# Input
resume = st.text_area("Paste your resume here", height=200)

if st.button("Analyze Jobs"):

    if resume.strip() == "":
        st.warning("Please paste your resume first")
    else:
        results = compute_similarity(resume)

        st.subheader("🔝 Top Job Matches")

        top_results = results.head(top_n)

        st.write("### 📊 Summary")
        st.write(f"Total Jobs Analyzed: {len(results)}")

        for _, row in top_results.iterrows():

            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown(f"### {row['title']} at {row['company']}")

                if row['missing_skills']:
                    st.error("Missing Skills: " + ", ".join(row['missing_skills']))
                else:
                    st.success("Strong Match - No major skill gaps")

                with st.expander("📄 View Job Description"):
                    st.write(row['description'])

            with col2:
                score = float(row['final_score'])
                st.metric("Match Score", f"{round(score, 2)}")
                st.progress(score)

st.subheader("📊 Market Insights")

skill_df = get_skill_counts()

st.bar_chart(skill_df.set_index("skill").head(10))
st.success("Analysis complete ✅")