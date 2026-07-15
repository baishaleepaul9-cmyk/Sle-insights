import streamlit as st

st.set_page_config(
    page_title="SLE-Insight",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------------------------------------
# CSS
# ----------------------------------------------------

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

.block-container{
    max-width:1100px;
    padding-top:3rem;
    padding-bottom:2rem;
}

.stApp{
    background:#F7F9FC;
}

/* Hero */

.hero{

background:white;

padding:45px;

border-radius:20px;

text-align:center;

box-shadow:0 10px 30px rgba(0,0,0,.08);

border-top:6px solid #1565C0;

}

.hero h1{

font-size:48px;

font-weight:700;

color:#0D47A1;

margin-bottom:10px;

}

.hero h2{

font-size:24px;

font-weight:500;

color:#374151;

margin-bottom:20px;

}

.hero p{

font-size:18px;

line-height:1.8;

color:#6B7280;

max-width:750px;

margin:auto;

}

/* Button */

div.stButton > button{

width:100%;

height:58px;

border-radius:12px;

font-size:18px;

font-weight:600;

}

/* Footer */

.footer{

margin-top:45px;

text-align:center;

font-size:15px;

color:#6B7280;

}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# HERO
# ----------------------------------------------------

st.markdown("""

<div class="hero">

<h1>🧬 SLE-Insight</h1>

<h2>Transcriptomic Biomarker Discovery Platform</h2>

<p>

Machine Learning-Based Diagnostic Framework for
<strong>Systemic Lupus Erythematosus (SLE)</strong>

<br><br>

Explore transcriptomic biomarkers, diagnostic models,
and biological insights through an interactive companion platform
developed alongside our research.

</p>

</div>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ----------------------------------------------------
# BUTTON
# ----------------------------------------------------

left, center, right = st.columns([2.5,2,2.5])

with center:

    if st.button("🧬 Explore Platform", use_container_width=True):
        st.switch_page("pages/1_Home.py")

# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------

st.markdown("""

<div class="footer">

Designed as an interactive companion platform for transcriptomic
biomarker exploration and machine learning-based SLE diagnosis.

</div>

""", unsafe_allow_html=True)



    















