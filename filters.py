import pandas as pd

def load_and_clean_data(filepath):
    """
    Loads the malaria dataset and ensures all column names and data types are clean.
    """
    try:
        df = pd.read_csv(filepath)
        df.columns = df.columns.str.strip()
        
        # Ensure numerical types are correct
        df['Year'] = df['Year'].astype(int)
        df['Reported_Confirmed_Cases'] = df['Reported_Confirmed_Cases'].astype(int)
        df['Estimated_Cases_WHO'] = df['Estimated_Cases_WHO'].astype(int)
        df['Reported_Deaths'] = df['Reported_Deaths'].astype(int)
        df['Estimated_Deaths_WHO'] = df['Estimated_Deaths_WHO'].astype(int)
        
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

def apply_dashboard_filters(df, selected_provinces, year_range, rainfall_range):
    """
    Applies the active dashboard sidebar selections to dynamically filter rows.
    """
    if df.empty:
        return df
        
    if selected_provinces:
        df = df[df['Province'].isin(selected_provinces)]
        
    # Corrected Syntax without unmatched brackets
    df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
    df = df[(df['Rainfall_Anomaly_mm'] >= rainfall_range[0]) & (df['Rainfall_Anomaly_mm'] <= rainfall_range[1])]
    
    return df