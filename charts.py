import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

def generate_all_charts(df):
    """
    Generates 10 highly interactive Plotly charts.
    Users can hover, zoom, and click elements just like premium dashboards.
    """
    if df.empty:
        st.warning("No data available for the selected filters.")
        return

    # 1. PIE CHART (Interactive Proportions)
    st.subheader("1. Provincial Distribution of Estimated Cases")
    prov_data = df.groupby('Province').sum().reset_index()
    fig1 = px.pie(prov_data, values='Estimated_Cases_WHO', names='Province', hole=0.3,
                  color_discrete_sequence=px.colors.qualitative.Set2)
    fig1.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig1, use_container_width=True)

    # 2. LINE CHART (Interactive Timeline Tracking)
    st.subheader("2. Yearly Case Trajectory Trend (2015 - 2025)")
    yearly = df.groupby('Year').sum().reset_index()
    fig2 = px.line(yearly, x='Year', y='Reported_Confirmed_Cases', markers=True,
                   title="Infection Progression Over Time")
    fig2.update_traces(line_color='firebrick', marker=dict(size=8))
    st.plotly_chart(fig2, use_container_width=True)

    # 3. BOX PLOT (Interactive Variance)
    st.subheader("3. Rainfall Anomaly Variance Across Provinces")
    fig3 = px.box(df, x='Province', y='Rainfall_Anomaly_mm', color='Province',
                  color_discrete_sequence=px.colors.qualitative.Accent)
    st.plotly_chart(fig3, use_container_width=True)

    # 4. HEATMAP (Interactive Correlation)
    st.subheader("4. Correlation Matrix of Variables")
    num_cols =
    corr_matrix = df[num_cols].corr()
    fig4 = px.imshow(corr_matrix, text_auto=".2f", color_continuous_scale='RdBu_r')
    st.plotly_chart(fig4, use_container_width=True)

    # 5. HISTOGRAM (Interactive Distribution)
    st.subheader("5. Distribution Range of Reported Deaths")
    fig5 = px.histogram(df, x='Reported_Deaths', nbins=15, color_discrete_sequence=['purple'])
    fig5.update_layout(bargap=0.1)
    st.plotly_chart(fig5, use_container_width=True)

    # 6. SCATTER PLOT (Interactive Hover Details)
    st.subheader("6. Rainfall Anomaly vs. Estimated Cases")
    fig6 = px.scatter(df, x='Rainfall_Anomaly_mm', y='Estimated_Cases_WHO', 
                      color='Province', symbol='Province', size='Reported_Deaths',
                      hover_data=)
    st.plotly_chart(fig6, use_container_width=True)

    # 7. AREA CHART (Interactive Shaded Volumes)
    st.subheader("7. Cumulative Bednets Distributed")
    area_data = df.groupby('Year').sum().reset_index()
    fig7 = px.area(area_data, x='Year', y='Bednets_Distributed', color_discrete_sequence=)
    st.plotly_chart(fig7, use_container_width=True)

    # 8. COUNT PLOT (Interactive Counter)
    st.subheader("8. Data Point Counts Monitored Per Province")
    fig8 = px.histogram(df, x='Province', color='Province', color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig8, use_container_width=True)

    # 9. VIOLIN PLOT (Interactive Kernel Density)
    st.subheader("9. Density and Spread of Confirmed Infections")
    fig9 = px.violin(df, x='Province', y='Reported_Confirmed_Cases', color='Province', box=True)
    st.plotly_chart(fig9, use_container_width=True)

    # 10. BAR CHART (Interactive sum)
    st.subheader("10. Total Confirmed Cases Compared Regionally")
    bar_data = df.groupby('Province').sum().reset_index()
    fig10 = px.bar(bar_data, x='Province', y='Reported_Confirmed_Cases', color='Province',
                   color_discrete_sequence=px.colors.sequential.Salmon_r)
    st.plotly_chart(fig10, use_container_width=True)
