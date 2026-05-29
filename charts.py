import plotly.graph_objects as go
import streamlit as st
import pandas as pd

def generate_all_charts(df):
    """
    Generates exactly 10 distinct interactive Plotly charts.
    Uses plotly.graph_objects to bypass Pandas 3.0 get_group incompatibility bug.
    """
    if df.empty:
        st.warning("No data available for the selected filters.")
        return

    # Force plain string conversion on Province to prevent group errors
    df = df.assign(Province=df.Province.astype(str))

    # --- 1. PIE CHART ---
    st.subheader("1. Provincial Distribution of Estimated Cases")
    prov_cases = df.groupby("Province").agg(dict(Estimated_Cases_WHO="sum")).reset_index()
    fig1 = go.Figure(data=go.Pie(
        labels=prov_cases.Province,
        values=prov_cases.Estimated_Cases_WHO,
        hole=0.3
    ))
    fig1.update_layout(margin=dict(t=30, b=10, l=10, r=10))
    st.plotly_chart(fig1, use_container_width=True)

    # --- 2. HISTOGRAM ---
    st.subheader("2. Frequency Distribution of Rainfall Anomaly (mm)")
    fig2 = go.Figure(data=go.Histogram(
        x=df.Rainfall_Anomaly_mm,
        marker_color="skyblue"
    ))
    fig2.update_layout(bargap=0.1, margin=dict(t=30, b=10, l=10, r=10))
    st.plotly_chart(fig2, use_container_width=True)

    # --- 3. LINE CHART ---
    st.subheader("3. Yearly Malaria Cases Trend (2015 - 2025)")
    yearly = df.groupby("Year").agg(dict(Reported_Confirmed_Cases="sum", Estimated_Cases_WHO="sum")).reset_index()
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(
        x=yearly.Year, 
        y=yearly.Estimated_Cases_WHO, 
        name='WHO Estimated', 
        mode='lines+markers',
        line=dict(color='red', width=2)
    ))
    fig3.add_trace(go.Scatter(
        x=yearly.Year, 
        y=yearly.Reported_Confirmed_Cases, 
        name='Reported Confirmed', 
        mode='lines+markers',
        line=dict(color='navy', width=2)
    ))
    fig3.update_layout(margin=dict(t=30, b=10, l=10, r=10))
    st.plotly_chart(fig3, use_container_width=True)

    # --- 4. BAR CHART ---
    st.subheader("4. Total Reported Deaths by Province")
    prov_deaths = df.groupby("Province").agg(dict(Reported_Deaths="sum")).reset_index()
    fig4 = go.Figure(data=go.Bar(
        x=prov_deaths.Province,
        y=prov_deaths.Reported_Deaths,
        marker_color="salmon"
    ))
    fig4.update_layout(margin=dict(t=30, b=10, l=10, r=10))
    st.plotly_chart(fig4, use_container_width=True)

    # --- 5. SCATTER PLOT ---
    st.subheader("5. Rainfall Anomaly vs. Confirmed Cases")
    fig5 = go.Figure()
    for prov in df.Province.unique():
        prov_df = df.query("Province == @prov")
        fig5.add_trace(go.Scatter(
            x=prov_df.Rainfall_Anomaly_mm,
            y=prov_df.Reported_Confirmed_Cases,
            mode='markers',
            name=str(prov),
            marker=dict(size=12)
        ))
    fig5.update_layout(xaxis_title="Rainfall Anomaly (mm)", yaxis_title="Confirmed Cases", margin=dict(t=30, b=10, l=10, r=10))
    st.plotly_chart(fig5, use_container_width=True)

    # --- 6. BOX PLOT ---
    st.subheader("6. Plasmodium Vivax Strain Spread by Province")
    fig6 = go.Figure()
    for prov in df.Province.unique():
        prov_df = df.query("Province == @prov")
        fig6.add_trace(go.Box(
            y=prov_df.Plasmodium_Vivax_Pct,
            name=str(prov)
        ))
    fig6.update_layout(yaxis_title="Vivax Percentage (%)", margin=dict(t=30, b=10, l=10, r=10))
    st.plotly_chart(fig6, use_container_width=True)

    # --- 7. HEATMAP ---
    st.subheader("7. Correlation Matrix of Variables")
    corr_cols = list(('Reported_Confirmed_Cases', 'Estimated_Cases_WHO', 'Reported_Deaths', 'Estimated_Deaths_WHO', 'Rainfall_Anomaly_mm', 'Bednets_Distributed'))
    corr_matrix = df.filter(items=corr_cols).corr()
    fig7 = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.index,
        colorscale="RdBu_r",
        zmin=-1, zmax=1
    ))
    fig7.update_layout(margin=dict(t=30, b=10, l=10, r=10))
    st.plotly_chart(fig7, use_container_width=True)

    # --- 8. AREA CHART ---
    st.subheader("8. Cumulative Bednets Distributed Over Time")
    bednets_yearly = df.groupby("Year").agg(dict(Bednets_Distributed="sum")).reset_index()
    fig8 = go.Figure(data=go.Scatter(
        x=bednets_yearly.Year,
        y=bednets_yearly.Bednets_Distributed,
        fill='tozeroy',
        line=dict(color='deepskyblue')
    ))
    fig8.update_layout(margin=dict(t=30, b=10, l=10, r=10))
    st.plotly_chart(fig8, use_container_width=True)

    # --- 9. COUNT PLOT ---
    st.subheader("9. Frequency of Tracked Records per Province")
    prov_counts = df.Province.value_counts().reset_index()
    prov_counts.columns = ('Province', 'Count')
    fig9 = go.Figure(data=go.Bar(
        x=prov_counts.Province,
        y=prov_counts.Count,
        marker_color="violet"
    ))
    fig9.update_layout(margin=dict(t=30, b=10, l=10, r=10))
    st.plotly_chart(fig9, use_container_width=True)

    # --- 10. VIOLIN PLOT ---
    st.subheader("10. Density and Probability Spread of Estimated Deaths")
    fig10 = go.Figure()
    for prov in df.Province.unique():
        prov_df = df.query("Province == @prov")
        fig10.add_trace(go.Violin(
            y=prov_df.Estimated_Deaths_WHO,
            name=str(prov),
            box_visible=True,
            meanline_visible=True
        ))
    fig10.update_layout(margin=dict(t=30, b=10, l=10, r=10))
    st.plotly_chart(fig10, use_container_width=True)
