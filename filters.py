import streamlit as st
import pandas as pd

def apply_filters(df):
    st.sidebar.header("🔍 Filters")
    
    # Clean column names just in case there are hidden spaces
    df.columns = df.columns.str.strip()
    
    # Convert categorical/object columns to clean string type to avoid unused categories error
    for col in df.columns:
        if isinstance(df[col].dtype, pd.CategoricalDtype) or df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.strip()

    # 1. Target Province Filter
    if 'Target Province' in df.columns:
        unique_provinces = sorted(df['Target Province'].dropna().unique())
        selected_provinces = st.sidebar.multiselect(
            "Select Target Province", 
            options=unique_provinces, 
            default=unique_provinces
        )
        if selected_provinces:
            df = df[df['Target Province'].isin(selected_provinces)]
    
    # 2. Year Filter
    if 'Year' in df.columns:
        # Fill NaN years or drop them for filter
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
        unique_years = sorted([int(x) for x in df['Year'].dropna().unique()])
        if unique_years:
            selected_years = st.sidebar.multiselect(
                "Select Year", 
                options=unique_years, 
                default=unique_years
            )
            if selected_years:
                df = df[df['Year'].isin(selected_years)]
            
    # 3. Development Partner Filter
    if 'Development Partner' in df.columns:
        unique_partners = sorted(df['Development Partner'].dropna().unique())
        selected_partners = st.sidebar.multiselect(
            "Select Development Partner", 
            options=unique_partners, 
            default=unique_partners
        )
        if selected_partners:
            df = df[df['Development Partner'].isin(selected_partners)]

    return df
