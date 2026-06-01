import streamlit as st
import os
from filters import load_and_clean_data, apply_dashboard_filters
from charts import generate_all_charts

# 1. Page Configuration
st.set_page_config(page_title="Pakistan Malaria Dashboard", layout="wide")

# Custom CSS aapki styling ke liye
st.markdown("""
    <style>
    .main-title {
        font-size: 34px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 2px;
    }
    .sub-header {
        font-size: 14px;
        color: #cccccc;
        font-weight: 400;
        margin-bottom: 20px;
    }
    .status-badge {
        color: #00e5ff; /* Sahi cyan color jo aapko chahiye tha */
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Aapka Actual Title (Malaria Dashboard)
st.markdown('<div class="main-title">🎛️ Exploratory Data Analysis — Malaria Dashboard (Pakistan)</div>', unsafe_allow_html=True)

# 3. Sub-header line jisme Deploy Status add kar diya hai
st.markdown(
    '<div class="sub-header">'
    'Developed for <strong>EDA Course Assignment</strong> | '
    'Instructor: <strong>Ali Hassan Sherazi</strong> | '
    'Deploy Status: <span class="status-badge">Verified Stable</span>'
    '</div>', 
    unsafe_allow_html=True
)

st.markdown("---")

# ==========================================
# YAHAAN SE AAPKA SAARA PURANA DATA LOGIC HAI
# ==========================================

# Resolve correct path to data
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "malaria_data.csv")

if not os.path.exists(DATA_PATH):
    st.error(f"Dataset file missing! Please place 'malaria_data.csv' inside a folder named 'data' at: {DATA_PATH}")
    st.stop()

raw_df = load_and_clean_data(DATA_PATH)

if raw_df.empty:
    st.error("🚨 Failed to load data. Please check if the CSV file content is formatted correctly.")
    st.stop()

# --- SIDEBAR CONFIGURATION ---
st.sidebar.header("🎯 Interactive Filtering Panel")

# Get unique list of provinces using dot notation
provinces = sorted(raw_df.Province.unique())
selected_provinces = st.sidebar.multiselect("Select Target Provinces:", provinces, default=provinces)

# Year boundaries using dot notation
min_year = int(raw_df.Year.min())
max_year = int(raw_df.Year.max())
year_range = st.sidebar.slider("Timeline Range (Years):", min_year, max_year, (min_year, max_year))

# Rainfall boundaries using dot notation
min_rain = float(raw_df.Rainfall_Anomaly_mm.min())
max_rain = float(raw_df.Rainfall_Anomaly_mm.max())
rainfall_range = st.sidebar.slider("Rainfall Anomaly Range (mm):", min_rain, max_rain, (min_rain, max_rain))

# Reset button
if st.sidebar.button("Reset / Clear Filters", use_container_width=True):
    st.rerun()

# Process Filter Masking
filtered_df = apply_dashboard_filters(raw_df, selected_provinces, year_range, rainfall_range)

# --- MAIN SCREEN INTERFACE ---
if not filtered_df.empty:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Confirmed Cases", value=f"{filtered_df.Reported_Confirmed_Cases.sum():,}")
    with col2:
        st.metric(label="Total Tracked Deaths", value=f"{filtered_df.Reported_Deaths.sum():,}")
    with col3:
        st.metric(label="Total Bednets Distributed", value=f"{filtered_df.Bednets_Distributed.sum():,}")
        
    st.markdown("---")
    
    # Render the 10 Plots (Plotly)
    generate_all_charts(filtered_df)
    
    # Interactive Scrollable Dataframe (Same as sample app!)
    st.markdown("---")
    st.subheader("📋 Interactive Data Table (Scroll, Sort & Search)")
    st.markdown("Aap is table ko apni marzi se scroll kar sakte hain, columns par click karke sort kar sakte hain, aur right-corner se CSV download kar sakte hain.")
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
    
else:
    st.error("No records match the current slider values. Adjust filters to load plots.")
