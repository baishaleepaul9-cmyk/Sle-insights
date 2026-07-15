import streamlit as st
import pandas as pd

st.set_page_config(page_title="Model Development", layout="wide")

st.title("🤖 Model Development & Performance")

st.markdown("""
The final diagnostic classifier was developed using supervised machine learning
after SHAP-based biomarker selection. This section summarizes the complete
model development pipeline, optimization strategy, validation procedures and
overall predictive performance.
""")

# ==========================================================
# MODEL SUMMARY
# ==========================================================

st.markdown("## 📊 Model Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("**Final Model**")
    st.markdown(
        """
        <div style='
        font-size:28px;
        font-weight:700;
        color:#1f2937;
        line-height:1.2;
        '>
        Logistic Regression
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown("**Features**")
    st.markdown(
        """
        <div style='
        font-size:28px;
        font-weight:700;
        color:#2563eb;
        '>
        8 Genes
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown("**Accuracy**")
    st.markdown(
        """
        <div style='
        font-size:28px;
        font-weight:700;
        color:#16a34a;
        '>
        95.5%
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown("**ROC-AUC**")
    st.markdown(
        """
        <div style='
        font-size:28px;
        font-weight:700;
        color:#9333ea;
        '>
        0.983
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()
# ==========================================================
# MODEL CONFIGURATION
# ==========================================================

st.markdown("## ⚙️ Model Configuration")

left, right = st.columns(2)

with left:

    st.info("""
### Preprocessing

- **Feature Scaling:** StandardScaler
- **Train/Test Split:** 80 : 20
- **Random State:** 42
- **Input Features:** Final 8 Biomarkers
""")

with right:

    st.success("""
### Training Strategy

- **Classifier:** Logistic Regression
- **Cross Validation:** Stratified 5-Fold
- **Class Weight:** Balanced
- **Probability Threshold:** 0.90
""")
    # ==========================================================
# MODEL DEVELOPMENT WORKFLOW
# ==========================================================

st.markdown("## 🧬 Model Development Workflow")

st.markdown("""
The complete machine learning pipeline used to construct the final diagnostic
classifier is illustrated below. Beginning with transcriptomic preprocessing,
the workflow includes feature selection using SHAP, supervised model training,
performance evaluation and external validation.
""")

st.image(
    "assets/workflow(2).png",
    use_container_width=True
)

st.caption("""
Figure. Overview of the complete machine learning workflow for SLE diagnosis.
Gene expression profiles were preprocessed and standardized prior to SHAP-based
feature selection. The selected biomarkers were used to train multiple machine
learning classifiers, followed by internal evaluation, calibration and external
validation on an independent cohort.
""")

st.divider()

# ==========================================================
# HYPERPARAMETER OPTIMIZATION
# ==========================================================

st.markdown("## ⚙️ Hyperparameter Optimization")

st.markdown("""
The Logistic Regression classifier was optimized using supervised machine
learning to maximize diagnostic performance while minimizing overfitting.
Model parameters were selected based on cross-validation performance and
generalization ability.
""")

with st.expander("🔧 Final Hyperparameters", expanded=True):

    hp = pd.DataFrame({

        "Parameter":[
            "Penalty",
            "Regularization (C)",
            "Solver",
            "Maximum Iterations",
            "Class Weight",
            "Random State"
        ],

        "Value":[
            "L2",
            "1.0",
            "liblinear",
            "1000",
            "balanced",
            "42"
        ]

    })

    st.table(hp)
    st.success("""
**Optimization Summary**

The final Logistic Regression model was selected after evaluating multiple
machine learning algorithms. Hyperparameter optimization together with
Stratified 5-Fold Cross Validation resulted in a robust classifier that
achieved excellent discrimination while maintaining strong generalization
performance on independent datasets.
""")
# ==========================================================
# WHY LOGISTIC REGRESSION?
# ==========================================================

st.markdown("## ⭐ Why Logistic Regression?")

st.markdown("""
<div style="
background:#f0fdf4;
border-left:6px solid #16a34a;
padding:25px;
border-radius:16px;
box-shadow:0 4px 12px rgba(0,0,0,0.05);
">

<p style="
font-size:17px;
line-height:1.8;
text-align:justify;
color:#374151;
margin:0;
">

Although several machine learning algorithms were evaluated during model
development, <b>Logistic Regression</b> demonstrated the most balanced
combination of diagnostic accuracy, ROC-AUC, calibration performance and
generalization on independent datasets.

Unlike more complex ensemble models, Logistic Regression provides a highly
interpretable probabilistic framework that is particularly suitable for
clinical decision support. Its coefficients allow direct interpretation of
feature contributions, making the final eight-gene biomarker panel easier to
translate into potential diagnostic applications.

The final optimized Logistic Regression classifier therefore served as the
primary diagnostic model throughout this study.

</p>

</div>
""", unsafe_allow_html=True)


# ==========================================================
# MODEL COMPARISON
# ==========================================================

st.markdown("## 📊 Model Comparison")

st.markdown("""
Three supervised machine learning algorithms were evaluated on the top 10,000
most variable genes. Model selection was based on discrimination performance,
stability across cross-validation folds and suitability for downstream
biomarker interpretation.
""")

comparison = pd.DataFrame({

    "Model":[
        "Logistic Regression",
        "XGBoost",
        "Random Forest"
    ],

    "Accuracy (Mean ± SD)":[
        "0.9824 ± 0.0047",
        "0.9698 ± 0.0151",
        "0.9548 ± 0.0100"
    ],

    "ROC-AUC (Mean ± SD)":[
        "0.9918 ± 0.0064",
        "0.9873 ± 0.0104",
        "0.9634 ± 0.0272"
    ],

    "Precision":[
        "0.9866",
        "0.9773",
        "0.9561"
    ],

    "Recall":[
        "0.9946",
        "0.9905",
        "0.9973"
    ],

    "F1-Score":[
        "0.9905",
        "0.9838",
        "0.9762"
    ]

})

st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)

st.success("""
Logistic Regression consistently demonstrated the highest ROC-AUC,
classification accuracy and cross-validation stability, making it the final
classifier selected for biomarker discovery and downstream model development.
""")

st.divider()
# ==========================================================
# MODEL SELECTION
# ==========================================================

st.markdown("## ⭐ Final Model Selection")

st.markdown("""
<div style="
background:#f0fdf4;
border-left:6px solid #22c55e;
padding:25px;
border-radius:16px;
">

<h4 style="color:#166534;">
Why Logistic Regression?
</h4>

<p style="
font-size:17px;
line-height:1.8;
text-align:justify;
">

Although XGBoost and Random Forest achieved competitive predictive
performance, Logistic Regression consistently exhibited the highest
cross-validation ROC-AUC together with excellent stability across folds.
Furthermore, its probabilistic predictions and model interpretability make it
particularly suitable for clinical decision support and biomarker-based
diagnostic applications.

</p>

</div>
""",
unsafe_allow_html=True)

st.divider()
# ==========================================================
# FINAL BIOMARKER PANEL
# ==========================================================

st.markdown("## 🧬 Final Diagnostic Signature")

st.info("""
SHAP analysis reduced the original transcriptomic feature space to a compact
eight-gene diagnostic signature while preserving excellent predictive
performance.
""")

genes = pd.DataFrame({

    "Final Biomarkers":[

        "IFI27",
        "ZBP1",
        "SCRN1",
        "ABCB1",
        "CDCA7",
        "GADD45A",
        "TFDP1",
        "KLHDC8B"

    ]

})

st.table(genes)

st.divider()
# ==========================================================
# FINAL MODEL PERFORMANCE
# ==========================================================

st.markdown("## 📈 Final Eight-Gene Model")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("Accuracy","95.5%")

with c2:
    st.metric("ROC-AUC","0.983")

with c3:
    st.metric("Cross Validation","5-Fold")

with c4:
    st.metric("Threshold","0.90")
st.markdown("### Cross-Validation")

cv = pd.DataFrame({

    "Metric":[
        "Mean ROC-AUC",
        "Mean Accuracy"
    ],

    "Value":[
        "0.9833",
        "95.48%"
    ]

})

st.table(cv)

st.success("""
The final eight-gene Logistic Regression model demonstrated excellent
generalization across five stratified cross-validation folds, confirming the
robustness and reproducibility of the identified biomarker panel.
""")

st.divider()
# ==========================================================
# EXTERNAL VALIDATION
# ==========================================================

st.markdown("## 🌍 External Validation")

st.markdown("""
The final model was independently validated using the external transcriptomic
dataset GSE61635 comprising 129 samples without any model retraining.
""")

external = pd.DataFrame({

    "Metric":[
        "Dataset",
        "Samples",
        "Accuracy",
        "ROC-AUC",
        "Specificity",
        "Sensitivity"
    ],

    "Value":[
        "GSE61635",
        "129",
        "84.5%",
        "0.937",
        "100%",
        "79.8%"
    ]

})

st.table(external)

st.divider()
# ==========================================================
# CLINICAL INTERPRETATION
# ==========================================================

st.markdown("## 💡 Clinical Interpretation")

st.markdown("""
<div style="
background:#fffdf4;
border-left:6px solid #f59e0b;
padding:25px;
border-radius:16px;
">

<p style="
font-size:17px;
line-height:1.8;
text-align:justify;
">

The explainable AI pipeline successfully identified a compact eight-gene
transcriptomic signature capable of accurately distinguishing patients with
systemic lupus erythematosus from healthy controls. The combination of SHAP-
based feature selection, Logistic Regression modelling and independent external
validation supports the biological relevance, robustness and potential clinical
utility of the proposed diagnostic framework.

</p>

</div>
""",
unsafe_allow_html=True)
