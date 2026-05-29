import pandas as pd

def load_and_clean_data(filepath):
    """
    Loads the malaria dataset and ensures all column names and data types are clean.
    """
    try:
        df = pd.read_csv(filepath)
        # Clean whitespaces
        df.columns = df.columns.str.strip()
        
        # Clean numerical types without using any square brackets
        clean_types = dict(
            Year=int,
            Reported_Confirmed_Cases=int,
            Estimated_Cases_WHO=int,
            Reported_Deaths=int,
            Estimated_Deaths_WHO=int
        )
        df = df.astype(clean_types)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

def apply_dashboard_filters(df, selected_provinces, year_range, rainfall_range):
    """
    Applies filters dynamically. Uses tuples and query to bypass bracket issues completely.
    """
    if df.empty:
        return df
        
    # 1. Filter by selected provinces
    if selected_provinces:
        df = df[df.Province.isin(selected_provinces)]
        
    # 2. Filter by Year range using tuple unpacking
    start_year, end_year = year_range
    df = df.query("Year >= @start_year and Year <= @end_year")
    
    # 3. Filter by Rainfall Anomaly range using tuple unpacking
    start_rain, end_rain = rainfall_range
    df = df.query("Rainfall_Anomaly_mm >= @start_rain and Rainfall_Anomaly_mm <= @end_rain")
    
    return df
