import streamlit as st

st.set_page_config(page_title="About", layout="wide")

st.title("📄 About the Study")

st.markdown("""
This companion application accompanies the research study on
**transcriptomic biomarker discovery for Systemic Lupus Erythematosus (SLE)**
using explainable artificial intelligence and machine learning.

The application was developed to provide an interactive platform for exploring
the identified biomarkers, biological pathways, diagnostic model performance
and disease activity analyses presented in the manuscript.
""")

st.divider()
st.header("🎯 Study Objectives")

st.markdown("""

The objectives of this study were to:

- Identify robust transcriptomic biomarkers for SLE diagnosis.

- Develop an interpretable machine learning classifier using SHAP-based
feature selection.

- Investigate biomarkers associated with disease activity.

- Perform biological validation using KEGG, Enrichr and STRING analyses.

- Validate the proposed diagnostic model on an independent external dataset.

""")
st.header("🔬 Study Workflow")

st.image(
    "assets/workflow.png",
    use_container_width=True
)

st.caption("""
Overview of the complete analytical workflow employed in this study,
from GEO transcriptomic datasets to biomarker discovery, explainable
machine learning and external validation.
""")


st.header("📊 Datasets Used")

datasets = {

    "Dataset":[

        "GSE65391",
        "GSE88884",
        "GSE61635"

    ],

    "Purpose":[

        "Diagnostic model development",
        "Disease activity analysis",
        "Independent external validation"

    ],

    "Platform":[

        "GPL10558 (Illumina HumanHT-12 V4.0 expression beadchip)",
        "GPL17586 (Illumina HumanHT-12 V4.0 expression beadchip)",
        "GPL570 (Affymetrix Human Genome U133 Plus 2.0 Array)"

    ]

}

st.table(datasets)
st.header("🏆 Key Findings")

left, right = st.columns(2)

with left:

    st.success("""

### Diagnostic Model

• Eight-gene diagnostic signature

• Accuracy: 95.5%

• ROC-AUC: 0.983

• Successfully validated on an
independent external dataset

• Compact and interpretable
Logistic Regression classifier

""")

with right:

    st.info("""

### Biological Findings

• Top 20 disease activity genes identified

• Best disease activity ROC-AUC: 0.706

• Three overlapping biomarkers identified

    • IFI27

    • ZBP1

    • CDCA7

• Functional enrichment performed using
KEGG, Enrichr and STRING analyses

""")
st.header("📚 Citation")

st.info("""
If you use this companion application or the accompanying research in your
work, please cite the associated manuscript once it has been published.

This application was developed as an interactive companion to facilitate the
exploration of transcriptomic biomarkers, explainable machine learning models,
and biological pathway analyses in systemic lupus erythematosus.
""")
st.header("🙏 Acknowledgements")

st.markdown("""
This work was made possible through the availability of publicly accessible
transcriptomic datasets from the Gene Expression Omnibus (GEO). We gratefully
acknowledge the original investigators for generating and sharing these
valuable datasets.

The study also benefited from several open-source bioinformatics and machine
learning libraries, including GEOparse, scikit-learn, SHAP, gseapy, pandas,
NumPy, Matplotlib, Plotly and Streamlit.
""")
st.header("⚠️ Disclaimer")

st.warning("""
SLE-Insights is intended exclusively for research and educational purposes.
The proposed biomarkers, predictive models and biological interpretations have
not been clinically validated for routine diagnostic use and should not be
used as a substitute for professional medical advice or clinical decision-
making.
""")
st.divider()

st.markdown(
"""
<div style="
background:#f8fbff;
border-left:6px solid #2563eb;
padding:30px;
border-radius:18px;
text-align:center;
">

<h2 style="color:#1e3a8a;">
Thank You for Exploring SLE-Insights
</h2>

<p style="
font-size:18px;
line-height:1.8;
color:#374151;
text-align:justify;
">

SLE-Insights was developed as an interactive companion to our research on
transcriptomic biomarker discovery in systemic lupus erythematosus using
explainable artificial intelligence and machine learning.

We hope this platform provides researchers, clinicians and students with an
accessible resource for exploring the methodology, biological insights and
diagnostic framework presented in this study.

</p>

</div>
""",
unsafe_allow_html=True
)

st.caption(
    "SLE-Insights • Explainable AI Companion for Transcriptomic Biomarker Discovery in Systemic Lupus Erythematosus"
)
