import pandas as pd

def load_and_clean_data(filepath):
    """
    Loads the malaria dataset and ensures all column names and data types are clean.
    """
    try:
        df = pd.read_csv(filepath)
        # Strip any accidental whitespaces from column names
        df.columns = df.columns.str.strip()
        
        # Ensure numerical types are correct using dict-based astype (No square brackets)
        convert_dict = {
            'Year': int,
            'Reported_Confirmed_Cases': int,
            'Estimated_Cases_WHO': int,
            'Reported_Deaths': int,
            'Estimated_Deaths_WHO': int
        }
        df = df.astype(convert_dict)
        
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

def apply_dashboard_filters(df, selected_provinces, year_range, rainfall_range):
    """
    Applies the active dashboard sidebar selections to dynamically filter rows.
    Using.query() syntax to bypass square bracket stripping issues completely.
    """
    if df.empty:
        return df
        
    # 1. Category Filter (Multi-Select)
    if selected_provinces:
        df = df.query("Province in @selected_provinces")
        
    # 2. Numerical Range Filter (Year Slider)
    start_year, end_year = year_range
    df = df.query("Year >= @start_year and Year <= @end_year")
    
    # 3. Numerical Range Filter (Rainfall Slider)
    start_rain, end_rain = rainfall_range
    df = df.query("Rainfall_Anomaly_mm >= @start_rain and Rainfall_Anomaly_mm <= @end_rain")
    
    return df