import streamlit as st
import pandas as pd

from gene_database import gene_database
from utils.kegg_loader import load_kegg, get_gene_pathways

st.set_page_config(
    page_title="Biomarker Explorer",
    page_icon="🧬",
    layout="wide"
)

st.markdown("""
<style>

/* ---------- Metric Cards ---------- */

.metric-card{
    background:#ffffff;
    border-radius:18px;
    padding:18px 15px;
    text-align:center;
    border:1px solid #edf2f7;
    box-shadow:0 4px 14px rgba(0,0,0,0.06);
    transition:all .25s ease;
    min-height:165px;

    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
}

.metric-card:hover{
    transform:translateY(-4px);
    box-shadow:0 10px 24px rgba(0,0,0,0.10);
}

/* ---------- Icon ---------- */

.metric-icon{
    width:55px;
    height:55px;

    display:flex;
    justify-content:center;
    align-items:center;

    border-radius:50%;
    font-size:26px;
    margin-bottom:12px;
}

/* ---------- Main Value ---------- */

.metric-value{
    font-size:28px;
    font-weight:700;
    margin-bottom:8px;
    line-height:1.2;
}

/* ---------- Label ---------- */

.metric-label{
    font-size:14px;
    color:#6b7280;
    font-weight:500;
}

/* ---------- Blue ---------- */

.blue .metric-icon{
    background:#e8f1ff;
}

.blue .metric-value{
    color:#2563eb;
}

/* ---------- Green ---------- */

.green .metric-icon{
    background:#eafaf0;
}

.green .metric-value{
    color:#16a34a;
}

/* ---------- Purple ---------- */

.purple .metric-icon{
    background:#f4edff;
}

.purple .metric-value{
    color:#7c3aed;
}

/* ---------- Gold ---------- */

.gold .metric-icon{
    background:#fff8e6;
}

.gold .metric-value{
    color:#d97706;
}

/* ---------- Responsive ---------- */

@media (max-width:900px){

.metric-card{
    min-height:140px;
    padding:15px;
}

.metric-value{
    font-size:24px;
}

.metric-icon{
    width:48px;
    height:48px;
    font-size:22px;
}

}

</style>
""", unsafe_allow_html=True)
# ==========================================================
# PAGE HEADER
# ==========================================================

st.markdown("""
<div style='
    background: linear-gradient(135deg,#1e3c72,#2563eb);
    padding:35px;
    border-radius:20px;
    color:white;
    margin-bottom:35px;
'>
<h1 style='margin:0;'>🧬 Biomarker Explorer</h1>

<p style='font-size:20px; margin-top:15px;'>
Explore the biological significance of transcriptomic biomarkers identified in this study.
</p>

<p style='font-size:18px; opacity:0.9;'>
The explorer integrates biological function, study evidence, KEGG pathway enrichment,
protein interaction networks, and literature evidence into a single interactive interface.
</p>

</div>
""", unsafe_allow_html=True)


# ==========================================================
# GENE SELECTOR
# ==========================================================

st.markdown("## 🔎 Search Biomarker")

gene_list = sorted(gene_database.keys())

selected_gene = st.selectbox(
    "",
    gene_list
)

gene = gene_database[selected_gene]


st.divider()
# ==========================================================
# GENE INFORMATION
# ==========================================================

st.markdown("## 📖 Gene Information")

col1, col2 = st.columns(2)

with col1:
    st.info(f"""
### 🧬 Full Gene Name

**{gene["general"]["full_name"]}**
""")

with col2:
    st.success(f"""
### 🧪 Encoded Protein

**{gene["general"]["protein"]}**
""")

st.markdown("<br>", unsafe_allow_html=True)
# ==========================================================
# BIOLOGICAL FUNCTION
# ==========================================================

st.markdown("## 🧬 Biological Function")

col1, col2, col3 = st.columns(3, gap="large")

