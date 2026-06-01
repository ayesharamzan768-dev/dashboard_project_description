# filters.py
import streamlit as st

def render_sidebar_filters(df):
    st.sidebar.header("🌍 Side Panel Controls")
    
    # Region Filter Dropdown
    region_options = ["All Regions"] + sorted(list(df["Region"].unique()))
    selected_region = st.sidebar.selectbox("Select WHO Region:", region_options)
    
    # Country Cascading logic based on region choice
    if selected_region == "All Regions":
        available_countries = sorted(list(df["Country"].unique()))
    else:
        available_countries = sorted(list(df[df["Region"] == selected_region]["Country"].unique()))
        
    country_options = ["All Countries"] + available_countries
    selected_country = st.sidebar.selectbox("Select Country:", country_options)
    
    # Year Selection Slider
    min_year, max_year = int(df["Year"].min()), int(df["Year"].max())
    selected_year = st.sidebar.slider("Select Timeline Year:", min_year, max_year, max_year)
    
    return selected_region, selected_country, selected_year
