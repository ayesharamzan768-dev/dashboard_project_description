import pandas as pd

def load_and_clean_data(filepath):
    """
    Loads the malaria dataset and ensures all column names and data types are clean.
    """
    try:
        df = pd.read_csv(filepath)
        df.columns = df.columns.str.strip()
        
        # Safe numeric conversions
        df = df.astype(int)
        df = df.astype(int)
        df = df.astype(int)
        df = df.astype(int)
        df = df.astype(int)
        
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

def apply_dashboard_filters(df, selected_provinces, year_range, rainfall_range):
    """
    Applies filters dynamically. Bypasses syntax issues completely.
    """
    if df.empty:
        return df
        
    # 1. Category Filter (Province)
    if selected_provinces:
        df = df[df['Province'].isin(selected_provinces)]
        
    # 2. Timeline Filter
    start_yr, end_yr = year_range
    df = df.query("Year >= @start_yr and Year <= @end_yr")
    
    # 3. Environmental Filter
    start_rf, end_rf = rainfall_range
    df = df.query("Rainfall_Anomaly_mm >= @start_rf and Rainfall_Anomaly_mm <= @end_rf")
    
    return df
