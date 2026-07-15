import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Study Overview",
    page_icon="📖",
    layout="wide"
)

# ==========================================================
# CSS
# ==========================================================

st.markdown("""
<style>

/* Hide Streamlit elements */

#MainMenu{
    visibility:hidden;
}

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* Background */

.stApp{
    background:#F6F8FC;
}

/* Page Width */

.block-container{
    max-width:1250px;
    padding-top:2rem;
    padding-bottom:2rem;
}

/* -------------------------
   PAGE TITLES
--------------------------*/

.page-title{

    font-size:46px;

    font-weight:700;

    color:#154C97;

    margin-bottom:8px;

}

.page-subtitle{

    font-size:18px;

    color:#64748B;

    line-height:1.8;

    margin-bottom:40px;

}

.section-title{

    font-size:30px;

    font-weight:700;

    color:#154C97;

    margin-top:45px;

    margin-bottom:22px;

}

/* -------------------------
   MAIN CARD
--------------------------*/

.main-card{

    background:white;

    border-radius:20px;

    padding:35px;

    border:1px solid #E8EDF5;

    box-shadow:0 8px 24px rgba(0,0,0,.06);

}

.objective{

    font-size:18px;

    line-height:1.9;

    color:#4B5563;

}

/* -------------------------
   INFO CARDS
--------------------------*/

.info-card{

    background:white;

    border-radius:18px;

    padding:28px 22px;

    border:1px solid #E8EDF5;

    box-shadow:0 8px 22px rgba(0,0,0,.06);

    min-height:220px;

    text-align:center;

    transition:.25s;

}

.info-card:hover{

    transform:translateY(-6px);

    border-color:#1565C0;

    box-shadow:0 18px 32px rgba(21,101,192,.16);

}

.info-icon{

    font-size:42px;

    margin-bottom:18px;

}

.info-title{

    font-size:22px;

    font-weight:700;

    color:#1565C0;

    margin-bottom:14px;

}

.info-subtitle{

    font-size:16px;

    color:#64748B;

    line-height:1.6;

}
            
/* ---------- RESEARCH OUTCOMES ---------- */

.outcome-card{
    background:#FFFFFF;
    border-radius:18px;
    padding:28px 24px;
    border-top:6px solid #1565C0;
    border-left:1px solid #E8EDF5;
    border-right:1px solid #E8EDF5;
    border-bottom:1px solid #E8EDF5;
    box-shadow:0 8px 22px rgba(0,0,0,.06);
    min-height:280px;
    transition:all .25s ease;
}

.outcome-card:hover{
    transform:translateY(-6px);
    box-shadow:0 18px 30px rgba(21,101,192,.16);
}

.outcome-icon{
    font-size:42px;
}

.outcome-number{
    font-size:48px;
    font-weight:700;
    color:#1565C0;
    margin-top:12px;
}

.outcome-title{
    font-size:22px;
    font-weight:700;
    color:#154C97;
    margin-top:10px;
    margin-bottom:14px;
}

.outcome-text{
    font-size:15px;
    color:#64748B;
    line-height:1.7;
}
            
</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""
<div class="page-title">

📖 Study Overview

</div>

<div class="page-subtitle">

Explore the study rationale, methodology, biomarker discovery process,
and machine learning framework developed for the diagnosis of
Systemic Lupus Erythematosus (SLE).

</div>
""", unsafe_allow_html=True)
# ==========================================================
# RESEARCH OBJECTIVE
# ==========================================================

st.markdown("""
<div class="section-title">

🎯 Research Objective

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-card">

<div class="objective">

The primary objective of this study was to develop an interpretable
<b>transcriptomic machine learning framework</b> for the accurate diagnosis of
<b>Systemic Lupus Erythematosus (SLE)</b>. The proposed framework integrates
feature selection, predictive modelling, biological interpretation, and
independent external validation to identify robust diagnostic biomarkers
while maintaining clinical interpretability.

</div>

</div>
""", unsafe_allow_html=True)
# ==========================================================
# WHY THIS STUDY?
# ==========================================================

st.markdown("""
<div class="section-title">

🩺 Why This Study?

</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4, gap="large")

cards = [
    (
        "⚠️",
        "Clinical\nHeterogeneity",
        "Complex and diverse disease manifestations"
    ),
    (
        "⏱️",
        "Delayed\nDiagnosis",
        "Symptoms overlap with other autoimmune diseases"
    ),
    (
        "📈",
        "Disease\nActivity",
        "Continuous monitoring is required due to fluctuating severity"
    ),
    (
        "🧬",
        "Need for\nBiomarkers",
        "Reliable transcriptomic signatures for accurate diagnosis"
    )
]

for col, (icon, title, subtitle) in zip([col1, col2, col3, col4], cards):

    with col:

        st.markdown(f"""
<div class="info-card">

<div class="info-icon">

{icon}

</div>

<div class="info-title">

{title.replace(chr(10),"<br>")}

</div>

<div class="info-subtitle">

{subtitle}

</div>

</div>
""", unsafe_allow_html=True)
# ==========================================================
# RESEARCH OUTCOMES
# ==========================================================

st.markdown("""
<div class="section-title">

🔬 Research Outcomes

</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3, gap="large")

# ---------------- Diagnostic ----------------

with c1:

    st.markdown("""
<div class="outcome-card">

<div class="outcome-icon">🧬</div>

<div class="outcome-number">
8
</div>

<div class="outcome-title">
Diagnostic Biomarkers
</div>

<div class="outcome-text">

Eight transcriptomic biomarkers identified for accurate SLE diagnosis using SHAP-based feature selection.

</div>

</div>
""", unsafe_allow_html=True)

# ---------------- Severity ----------------

with c2:

    st.markdown("""
<div class="outcome-card">

<div class="outcome-icon">📈</div>

<div class="outcome-number">
20
</div>

<div class="outcome-title">
Severity-associated Genes
</div>

<div class="outcome-text">

Twenty genes associated with disease activity were identified for severity modelling and biological interpretation.

</div>

</div>
""", unsafe_allow_html=True)

# ---------------- Overlap ----------------

with c3:

    st.markdown("""
<div class="outcome-card">

<div class="outcome-icon">⭐</div>

<div class="outcome-number">
3
</div>

<div class="outcome-title">
Overlapping Genes
</div>

<div class="outcome-text">

<b>IFI27</b><br>
<b>ZBP1</b><br>
<b>CDCA7</b>

</div>

</div>
""", unsafe_allow_html=True)
# ==========================================================
# STUDY SUMMARY
# ==========================================================

st.markdown("""
<div class="section-title">

📝 Study Summary

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-card">

<div class="objective">

This study presents an interpretable transcriptomic machine learning framework for the diagnosis of Systemic Lupus Erythematosus (SLE). By integrating feature selection, predictive modelling, external validation, and disease activity analysis, the framework identified robust diagnostic biomarkers and severity-associated genes with strong biological relevance.

<br>
The discovery of three overlapping biomarkers (<b>IFI27</b>, <b>ZBP1</b>, and <b>CDCA7</b>) across both diagnostic and disease activity analyses highlights their potential as clinically relevant biomarkers for SLE diagnosis and disease monitoring.

</div>

</div>
""", unsafe_allow_html=True)

    
