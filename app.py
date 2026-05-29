import streamlit as st
import os
from filters import load_and_clean_data, apply_dashboard_filters
from charts import generate_all_charts

st.set_page_config(page_title="Pakistan Malaria Dashboard", layout="wide")

st.title("🎛️ Exploratory Data Analysis — Malaria Dashboard (Pakistan)")
st.markdown("Developed for **EDA Course Assignment** | Instructor: **Ali Hassan Sherazi**")

# Resolve correct path to data
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "malaria_data.csv")

if not os.path.exists(DATA_PATH):
    st.error(f"Dataset file missing! Please place 'malaria_data.csv' inside a folder named 'data' at: {DATA_PATH}")
else:
    raw_df = load_and_clean_data(DATA_PATH)
    
    # --- SIDEBAR CONFIGURATION ---
    st.sidebar.header("🎯 Interactive Filtering Panel")
    
    provinces = sorted(raw_df['Province'].unique()) if not raw_df.empty else []
    selected_provinces = st.sidebar.multiselect("Select Target Provinces:", provinces, default=provinces)
    
    min_year, max_year = (int(raw_df['Year'].min()), int(raw_df['Year'].max())) if not raw_df.empty else (2015, 2025)
    year_range = st.sidebar.slider("Timeline Range (Years):", min_year, max_year, (min_year, max_year))
    
    min_rain, max_rain = (float(raw_df['Rainfall_Anomaly_mm'].min()), float(raw_df['Rainfall_Anomaly_mm'].max())) if not raw_df.empty else (-50.0, 150.0)
    rainfall_range = st.sidebar.slider("Rainfall Anomaly Range (mm):", min_rain, max_rain, (min_rain, max_rain))
    
    # Process Filter Masking
    filtered_df = apply_dashboard_filters(raw_df, selected_provinces, year_range, rainfall_range)
    
    # --- MAIN SCREEN INTERFACE ---
    if not filtered_df.empty:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Total Confirmed Cases", value=f"{filtered_df['Reported_Confirmed_Cases'].sum():,}")
        with col2:
            st.metric(label="Total Tracked Deaths", value=f"{filtered_df['Reported_Deaths'].sum():,}")
        with col3:
            st.metric(label="Total Bednets Distributed", value=f"{filtered_df['Bednets_Distributed'].sum():,}")
            
        st.markdown("---")
        
        # Render the 10 Plots
        generate_all_charts(filtered_df)
    else:
        st.error("No records match the current slider values. Adjust filters to load plots.")