import streamlit as st
import pandas as pd
from filters import render_sidebar, apply_filters
import charts

st.set_page_config(page_title="Global Malaria GHO Analytical Hub", layout="wide")

st.title("🔬 Global Malaria GHO Analytical Insights Engine (2000 - 2026)")
st.markdown("---")

# Safe Data Loader Component
@st.cache_data
def load_data():
    try:
        data = pd.read_csv('data/global_malaria_data.csv')
        return data
    except FileNotFoundError:
        st.error("🚨 Critical Error: 'data/global_malaria_data.csv' missing! Please execute 'python generate_data.py' first.")
        st.stop()

df = load_data()

# Render Sidebar Layout and extract state attributes
region, country, years = render_sidebar(df)
processed_df = apply_filters(df, region, country, years)

# Sequential Navigation Interface
st.sidebar.markdown("### 🗺️ Dashboard Navigation (10 Points)")
page = st.sidebar.radio(
    "Go to Analytical Point:",
    [
        "1. Incidences Development Trend",
        "2. System Reporting Gaps",
        "3. Cross-Regional Mortality Proportions",
        "4. Interventions & Controls Mapping",
        "5. Climate Drivers (Precipitation)",
        "6. Parasite Strain Breakdown",
        "7. Healthcare Case Fatality Rates",
        "8. Decadal Projections to 2026",
        "9. Country Hotspot Rankings",
        "10. Feature Attribute Correlation Matrix"
    ]
)

# Route Navigation States to appropriate analytical views
if processed_df.empty:
    st.warning("⚠️ No records matched your filter selection combinations. Reset fields in the sidebar panel.")
else:
    if page.startswith("1."):
        charts.plot_reported_cases(processed_df)
    elif page.startswith("2."):
        charts.plot_estimated_vs_reported(processed_df)
    elif page.startswith("3."):
        charts.plot_mortality_distribution(processed_df)
    elif page.startswith("4."):
        charts.plot_intervention_impact(processed_df)
    elif page.startswith("5."):
        charts.plot_climatic_influence(processed_df)
    elif page.startswith("6."):
        charts.plot_parasite_shift(processed_df)
    elif page.startswith("7."):
        charts.plot_case_fatality(processed_df)
    elif page.startswith("8."):
        charts.plot_projections(processed_df)
    elif page.startswith("9."):
        charts.plot_top_countries(processed_df)
    elif page.startswith("10."):
        charts.plot_correlation_heatmap(processed_df)
