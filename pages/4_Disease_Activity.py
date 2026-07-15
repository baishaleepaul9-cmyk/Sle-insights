import streamlit as st

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Disease Activity Analysis",
    page_icon="📈",
    layout="wide"
)

# ==========================================================
# CSS
# ==========================================================

st.markdown("""
<style>

/* ---------- Main ---------- */

.main{
    padding-top:1rem;
}

/* ---------- Header ---------- */

.dashboard-header{
    text-align:center;
    padding:10px 0 10px 0;
}

.dashboard-header h1{
    font-size:42px;
    font-weight:700;
    color:#1E293B;
    margin-bottom:10px;
}

.dashboard-header p{
    max-width:900px;
    margin:auto;
    font-size:17px;
    color:#64748B;
    line-height:1.8;
}

.dashboard-divider{
    height:2px;
    background:#ECECEC;
    margin:40px 0;
}

/* ---------- Statistics ---------- */

.dashboard-card{

    background:white;

    border-radius:18px;

    padding:30px;

    border:1px solid #E5E7EB;

    text-align:center;

    box-shadow:0 8px 24px rgba(15,23,42,.05);

    transition:.25s;

    height:185px;

}

.dashboard-card:hover{

    transform:translateY(-6px);

    box-shadow:0 14px 30px rgba(15,23,42,.08);

}

.dashboard-icon{

    font-size:36px;

}

.dashboard-number{

    margin-top:14px;

    font-size:34px;

    font-weight:700;

    color:#D97706;

}

.dashboard-title{

    margin-top:12px;

    font-size:16px;

    color:#475569;

    font-weight:600;

}

/* ---------- Sections ---------- */

.section-title{

    margin-top:55px;

    margin-bottom:20px;

    font-size:30px;

    font-weight:700;

    color:#1E293B;

}

/* ---------- Overview ---------- */

.info-box{

    background:#FFFDF8;

    border-left:6px solid #F59E0B;

    border-radius:16px;

    padding:28px;

    color:#475569;

    line-height:1.9;

    box-shadow:0 6px 18px rgba(15,23,42,.05);

}

/* ---------- Workflow ---------- */

.workflow-wrapper{

    display:flex;

    justify-content:space-between;

    align-items:flex-start;

    margin-top:35px;

    margin-bottom:45px;

}

.workflow-step{

    flex:1;

    text-align:center;

}

.workflow-circle{

    width:90px;

    height:90px;

    margin:auto;

    border-radius:50%;

    background:#FFF7ED;

    border:3px solid #F59E0B;

    display:flex;

    align-items:center;

    justify-content:center;

    font-size:40px;

}

.workflow-title{

    margin-top:18px;

    font-size:18px;

    font-weight:700;

    color:#1E293B;

}

.workflow-desc{

    margin-top:10px;

    font-size:15px;

    color:#64748B;

    line-height:1.6;

}

.workflow-line{

    flex:.30;

    height:3px;

    background:#F59E0B;

    margin-top:45px;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""

<div class="dashboard-header">

<h1>📈 Disease Activity Analysis</h1>

<p>

Explore transcriptomic biomarkers associated with
<b>Systemic Lupus Erythematosus (SLE)</b> disease activity.

This section summarizes the correlation-based transcriptomic
analysis performed using the
<b>SLE Disease Activity Index (SLEDAI)</b>,
highlighting molecular biomarkers associated with
disease progression.

</p>

</div>

<div class="dashboard-divider"></div>

""", unsafe_allow_html=True)

# ==========================================================
# STATISTICS
# ==========================================================

col1,col2,col3,col4 = st.columns(4)

cards = [

("📊","209","Significant Biomarkers"),

("🧬","20","Candidate Biomarkers"),

("📈","SLEDAI","Disease Activity Measure"),

("🔬","Spearman","Correlation Analysis")

]

for column,(icon,value,title) in zip([col1,col2,col3,col4],cards):

    with column:

        st.markdown(f"""

<div class="dashboard-card">

<div class="dashboard-icon">{icon}</div>

<div class="dashboard-number">

{value}

</div>

<div class="dashboard-title">

{title}

</div>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# OVERVIEW
# ==========================================================

st.markdown("""
<div class="section-title">

📖 Disease Activity Overview

</div>
""", unsafe_allow_html=True)

st.markdown("""

<div class="info-box">

Disease activity analysis was performed using the
<b>Systemic Lupus Erythematosus Disease Activity Index (SLEDAI)</b>
to investigate transcriptomic alterations associated
with disease progression.

<br><br>

Correlation-based analysis identified
<b>209 statistically significant biomarkers</b>.
From these,
<b>20 candidate biomarkers</b>
were prioritized for downstream biological interpretation,
visualization and severity modelling.

</div>

""", unsafe_allow_html=True)

# ==========================================================
# WORKFLOW
# ==========================================================

st.markdown("""
<div class="section-title">

🔬 Research Workflow

</div>
""", unsafe_allow_html=True)

st.markdown("""

<div class="workflow-wrapper">

<div class="workflow-step">

<div class="workflow-circle">🧬</div>

<div class="workflow-title">

Gene Expression

</div>

<div class="workflow-desc">

Normalized transcriptomic
expression profiles

</div>

</div>

<div class="workflow-line"></div>

<div class="workflow-step">

<div class="workflow-circle">📈</div>

<div class="workflow-title">

Spearman Correlation

</div>

<div class="workflow-desc">

Correlation between
gene expression
and SLEDAI

</div>

</div>

<div class="workflow-line"></div>

<div class="workflow-step">

<div class="workflow-circle">📊</div>

<div class="workflow-title">

Significant Biomarkers

</div>

<div class="workflow-desc">

209 biomarkers
identified

</div>

</div>

<div class="workflow-line"></div>

<div class="workflow-step">

<div class="workflow-circle">🧬</div>

<div class="workflow-title">

Top Candidates

</div>

<div class="workflow-desc">

20 biomarkers
prioritized for
downstream analysis

</div>

</div>

</div>

""", unsafe_allow_html=True)
# ==========================================================
# KEY FINDINGS
# ==========================================================

st.markdown("## 📋 Key Findings")

col1, col2 = st.columns(2)

with col1:

    st.info("""
### 📈 Disease Activity Assessment

Disease activity was evaluated using the **Systemic Lupus Erythematosus Disease Activity Index (SLEDAI)**, providing a standardized clinical measure of disease severity.
""")

    st.success("""
### 📊 Significant Biomarkers

**209 statistically significant transcriptomic biomarkers** were identified through Spearman correlation analysis, highlighting genes associated with increasing disease activity.
""")

with col2:

    st.warning("""
### 🧬 Candidate Biomarkers

The **20 highest-ranking biomarkers** were prioritized for downstream biological interpretation, visualization, and exploratory severity modelling.
""")

    st.info("""
### 🔬 Biological Insight

The identified biomarkers provide valuable insight into the molecular mechanisms underlying **SLE disease progression** and represent promising candidates for future biological and clinical validation.
""")
    