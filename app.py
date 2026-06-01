import streamlit as st
import os
from filters import load_and_clean_data, apply_dashboard_filters
from charts import generate_all_charts
from itertools import islice

# Set high-tech dark page configuration
st.set_page_config(page_title="Global Malaria Pathogen Intelligence", layout="wide")

st.title("🛡️ Global Malaria & Pathogen Intelligence Portal")
st.markdown("A futuristic unified Command Center mapping chronological trends, intervention dynamics, and pathogenetic variance since 2000.")
st.markdown("---")

# Resolve correct path to data
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "malaria_data.csv")
raw_df = load_and_clean_data(DATA_PATH)

# --- SIDEBAR CONTROL PANEL ---
st.sidebar.markdown("<h3 style='color:#00ffcc;'>INTELLIGENCE CONSOLE</h3>", unsafe_allow_html=True)

# Point Selection Matrix Navigation (10 Distinct Required Points)
point_options = (
    "01 Executive Summary (Data & KPIs)",
    "02 Pie Chart: Regional Case Burden",
    "03 Histogram: Rainfall Anomaly Spread",
    "04 Line Chart: Temporal Trends",
    "05 Bar Chart: Comparative Deaths",
    "06 Scatter Plot: Climate-Intervention Link",
    "07 Box Plot: Parasite Strain Variance",
    "08 Heatmap: Correlation Matrix",
    "09 Area Chart: Intervention Scaling",
    "10 Count & Violin Plots: Data Density"
)
selected_point = st.sidebar.radio("Navigate Analytics Matrix:", point_options)

st.sidebar.markdown("<hr style='border:1px solid #1f242c;'>", unsafe_allow_html=True)

# 1. Year range slider (2000-2026)
min_year = int(raw_df.Year.min())
max_year = int(raw_df.Year.max())
year_range = st.sidebar.slider("Timeline Boundaries:", min_year, max_year, (min_year, max_year))

# 2. WHO Regions multi-select
regions = sorted(raw_df.WHO_Region.unique().tolist())
selected_regions = st.sidebar.multiselect("WHO Regions Filter:", regions, default=regions)

# 3. Dynamic Countries multi-select (125 total countries resolved)
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

# --- MAIN SCREEN METRIC PANELS ---
if not filtered_df.empty:
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
    
    with kpi_col1:
        st.metric(label="Total Nations", value=f"{filtered_df.Country.nunique()} / 125")
        
    with kpi_col2:
        total_cases_mil = filtered_df.Estimated_Cases_WHO.sum() / 1000000
        st.metric(label="WHO Estimated Cases", value=f"{total_cases_mil:.2f}M")
        
    with kpi_col3:
        total_deaths = filtered_df.Estimated_Deaths_WHO.sum()
        st.metric(label="Estimated Pathogen Mortality", value=f"{total_deaths:,}")
        
    with kpi_col4:
        total_nets_mil = filtered_df.Bednets_Distributed.sum() / 1000000
        st.metric(label="Bednets Distributed", value=f"{total_nets_mil:.2f}M")
        
    st.markdown("---")
    
    # Render Point Actions Based on Side Panel Selection
    if selected_point == "01 Executive Summary (Data & KPIs)":
        st.subheader("📋 Active Spreadsheet Matrix View")
        st.markdown("Aap is table ko apni marzi se scroll kar sakte hain, columns par click karke sort kar sakte hain, aur right-corner se CSV download kar sakte hain.")
        st.dataframe(filtered_df, use_container_width=True, height=500)
    else:
        # Dynamic visual execution block
        generate_all_charts(filtered_df, selected_point)
        
        st.markdown("---")
        st.subheader("📋 Segmented Data Table")
        st.dataframe(filtered_df, use_container_width=True, height=250)
    
else:
    st.error("No records match the current slider values. Adjust filters to load plots.")
