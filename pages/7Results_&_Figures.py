import streamlit as st

st.set_page_config(
    page_title="Results & Figures",
    layout="wide"
)

st.title("📊 Results & Figures")

st.markdown("""
This page presents the key figures generated during model development,
validation and biological interpretation. Interactive visualizations are
organized into categories corresponding to the Results section of the
accompanying manuscript.
""")


st.divider()

section = st.radio(

    "Select Figure Category",

    [

        "🩺 Diagnosis",

        "📈 Disease Activity",

        "🧬 Biomarker Discovery",

        "🌐 Biological Validation",
        
        "🌍 External Validation",

        "🤖 Model Development",

        

    ],

    horizontal=True

)

st.divider()
if section == "🩺 Diagnosis":

    st.header("🩺 Diagnosis Results")

    st.markdown("""
This section summarizes the diagnostic performance of the final eight-gene
Logistic Regression classifier.
""")

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.metric("Accuracy","95.5%")
    c2.metric("ROC-AUC","0.983")
    c3.metric("Precision","97.3%")
    c4.metric("Recall","96.8%")
    c5.metric("F1 Score","97.0%")

    st.divider()

    left,right = st.columns(2)

    with left:

        st.image(
            "assets/roc_curve.png",
            caption="ROC Curve",
            use_container_width=True
        )

    with right:

        st.image(
            "assets/confusion_matrix.png",
            caption="Confusion Matrix",
            use_container_width=True
        )

    st.info("""
The ROC curve demonstrates excellent diagnostic discrimination, while the
confusion matrix confirms accurate classification of SLE and healthy samples.
""")

    st.divider()

    left,right = st.columns(2)

    with left:

        st.image(
            "assets/calibration_curve.png",
            caption="Calibration Curve",
            use_container_width=True
        )

    with right:

        st.metric("Brier Score","0.0112")

        st.markdown("""
A low Brier Score indicates excellent calibration between predicted
probabilities and observed outcomes.
""")
elif section == "🧬 Biomarker Discovery":

    st.header("🧬 Biomarker Discovery")

    left,right = st.columns(2)

    with left:

        st.image(
            "assets/shap_summary.png",
            caption="SHAP Summary Plot",
            use_container_width=True
        )

    with right:

        st.image(
            "assets/shap_bar.png",
            caption="Final Eight-Gene Signature",
            use_container_width=True
        )
        
elif section == "📈 Disease Activity":

    st.header("📈 Disease Activity Prediction")

    st.markdown("""
The disease activity model was trained independently using the top 20
severity-associated genes. Unlike disease diagnosis, disease activity
prediction is considerably more challenging because SLE severity is
influenced by multiple biological, clinical and environmental factors
beyond transcriptomic biomarkers alone.
""")

    st.metric("Best ROC-AUC", "0.686")

    st.divider()

    left, right = st.columns(2)

    with left:

        st.image(
            "assets/severity_roc.png",
            caption="ROC-AUC Comparison of Machine Learning Models",
            use_container_width=True
        )

    with right:

        st.image(
            "assets/top20_severity_genes.png",
            caption="Top 20 Severity-Associated Biomarkers",
            use_container_width=True
        )

    st.info("""
Although the transcriptomic biomarkers successfully captured disease-related
signals, disease activity prediction remains substantially more complex than
disease diagnosis. Clinical manifestations of SLE are influenced by numerous
factors including treatment response, disease duration, organ involvement,
immune-cell heterogeneity and environmental triggers. Consequently, gene
expression alone cannot fully explain disease severity, resulting in a more
moderate predictive performance compared with the diagnostic classifier.
""")
elif section == "🌍 External Validation":

    st.header("🌍 External Validation")

    st.markdown("""
The final diagnostic model was validated on an independent external
transcriptomic cohort without retraining to evaluate its robustness and
generalizability.
""")

    # ==========================================================
    # VALIDATION SUMMARY
    # ==========================================================

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Dataset", "GSE61635")

    with c2:
        st.metric("Samples", "129")

    with c3:
        st.metric("ROC-AUC", "0.937")

    st.divider()

    # ==========================================================
    # EXTERNAL VALIDATION FIGURES
    # ==========================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.image(
            "assets/external_validation_roc.png",
            caption="External ROC Curve",
            use_container_width=True
        )

    with col2:

        st.image(
            "assets/external_confusion_matrix.png",
            caption="External Confusion Matrix",
            use_container_width=True
        )

    with col3:

        st.image(
            "assets/external_calibration_curve.png",
            caption="External Calibration Curve",
            use_container_width=True
        )

    st.divider()

    # ==========================================================
    # INTERPRETATION
    # ==========================================================

    st.success("""
The final eight-gene diagnostic model demonstrated strong performance on the
independent GSE61635 validation cohort without retraining. The external ROC
curve confirmed excellent discriminative ability, the confusion matrix showed
accurate classification of SLE and healthy samples, and the calibration curve
demonstrated good agreement between predicted probabilities and observed
outcomes. Collectively, these findings support the robustness,
generalizability and clinical applicability of the proposed transcriptomic
diagnostic framework.
""")
    

elif section == "🌐 Biological Validation":

    st.header("🌐 Biological Validation")

    st.markdown("""
Functional enrichment and interaction network analyses were performed to
investigate the biological relevance of the identified biomarkers.
""")

    left,right = st.columns(2)

    with left:

        st.image(
            "assets/Overlap_KEGG_Barplot.png",
            caption="KEGG Pathway Enrichment",
            use_container_width=True
        )

    with right:

        st.image(
            "assets/enrichr_results.png",
            caption="Enrichr Pathway Enrichment",
            use_container_width=True
        )

elif section == "🤖 Model Development":

    st.header("🤖 Model Development Workflow")

    st.markdown("""
The complete machine learning workflow illustrates the analytical pipeline
used for biomarker discovery, feature selection, model development and
independent validation.
""")

    st.image(
        "assets/workflow(2).png",
        caption="Overall Study Workflow",
        use_container_width=True
    )

    st.divider()

    st.subheader("Model Comparison")

    st.image(
        "assets/model_comparison.png",
        caption="Comparison of Machine Learning Algorithms",
        use_container_width=True
    )

    st.info("""
Multiple supervised learning algorithms were evaluated during model
development. Logistic Regression consistently demonstrated the highest
combination of discrimination performance, calibration and interpretability,
leading to its selection as the final diagnostic classifier.
""")

    st.divider()

    st.subheader("SHAP-Based Feature Selection")

    left, right = st.columns(2)

    with left:

        st.image(
            "assets/shap_summary.png",
            caption="SHAP Summary Plot",
            use_container_width=True
        )

    with right:

        st.image(
            "assets/shap_bar.png",
            caption="Final 8-gene signature",
            use_container_width=True
        )

    st.success("""
SHAP explainability reduced thousands of transcriptomic features to a compact
eight-gene diagnostic signature while maintaining excellent predictive
performance. These biomarkers formed the basis of the final Logistic
Regression classifier.
""")
