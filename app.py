import streamlit as st
import plotly.express as px
import recommender



from recommender import recommend_jobs
from utils import get_all_skills, analyze_skill_gap

# =====================================================
# Page Config
# =====================================================

st.set_page_config(
    page_title="AI Tech Stack Recommender",
    page_icon="🤖",
    layout="wide"
)

# =====================================================
# Load CSS
# =====================================================

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css("style.css")

# =====================================================
# Sidebar
# =====================================================

with st.sidebar:

    st.title("🤖 AI Tech Stack Recommender")

    st.markdown("---")

    st.subheader("📌 About")

    st.write("""
This AI-powered recommendation system suggests the best IT job roles based on your technical skills.

### Technologies Used

- Python
- Pandas
- Scikit-Learn
- TF-IDF
- Cosine Similarity
- Streamlit
- Plotly
""")

    st.markdown("---")

    st.subheader("💡 Example Skills")

    st.write("""
Python

Machine Learning

TensorFlow

SQL

Java

Spring Boot

Docker

AWS

React

Node.js
""")

# =====================================================
# Header
# =====================================================

st.markdown(
    """
<div class="main-title">
🤖 AI Tech Stack Recommendation System
</div>
""",
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="sub-title">
Discover the best IT job roles based on your technical skills using Artificial Intelligence.
</div>
""",
    unsafe_allow_html=True
)

st.markdown("---")

# =====================================================
# Skill Selection
# =====================================================

all_skills = get_all_skills()

selected_skills = st.multiselect(
    "💻 Select Your Skills",
    options=all_skills
)

user_skills = ", ".join(selected_skills)

# =====================================================
# Recommend Button
# =====================================================

if st.button("🚀 Recommend Jobs", use_container_width=True):

    if not selected_skills:

        st.warning("Please select at least one skill.")

    else:

        recommendations = recommend_jobs(user_skills)
        

        # ======================================
# Hero Recommendation Card
# ======================================

        best_job = recommendations.iloc[0]

        st.markdown(
            f"""
            <div style="
                background: linear-gradient(90deg,#2563EB,#1E40AF);
                color:white;
                padding:25px;
                border-radius:15px;
                margin-bottom:20px;
                box-shadow:0px 4px 15px rgba(0,0,0,0.2);
            ">

            <h2>🏆 Best Match</h2>

            <h1>{best_job['Job Title']}</h1>

            <h3>🎯 Match Score: {best_job['Match Score']*100:.2f}%</h3>

            </div>
            """,
            unsafe_allow_html=True
        )

        # ==========================================
        # Dashboard Metrics
        # ==========================================

        st.markdown("## 📊 Dashboard")

        col1, col2, col3 = st.columns(3)

        highest = recommendations.iloc[0]["Match Score"] * 100

        with col1:
            st.metric(
                label="💼 Jobs Found",
                value=len(recommendations)
            )

        with col2:
            st.metric(
                label="🛠 Skills Selected",
                value=len(selected_skills)
            )

        with col3:
            st.metric(
                label="🎯 Best Match",
                value=f"{highest:.2f}%"
            )

        st.markdown("---")

        

        # ==========================================
        # Chart
        # ==========================================

       # ==========================================
# Job Match Chart
# ==========================================

        chart_df = recommendations.copy()

        chart_df["Percentage"] = chart_df["Match Score"] * 100

        fig = px.bar(
            chart_df,
            x="Percentage",
            y="Job Title",
            orientation="h",
            text=chart_df["Percentage"].apply(lambda x: f"{x:.1f}%"),
            color="Percentage",
            color_continuous_scale="Blues",
            title="📊 Top Matching Jobs"
        )

        fig.update_traces(
            textposition="outside"
        )

        fig.update_layout(
            height=320,
            coloraxis_showscale=False,
            yaxis=dict(categoryorder="total ascending"),
            xaxis_title="Match Percentage",
            yaxis_title="",
            margin=dict(l=20, r=20, t=50, b=20)
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

        # ==========================================
        # Recommendations
        # ==========================================
        
        for _, row in recommendations.iterrows():

            st.markdown(
                '<div class="card">',
                unsafe_allow_html=True
            )

            st.subheader(f"💼 {row['Job Title']}")
            
            #st.write(row)

            score = float(row["Match Score"])

            st.progress(score)

            st.metric(
                "🎯 Match Score",
                f"{score*100:.2f}%"
            )

            left, right = st.columns(2)

            with left:

                st.markdown("### 🛠 Required Skills")

                st.info(row["Skills"])

                matched, missing = analyze_skill_gap(
                    user_skills,
                    row["Skills"]
                )

                st.markdown("### ✅ Skills You Already Have")

                if matched:

                    for skill in matched:
                        st.success(skill.title())

                else:
                    st.write("No matching skills found.")

                st.markdown("### 📚 Skills To Learn")

                if missing:

                    for skill in missing:
                        st.warning(skill.title())

                else:

                    st.success(
                        "You already have all required skills!"
                    )

            with right:

                st.markdown("### 🎓 Recommended Certifications")

                st.success(
                    row["Certifications"]
                )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

        # ==========================================
        # Download CSV
        # ==========================================

        st.markdown("---")

        csv = recommendations.to_csv(index=False)

        st.download_button(
            "📥 Download Recommendations",
            data=csv,
            file_name="job_recommendations.csv",
            mime="text/csv",
            use_container_width=True
        )

# =====================================================
# Footer
# =====================================================

st.markdown("---")

st.caption(
    "Built with ❤️ using Python • Streamlit • Scikit-Learn • Plotly"
)