# app.py
import streamlit as st
import pandas as pd
import os
from filters import render_sidebar_filters
from charts import render_kpis, render_trends

st.set_page_config(page_title="WHO Malaria Analytics Platform", layout="wide")

# Check if dataset file exists
DATA_FILE = "malaria_132_countries_dataset.csv"

if not os.path.exists(DATA_FILE):
    st.error(f"❌ '{DATA_FILE}' nahi mili! Pehle `python generate_data.py` run karein taake dataset generate ho sake.")
    st.stop()

@st.cache_data
def get_data():
    return pd.read_csv(DATA_FILE)

df = get_data()

# Render side panel filters
selected_region, selected_country, selected_year = render_sidebar_filters(df)

# Filter Dataset based on Side Panel choices
filtered_df = df.copy()
if selected_region != "All Regions":
    filtered_df = filtered_df[filtered_df["Region"] == selected_region]
if selected_country != "All Countries":
    filtered_df = filtered_df[filtered_df["Country"] == selected_country]

# Year breakdown subset
df_year = filtered_df[filtered_df["Year"] == selected_year]

# UI Heading
st.title("🗺️ Global Malaria Interactive Analytics Panel")
st.markdown(f"Display Target scope: **{selected_region}** 👉 *{selected_country}* | Target Year: **{selected_year}**")
st.markdown("---")

# Render KPI blocks
render_kpis(df_year, total_all_countries=df["Country"].nunique())

st.markdown("---")

# Tab structure matching layout
tab_table, tab_charts = st.tabs(["📊 Matrix Data Table Viewer", "📈 Analytical Historical Trends"])

with tab_table:
    st.subheader(f"Data Matrix Breakdown for Year {selected_year}")
    st.dataframe(
        df_year[["Region", "Country", "Year", "Estimated Cases", "Estimated Deaths"]].reset_index(drop=True),
        use_container_width=True,
        height=450
    )

with tab_charts:
    st.subheader("Historical Trajectory Insights")
    render_trends(filtered_df)
