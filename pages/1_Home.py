import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="SLE-Insight Dashboard",
    page_icon="🧬",
    layout="wide"
)

# ==========================================================
# CSS
# ==========================================================

st.markdown("""
<style>

#MainMenu{
    visibility:hidden;
}

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

.stApp{
    background:#F6F8FC;
}

.block-container{
    max-width:1250px;
    padding-top:2rem;
    padding-bottom:2rem;
}

/* ---------------- HEADER ---------------- */

.main-title{

    font-size:42px;

    font-weight:700;

    color:#154C97;

    margin-bottom:6px;

}

.subtitle{

    font-size:18px;

    color:#64748B;

    margin-bottom:35px;

}

/* ---------------- SECTION ---------------- */

.section{

    font-size:30px;

    font-weight:700;

    color:#154C97;

    margin-top:30px;

    margin-bottom:20px;

}

/* ---------------- METRICS ---------------- */

.metric-card{

    background:white;

    border-radius:20px;

    padding:28px;

    text-align:center;

    box-shadow:0px 8px 25px rgba(0,0,0,.06);

    transition:.25s;

}

.metric-card:hover{

    transform:translateY(-5px);

    box-shadow:0px 15px 30px rgba(0,0,0,.12);

}

.metric-number{

    font-size:48px;

    font-weight:700;

    color:#1565C0;

}

.metric-title{

    font-size:18px;

    font-weight:600;

    margin-top:10px;

}

.metric-sub{

    font-size:14px;

    color:#64748B;

    margin-top:6px;

}

/* ---------------- CARDS ---------------- */

.card{

    background:white;

    border-radius:20px;

    padding:28px;

    border:1px solid #E6EDF5;

    box-shadow:0px 8px 24px rgba(0,0,0,.06);

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""
<div class="main-title">

🧬 SLE-Insight Dashboard

</div>

<div class="subtitle">

Explore transcriptomic biomarkers, diagnostic models,
and study findings through an interactive companion platform.

</div>
""", unsafe_allow_html=True)

# ==========================================================
# RESEARCH STATISTICS
# ==========================================================

st.markdown(
"""
<div class="section">

Research Statistics

</div>
""",
unsafe_allow_html=True
)

c1,c2,c3,c4=st.columns(4)

cards=[

("996","Discovery Cohort","GSE65391"),

("8","Diagnostic Biomarkers","Final Signature"),

("95.5%","Classification Accuracy","Independent Validation"),

("0.983","ROC-AUC","Logistic Regression")

]

for col,(number,title,subtitle) in zip([c1,c2,c3,c4],cards):

    with col:

        st.markdown(f"""

<div class="metric-card">

<div class="metric-number">

{number}

</div>

<div class="metric-title">

{title}

</div>

<div class="metric-sub">

{subtitle}

</div>

</div>

""",unsafe_allow_html=True)
        
# ==========================================================
# EXPLORE SLE-INSIGHT
# ==========================================================

st.markdown(
"""
<div class="section">

Explore SLE-Insight

</div>
""",
unsafe_allow_html=True
)

st.caption("Select a module to begin exploring the platform.")

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")
with col1:

    with st.container(border=True):

        st.markdown("## 🩺 Diagnostic Prediction")

        st.write(
            """
Predict the probability of **Systemic Lupus Erythematosus**
using our transcriptomic biomarker panel and trained
machine learning model.
"""
        )

        if st.button(
            "Launch Diagnosis",
            use_container_width=True,
            key="diag",
        ):
            st.switch_page("pages/3_Diagnosis.py")
with col2:

    with st.container(border=True):

        st.markdown("## 🧬 Biomarker Explorer")

        st.write(
            """
Explore the biological functions,
expression patterns,
and diagnostic significance
of the identified biomarkers.
"""
        )

        if st.button(
            "Explore Biomarkers",
            use_container_width=True,
             key="bio",
        ):
            st.switch_page("pages/5_Biomarker_explorer.py")
        st.markdown("<br>", unsafe_allow_html=True)


       

col3, col4 = st.columns(2, gap="large")
with col3:

    with st.container(border=True):

        st.markdown("## 📖 Study Overview")

        st.write(
            """
Understand the complete study,
including datasets,
preprocessing,
feature selection,
model development,
and validation.
"""
        )

        if st.button(
            "View Study",
            use_container_width=True,
            key="study",
        ):
            st.switch_page("pages/2_Study_Overview.py")
with col4:

    with st.container(border=True):

        st.markdown("## 📈 Model Performance")

        st.write(
            """
Review ROC curves,
confusion matrices,
SHAP interpretation,
calibration,
and external validation.
"""
        )

        if st.button(
            "View Performance",
            use_container_width=True,
            key="perf",
        ):
            st.switch_page("pages/6_Model_Performance.py")
# ==========================================================
# RESEARCH OVERVIEW
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="section">

🔬 Research Overview

</div>
""", unsafe_allow_html=True)

left, right = st.columns([2, 1], gap="large")
with left:

    with st.container(border=True):

        st.subheader("🧬 Study Workflow")

        workflow = Image.open("assets/workflow.png")

        st.image(
            workflow,
            use_container_width=True
        )

        st.caption(
            "Figure 1. Overview of the transcriptomic biomarker discovery, diagnostic modelling, external validation, disease activity analysis, and biological characterization workflow."
        )
with right:

    st.markdown("""
    <style>

    .highlight-card{

        background:white;

        border-radius:18px;

        padding:25px;

        box-shadow:0px 8px 24px rgba(0,0,0,.06);

        border:1px solid #E7EDF5;

    }

    .highlight-item{

        padding:14px 0;

        border-bottom:1px solid #EEF2F7;

    }

    .highlight-item:last-child{

        border-bottom:none;

    }

    .highlight-title{

        color:#154C97;

        font-size:17px;

        font-weight:700;

        margin-bottom:4px;

    }

    .highlight-text{

        color:#64748B;

        font-size:15px;

        line-height:1.5;

    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""

    <div class="highlight-card">

    <h3 style="color:#154C97;margin-top:0;">
    ⭐ Key Highlights
    </h3>

    <div class="highlight-item">

    <div class="highlight-title">
    🧪 Discovery Cohort
    </div>

    <div class="highlight-text">
    996 transcriptomic samples from GEO dataset GSE65391.
    </div>

    </div>

    <div class="highlight-item">

    <div class="highlight-title">
    🧬 Diagnostic Biomarkers
    </div>

    <div class="highlight-text">
    Final 8-gene transcriptomic biomarker signature selected through feature importance analysis.
    </div>

    </div>

    <div class="highlight-item">

    <div class="highlight-title">
    🤖 Machine Learning
    </div>

    <div class="highlight-text">
    Logistic Regression achieved excellent diagnostic performance for SLE prediction.
    </div>

    </div>

    <div class="highlight-item">

    <div class="highlight-title">
    ✅ External Validation
    </div>

    <div class="highlight-text">
    Model performance evaluated using an independent validation cohort.
    </div>

    </div>

    <div class="highlight-item">

    <div class="highlight-title">
    📈 Disease Activity
    </div>

    <div class="highlight-text">
    Biomarkers further investigated for disease severity and activity assessment.
    </div>

    </div>

    </div>

    """, unsafe_allow_html=True)
    
