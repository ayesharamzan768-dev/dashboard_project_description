# charts.py
import streamlit as st

def render_kpis(df_year, total_all_countries=132):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        current_countries = df_year["Country"].nunique()
        st.metric(label="Selected Countries Active", value=f"{current_countries} / {total_all_countries}")
    with col2:
        total_cases = df_year["Estimated Cases"].sum()
        st.metric(label="Total Cases Globally", value=f"{total_cases:,}")
    with col3:
        total_deaths = df_year["Estimated Deaths"].sum()
        st.metric(label="Total Mortality Deaths", value=f"{total_deaths:,}")

def render_trends(filtered_df):
    trend_df = filtered_df.groupby("Year")[["Estimated Cases", "Estimated Deaths"]].sum().reset_index()
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.markdown("**📉 Malaria Incident Trends Cases**")
        st.line_chart(data=trend_df, x="Year", y="Estimated Cases", color="#FF4B4B")
    with col_c2:
        st.markdown("**💀 Mortality Rate Trajectory Deaths**")
        st.line_chart(data=trend_df, x="Year", y="Estimated Deaths", color="#1F77B4")