with col1:

    st.markdown(f"""
    <div style="
        background:linear-gradient(180deg,#f8fbff,#eef4ff);
        border-left:6px solid #4f46e5;
        border-radius:18px;
        padding:22px;
        min-height:340px;
        box-shadow:0 6px 18px rgba(0,0,0,0.08);
    ">

    <h3 style="
        margin-top:0;
        color:#4338ca;
        font-size:28px;
    ">
    ⚙️ Function
    </h3>

    <hr style="margin:15px 0;">

    <p style="
        font-size:17px;
        color:#374151;
        line-height:1.9;
        text-align:justify;
    ">
    {gene["biology"]["function"]}
    </p>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown(f"""
    <div style="
        background:linear-gradient(180deg,#f8fff9,#eefdf5);
        border-left:6px solid #16a34a;
        border-radius:18px;
        padding:22px;
        min-height:340px;
        box-shadow:0 6px 18px rgba(0,0,0,0.08);
    ">

    <h3 style="
        margin-top:0;
        color:#15803d;
        font-size:28px;
    ">
    🦠 Role in SLE
    </h3>

    <hr style="margin:15px 0;">

    <p style="
        font-size:17px;
        color:#374151;
        line-height:1.9;
        text-align:justify;
    ">
    {gene["biology"]["role_sle"]}
    </p>

    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown(f"""
    <div style="
        background:linear-gradient(180deg,#fffdf7,#fff7ed);
        border-left:6px solid #ea580c;
        border-radius:18px;
        padding:22px;
        min-height:340px;
        box-shadow:0 6px 18px rgba(0,0,0,0.08);
    ">

    <h3 style="
        margin-top:0;
        color:#c2410c;
        font-size:28px;
    ">
    🏥 Clinical Significance
    </h3>

    <hr style="margin:15px 0;">

    <p style="
        font-size:17px;
        color:#374151;
        line-height:1.9;
        text-align:justify;
    ">
    {gene["biology"]["clinical_significance"]}
    </p>

    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
# ==========================================================
# STUDY EVIDENCE
# ==========================================================

st.markdown("## 📑 Study Evidence")

left, right = st.columns(2, gap="large")

# ==========================================================
# LEFT CARD
# ==========================================================

status_html = ""

if gene["study"]["shap_selected"]:
    status_html += "<p style='font-size:18px;margin-bottom:16px;'>✅ SHAP Selected</p>"

if gene["study"]["final_signature"]:
    status_html += "<p style='font-size:18px;margin-bottom:16px;'>✅ Final Diagnostic Signature</p>"

if gene["study"]["diagnostic_biomarker"]:
    status_html += "<p style='font-size:18px;margin-bottom:16px;'>✅ Diagnostic Biomarker</p>"

if gene["study"]["disease_activity_biomarker"]:
    status_html += "<p style='font-size:18px;margin-bottom:16px;'>✅ Disease Activity Biomarker</p>"

if gene["study"]["shared_biomarker"]:
    status_html += "<p style='font-size:18px;margin-bottom:16px;'>⭐ Overlapping Biomarker</p>"

with left:

    st.markdown(f"""
    <div style="
        background:#f8fbff;
        border-left:6px solid #2563eb;
        border-radius:18px;
        padding:28px;
        box-shadow:0 6px 18px rgba(0,0,0,.06);
        min-height:340px;
    ">

    <h2 style="margin-top:0;color:#2563eb;">
    📌 Biomarker Status
    </h2>

    <hr style="margin-bottom:20px;">

    {status_html}

    </div>
    """, unsafe_allow_html=True)

# ==========================================================
# RIGHT CARD
# ==========================================================

evidence_html = ""

for item in gene["study"]["evidence"]:

    evidence_html += f"""
    <div style="
        background:white;
        border-left:5px solid #22c55e;
        border-radius:10px;
        padding:14px 18px;
        margin-bottom:12px;
        box-shadow:0 2px 6px rgba(0,0,0,.05);
        font-size:17px;
    ">
        ✅ {item}
    </div>
    """

with right:

    st.markdown(f"""
    <div style="
        background:#f0fdf4;
        border-left:6px solid #16a34a;
        border-radius:18px;
        padding:28px;
        box-shadow:0 6px 18px rgba(0,0,0,.06);
        min-height:340px;
    ">

    <h2 style="margin-top:0;color:#15803d;">
    📄 Evidence from this Study
    </h2>

    <hr style="margin-bottom:20px;">

    {evidence_html}

    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
# ==========================================================
# KEGG PATHWAY ENRICHMENT
# ==========================================================

st.divider()

st.markdown("# 🧬 KEGG Pathway Enrichment")

status = gene["status"]
context = gene["pathway_context"]

available = []

if status["diagnostic"]:
    available.append("Diagnostic Biomarkers")

if status["disease_activity"]:
    available.append("Disease Activity")

if status["shared"]:
    available.append("Overlapping Biomarkers")


# ----------------------------------------------------------
# Choose analysis
# ----------------------------------------------------------

if len(available) == 1:

    analysis = available[0]

else:

    st.markdown(
        """
        Explore the enriched biological pathways associated with this biomarker
        across the available analyses.
        """
    )

    analysis = st.radio(
        "Select Analysis",
        available,
        horizontal=True
    )


# ----------------------------------------------------------
# Select dataset
# ----------------------------------------------------------

if analysis == "Diagnostic Biomarkers":

    kegg = context["diagnostic"]

elif analysis == "Disease Activity":

    kegg = context["severity"]

else:

    kegg = context["overlap"]


# ==========================================================
# DESCRIPTION
# ==========================================================

st.markdown(
f"""
<div style="
background:#f8fbff;
border-left:6px solid #2563eb;
padding:28px;
border-radius:18px;
box-shadow:0 6px 18px rgba(0,0,0,.06);
">

<h2 style="color:#1e3a8a;margin-top:0;">
{kegg["title"]}
</h2>

<p style="
font-size:18px;
line-height:1.8;
text-align:justify;
color:#374151;
margin-bottom:0;
">

{kegg["description"]}

</p>

</div>
""",
unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)


# ==========================================================
# KEGG BARPLOT
# ==========================================================

st.markdown("## 📊 KEGG Enrichment Plot")

col1, col2, col3 = st.columns([1,4,1])

with col2:

    st.image(
        kegg["figure"],
        use_container_width=True
    )

st.markdown("<br>", unsafe_allow_html=True)


# ==========================================================
# ENRICHED PATHWAYS
# ==========================================================

st.markdown("## 📋 Top Enriched KEGG Pathways")

results = pd.DataFrame(kegg["results"])

st.dataframe(
    results,
    use_container_width=True,
    hide_index=True
)

st.markdown("<br>", unsafe_allow_html=True)


# ==========================================================
# BIOLOGICAL INTERPRETATION
# ==========================================================

st.markdown("## 💡 Biological Interpretation")

if analysis == "Diagnostic Biomarkers":

    interpretation = f"""
<b>{gene['general']['symbol']}</b> belongs to the final diagnostic biomarker
panel identified in this study. The enriched pathways indicate participation
in immune dysregulation, interferon signalling and cell-cycle regulation,
supporting its utility as a diagnostic biomarker for systemic lupus
erythematosus.
"""

elif analysis == "Disease Activity":

    interpretation = f"""
<b>{gene['general']['symbol']}</b> is associated with disease activity.
The enriched pathways suggest persistent immune activation together with
cell-cycle regulation and inflammatory signalling during active SLE.
"""

else:

    interpretation = f"""
<b>{gene['general']['symbol']}</b> was identified as an overlapping biomarker
shared between diagnostic and disease activity analyses. These pathways
highlight innate immune activation and inflammatory mechanisms central
to SLE pathogenesis.
"""


st.markdown(
f"""
<div style="
background:#fffdf4;
border-left:6px solid #f59e0b;
padding:25px;
border-radius:18px;
box-shadow:0 6px 18px rgba(0,0,0,.05);
">

<p style="
font-size:18px;
line-height:1.8;
text-align:justify;
margin:0;
color:#374151;
">

{interpretation}

</p>

</div>
""",
unsafe_allow_html=True
)


# ==========================================================
# STRING NETWORK
# ==========================================================

st.divider()

st.markdown("# 🕸 STRING Protein Interaction Network")

st.markdown(gene["string"]["summary"])

st.image(
    gene["string"]["figure"],
    use_container_width=True
)

st.markdown("### Key Interaction Partners")

cols = st.columns(5)

for i, protein in enumerate(gene["string"]["key_interactors"]):

    cols[i % 5].success(protein)


# ==========================================================
# LITERATURE
# ==========================================================

st.divider()

st.markdown("# 📚 Supporting Literature")

st.info(gene["literature"]["summary"])

for paper in gene["literature"]["references"]:

    st.markdown(
        f"""
**{paper['title']}**

*{paper['journal']} ({paper['year']})*
"""
    )


