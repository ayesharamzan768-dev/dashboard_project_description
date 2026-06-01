import streamlit as st
import os
from filters import load_and_clean_data, apply_dashboard_filters
from charts import generate_all_charts

# Set high-tech dark page configuration
st.set_page_config(page_title="Global Malaria Pathogen Intelligence", layout="wide")

# Custom Glowing Dark CSS styles for visual parity
st.markdown("""
<style>
  .stApp { background-color: #0d1117; color: #c9d1d9; }
    div[data-testid="stMetricValue"] { color: #00ffcc!important; font-family: 'Courier New', monospace; font-weight: bold; }
    div[data-testid="stMetricLabel"] { color: #8b949e!important; }
    div { background-color: #090d12!important; border-right: 1px solid #1f242c; }
</style>
""", unsafe_allow_html=True)

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
        st.markdown(f"""
        <div style="background-color:#161b22; padding:20px; border-radius:10px; border:1px solid #1f242c; border-left: 5px solid #00ffcc; box-shadow: 0px 0px 15px rgba(0,255,204,0.15);">
            <h5 style="color:#8b949e; margin:0; font-size:12px; font-weight:bold;">TOTAL NATIONS</h5>
            <h2 style="color:#00ffcc; margin:10px 0 0 0; font-family:monospace; font-size:32px;">{filtered_df.Country.nunique()} / 125</h2>
            <p style="color:#58a6ff; margin:5px 0 0 0; font-size:11px;">★ Active Epidemic Centers</p>
        </div>
        """, unsafe_allow_html=True)
        
    with kpi_col2:
        total_cases_mil = filtered_df.Estimated_Cases_WHO.sum() / 1000000
        st.markdown(f"""
        <div style="background-color:#161b22; padding:20px; border-radius:10px; border:1px solid #1f242c; border-left: 5px solid #ff3366; box-shadow: 0px 0px 15px rgba(255,51,102,0.15);">
            <h5 style="color:#8b949e; margin:0; font-size:12px; font-weight:bold;">WHO ESTIMATED CASES</h5>
            <h2 style="color:#ff3366; margin:10px 0 0 0; font-family:monospace; font-size:32px;">{total_cases_mil:.2f}M</h2>
            <p style="color:#ff3366; margin:5px 0 0 0; font-size:11px;">▲ Chronological Velocity</p>
        </div>
        """, unsafe_allow_html=True)
        
    with kpi_col3:
        total_deaths = filtered_df.Estimated_Deaths_WHO.sum()
        st.markdown(f"""
        <div style="background-color:#161b22; padding:20px; border-radius:10px; border:1px solid #1f242c; border-left: 5px solid #ffcc00; box-shadow: 0px 0px 15px rgba(255,204,0,0.15);">
            <h5 style="color:#8b949e; margin:0; font-size:12px; font-weight:bold;">ESTIMATED PATHOGEN MORTALITY</h5>
            <h2 style="color:#ffcc00; margin:10px 0 0 0; font-family:monospace; font-size:32px;">{total_deaths:,}</h2>
            <p style="color:#ffcc00; margin:5px 0 0 0; font-size:11px;">▼ Mortality Rate Vector</p>
        </div>
        """, unsafe_allow_html=True)
        
    with kpi_col4:
        total_nets_mil = filtered_df.Bednets_Distributed.sum() / 1000000
        st.markdown(f"""
        <div style="background-color:#161b22; padding:20px; border-radius:10px; border:1px solid #1f242c; border-left: 5px solid #33ccff; box-shadow: 0px 0px 15px rgba(51,204,255,0.15);">
            <h5 style="color:#8b949e; margin:0; font-size:12px; font-weight:bold;">BEDNETS DISTRIBUTED</h5>
            <h2 style="color:#33ccff; margin:10px 0 0 0; font-family:monospace; font-size:32px;">{total_nets_mil:.2f}M</h2>
            <p style="color:#33ccff; margin:5px 0 0 0; font-size:11px;">✚ Target Protection Units</p>
        </div>
        """, unsafe_allow_html=True)
        
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
