import streamlit as st

def render_sidebar(df):
    # Verified User branding at the top of the sidebar panel
    st.sidebar.markdown(
        """
        <div style="background-color:#1e293b; padding:15px; border-radius:10px; margin-bottom:20px; text-align:center; border: 1px solid #334155;">
            <h2 style="color:#38bdf8; margin:0; font-size:20px; font-family:'Arial';">EDA Ali Hassan Sherazi</h2>
            <p style="color:#4ade80; margin:5px 0 0 0; font-weight:bold; font-size:14px;">
                <span style="background-color:#065f46; padding:3px 8px; border-radius:12px;">✔️ Verified Profile</span>
            </p>
        </div>
        """, 
        unsafe_style_html=True
    )
    
    st.sidebar.header("🎛️ Interactive Filters")
    
    # Region Filter
    regions = ["All"] + sorted(list(df['WHO_Region'].unique()))
    selected_region = st.sidebar.selectbox("Select WHO Region", regions)
    
    # Filter country basis selected region
    if selected_region != "All":
        filtered_countries = sorted(list(df[df['WHO_Region'] == selected_region]['Country'].unique()))
    else:
        filtered_countries = sorted(list(df['Country'].unique()))
        
    countries = ["All"] + filtered_countries
    selected_country = st.sidebar.selectbox("Select Country", countries)
    
    # Year Filter Range
    min_year, max_year = int(df['Year'].min()), int(df['Year'].max())
    selected_years = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))
    
    return selected_region, selected_country, selected_years

def apply_filters(df, region, country, years):
    filtered_df = df.copy()
    filtered_df = filtered_df[(filtered_df['Year'] >= years[0]) & (filtered_df['Year'] <= years[1])]
    
    if region != "All":
        filtered_df = filtered_df[filtered_df['WHO_Region'] == region]
    if country != "All":
        filtered_df = filtered_df[filtered_df['Country'] == country]
        
    return filtered_df
