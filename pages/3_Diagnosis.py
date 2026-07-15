import streamlit as st
import numpy as np
import joblib

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Diagnosis",
    page_icon="🩺",
    layout="wide"
)

# ==========================================================
# LOAD MODEL
# ==========================================================

model = joblib.load("models/diagnosis_model_clean8.pkl")
threshold = joblib.load("models/threshold_clean8.pkl")
genes = joblib.load("models/final_clean_8_genes.pkl")



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
    max-width:1200px;
    padding-top:2rem;
    padding-bottom:2rem;
}

.page-title{
    font-size:44px;
    font-weight:700;
    color:#154C97;
    margin-bottom:6px;
}

.page-subtitle{
    color:#64748B;
    font-size:18px;
    margin-bottom:35px;
    line-height:1.8;
}

.section-title{
    font-size:28px;
    font-weight:700;
    color:#154C97;
    margin-top:25px;
    margin-bottom:18px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""
<div class="page-title">

🩺 Diagnosis

</div>

<div class="page-subtitle">

Predict the probability of <b>Systemic Lupus Erythematosus (SLE)</b>
using the eight-gene transcriptomic diagnostic signature developed in this study.

</div>
""", unsafe_allow_html=True)
# ==========================================================
# GENE EXPRESSION INPUT
# ==========================================================

st.markdown("""
<div class="section-title">

🧬 Gene Expression Input

</div>
""", unsafe_allow_html=True)

st.info(
    "Enter the normalized expression values for the eight diagnostic biomarkers."
)

col1, col2 = st.columns(2)

with col1:
    ifi27 = st.text_input("IFI27", placeholder="e.g. 2.145")
    scrn1 = st.text_input("SCRN1", placeholder="e.g. 0.823")
    cdca7 = st.text_input("CDCA7", placeholder="e.g. -1.247")
    tfdp1 = st.text_input("TFDP1", placeholder="e.g. 0.654")

with col2:
    zbp1 = st.text_input("ZBP1", placeholder="e.g. 1.982")
    abcb1 = st.text_input("ABCB1", placeholder="e.g. -0.512")
    gadd45a = st.text_input("GADD45A", placeholder="e.g. 0.341")
    klhdc8b = st.text_input("KLHDC8B", placeholder="e.g. -0.876")

st.markdown("<br>", unsafe_allow_html=True)

# Analyze Button
predict = st.button(
    "🧬 Analyze Sample",
    use_container_width=True,
    type="primary"
)

# ==========================================================
# PREDICTION
# ==========================================================

if predict:

    try:

        # Create input array
        input_data = np.array([[
            float(ifi27),
            float(zbp1),
            float(scrn1),
            float(abcb1),
            float(cdca7),
            float(gadd45a),
            float(tfdp1),
            float(klhdc8b)
        ]])

        # Model prediction
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        st.markdown("---")

        st.markdown("""
        <div class="section-title">
        🩺 Diagnostic Report
        </div>
        """, unsafe_allow_html=True)

        # =====================================================
        # Prediction Banner
        # =====================================================

        if prediction == 1:

            st.success(
                "### 🟢 Predicted Diagnosis: **Systemic Lupus Erythematosus (SLE)**"
            )

        else:

            st.info(
                "### 🔵 Predicted Diagnosis: **Healthy Control**"
            )

        # =====================================================
        # Summary Cards
        # =====================================================

        confidence = probability * 100

        if prediction == 0:
            confidence = (1 - probability) * 100

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Prediction Confidence",
                f"{confidence:.2f}%"
            )

        with col2:
            st.metric(
                "Decision Threshold",
                f"{threshold:.2f}"
            )

        with col3:
            st.metric(
                "Model",
                "Logistic Regression"
            )

        st.markdown("")

        # =====================================================
        # Clinical Interpretation
        # =====================================================

        st.markdown("### 📋 Interpretation")

        if prediction == 1:

            st.warning(
                f"""
The submitted transcriptomic profile has been classified as **Systemic Lupus Erythematosus (SLE)**.

The diagnostic model estimates a confidence of **{confidence:.2f}%** that this sample belongs to the SLE class.

This prediction was generated using the **8-gene transcriptomic biomarker panel** identified in this study:

**IFI27, ZBP1, SCRN1, ABCB1, CDCA7, GADD45A, TFDP1 and KLHDC8B.**

The result should be interpreted alongside clinical findings and laboratory investigations.
"""
            )

        else:

            st.success(
                f"""
The submitted transcriptomic profile has been classified as a **Healthy Control**.

The diagnostic model estimates a confidence of **{confidence:.2f}%** that this sample belongs to the healthy class.

No transcriptomic evidence supporting an SLE classification was identified by the model.

This result should be interpreted alongside clinical findings and laboratory investigations.
"""
            )

        # =====================================================
        # Disclaimer
        # =====================================================

        st.markdown("---")

        st.caption(
            """
**Research Use Only**

This diagnostic model was developed as part of the transcriptomic biomarker discovery framework presented in this study.
The application is intended solely for research and educational purposes and must not be used as a standalone clinical diagnostic system.
"""
        )

    except ValueError:

        st.error("⚠️ Please enter valid numeric values for all eight biomarkers.")

    except Exception as e:

        st.exception(e)
        


