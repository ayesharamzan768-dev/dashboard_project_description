import streamlit as st

# 1. Page Configuration (Dashboard ko wide mode aur dark theme dene ke liye)
st.set_page_config(
    page_title="Reddit Insights: Depression in Indian Society",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS takay font colors aur spacing bilkul image jaisi dikhe
st.markdown("""
    <style>
    .main-title {
        font-size: 36px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 5px;
    }
    .sub-header {
        font-size: 14px;
        color: #cccccc;
        font-weight: 500;
        margin-bottom: 30px;
    }
    .status-badge {
        color: #00d2c4; /* Cyan/Teal color bilkul dashboard metrics jaisa */
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Main Title (🏛️ Icon ke sath)
st.markdown('<div class="main-title">🏛️ Reddit Insights: Depression in Indian Society</div>', unsafe_allow_html=True)

# 3. Sub-header Line (Aapka manga hua Deploy Status yahan add kar diya hai)
st.markdown(
    '<div class="sub-header">'
    'Course Project Track: Exploratory Data Analysis | '
    'Instructor: Ali Hassan Sherazi | '
    'Deploy Status: <span class="status-badge">Verified Stable</span>'
    '</div>', 
    unsafe_allow_html=True
)

st.markdown("---") # Ek barriq line sections ko alag karne ke liye

# =========================================================================
# ISKE NEECHE AAPKA PURANA/BAKI CODE AAYEGA (Metrics, Tabs, Plots, etc.)
# =========================================================================

# Example ke liye niche columns ka sample de raha hoon jahan aapke metrics hain:
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric(label="Audited Corpus Scale", value="5,500")
with col2:
    st.metric(label="Mean Engagement Metric", value="1606.5")
# ... isi tarah aapka baqi saala code chalega
