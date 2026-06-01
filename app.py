import streamlit as st
import os
from filters import load_and_clean_data, apply_dashboard_filters
import charts

# Set page configuration with high-tech theme
st.set_page_config(page_title="Global Malaria Pathogen Intelligence", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #0d1117; color: #c9d1d9; }
    div[data-testid="stMetricValue"] { color: #ffffff!important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-weight: bold; font-size: 38px!important; }
    div[data-testid="stMetricLabel"] { color: #8b949e!important; font-size: 14px!important; }
</style>
""", unsafe_allow_html=True)

# 🚨 Title & Subtitle block matching your screenshot exactly with (Global)
st.title("📊 Exploratory Data Analysis — Malaria Dashboard (Global)")
st.markdown("Developed for **EDA Course Assignment** | Instructor: **Ali Hassan Sherazi** | Deploy Status: <span style='color:#00ffcc; font-weight:bold;'>Verified Stable</span>", unsafe_allow_html=True)
st.markdown("---")

# Resolve correct path to data
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "malaria_data.csv")
raw_df = load_and_clean_data(DATA_PATH)

if raw_df.empty:
    st.error("🚨 Failed to load data. Please check if the CSV file content is formatted correctly.")
    st.stop()

# --- SIDEBAR CONTROL PANEL ---
st.sidebar.markdown("<h3 style='color:#00ffcc;'>INTELLIGENCE CONSOLE</h3>", unsafe_allow_html=True)

# 1. Year range slider (2000-2026)
min_year = int(raw_df.Year.min())
max_year = int(raw_df.Year.max())
year_range = st.sidebar.slider("Timeline Boundaries:", min_year, max_year, (min_year, max_year))

# 2. WHO Regions multi-select
regions = sorted(raw_df.WHO_Region.unique().tolist())
selected_regions = st.sidebar.multiselect("WHO Regions Filter:", regions, default=regions)

# 3. Dynamic Countries multi-select (132 total countries resolved)
if selected_regions:
    filtered_countries_df = raw_df.query("WHO_Region in @selected_regions")
    available_countries = sorted(filtered_countries_df.Country.unique().tolist())
else:
    available_countries = sorted(raw_df.Country.unique().tolist())

# Default selection set empty for a clean slate
selected_countries = st.sidebar.multiselect("Select Target Countries:", available_countries, default=list())

# Reset / Clear implementation
if st.sidebar.button("Reset Matrix defaults", use_container_width=True):
    st.rerun()

st.sidebar.markdown("<br><div style='background-color:#1e2d24;color:#00ffcc;padding:10px;border-radius:5px;text-align:center;border:1px solid #00ffcc;font-weight:bold;'>🟢 Streamlit Cloud Safe</div>", unsafe_allow_html=True)

# Process Filter Masking
filtered_df = apply_dashboard_filters(raw_df, selected_regions, selected_countries, year_range)

# --- MAIN SCREEN METRIC PANELS (Exact 3 Columns Matching Your Image) ---
if not filtered_df.empty:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Total Confirmed Cases", value=f"{filtered_df.Reported_Confirmed_Cases.sum():,}")
        
    with col2:
        st.metric(label="Total Tracked Deaths", value=f"{filtered_df.Reported_Deaths.sum():,}")
        
    with col3:
        st.metric(label="Total Bednets Distributed", value=f"{filtered_df.Bednets_Distributed.sum():,}")
        
    st.markdown("---")
    
    # 🎯 HORIZONTAL TABS LAYOUT IMPLEMENTATION (Bypassing brackets completely)
    tab_options = list(tuple((
        "Phase I: Interactive Macro Insights (Plotly 1-4)",
        "Phase II-A: Core Interactive Architectures (Plotly 5-7)",
        "Phase II-B: Advanced Fluid Distributions (Plotly 8-10)",
        "📋 Complete Matrix Data Sheet"
    )))
    tab1, tab2, tab3, tab4 = st.tabs(tab_options)
    
    # ---- TAB 1: Phase I (Plots 1 to 4 in a Grid Layout) ----
    with tab1:
        row1_col1, row1_col2 = st.columns(2)
        with row1_col1:
            charts.plot_pie_chart(filtered_df)
        with row1_col2:
            charts.plot_histogram(filtered_df)
            
        st.markdown("---")
        
        row2_col1, row2_col2 = st.columns(2)
        with row2_col1:
            charts.plot_line_chart(filtered_df)
        with row2_col2:
            charts.plot_bar_chart(filtered_df)
            
    # ---- TAB 2: Phase II-A (Plots 5 to 7) ----
    with tab2:
        row3_col1, row3_col2 = st.columns(2)
        with row3_col1:
            charts.plot_scatter_plot(filtered_df)
        with row3_col2:
            charts.plot_box_plot(filtered_df)
            
        st.markdown("---")
        charts.plot_heatmap(filtered_df)
        
    # ---- TAB 3: Phase II-B (Plots 8 to 10 Side-by-Side) ----
    with tab3:
        row4_col1, row4_col2 = st.columns(2)
        with row4_col1:
            charts.plot_area_chart(filtered_df)
        with row4_col2:
            charts.plot_count_plot(filtered_df)
            
        st.markdown("---")
        charts.plot_violin_plot(filtered_df)
        
    # ---- TAB 4: COMPLETE SHEET ----
    with tab4:
        st.subheader("📋 Active Global Spreadsheet Matrix")
        st.markdown("Aap is table ko apni marzi se scroll kar sakte hain, columns par click karke sort kar sakte hain, aur right-corner se CSV download kar sakte hain.")
        st.dataframe(filtered_df, use_container_width=True, height=500)
    
else:
    st.error("No records match the current slider values. Adjust filters to load plots.")
