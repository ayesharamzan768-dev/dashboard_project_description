import plotly.graph_objects as go
import streamlit as st
import pandas as pd
from itertools import islice

def generate_all_charts(df, point_option):
    """
    Core plotting engine. Renders the requested interactive chart based on the Side Panel selection.
    """
    if df.empty:
        st.warning("No data available for the selected filters.")
        return

    df = df.assign(Country=df.Country.astype(str))
    df = df.assign(WHO_Region=df.WHO_Region.astype(str))

    # --- 1. PIE CHART ---
    if point_option == "02 Pie Chart: Regional Case Burden":
        st.subheader("Distribution of WHO Estimated Cases by Country")
        country_cases = df.groupby("Country").agg(dict(Estimated_Cases_WHO="sum")).reset_index()
        country_cases = country_cases.sort_values(by="Estimated_Cases_WHO", ascending=False).head(10)
        fig = go.Figure(data=list(tuple((go.Pie(
            labels=country_cases.Country,
            values=country_cases.Estimated_Cases_WHO,
            hole=0.3
        ),))))
        fig.update_layout(margin=dict(t=30, b=10, l=10, r=10), template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    # --- 2. HISTOGRAM ---
    elif point_option == "03 Histogram: Rainfall Anomaly Spread":
        st.subheader("Frequency Distribution of Precipitation Anomalies (mm)")
        fig = go.Figure(data=list(tuple((go.Histogram(
            x=df.Rainfall_Anomaly_mm,
            marker_color="skyblue"
        ),))))
        fig.update_layout(bargap=0.1, margin=dict(t=30, b=10, l=10, r=10), template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    # --- 3. LINE CHART ---
    elif point_option == "04 Line Chart: Temporal Trends":
        st.subheader("Yearly Malaria Cases Trend Line (2000 - 2026)")
        yearly = df.groupby("Year").agg(dict(Reported_Confirmed_Cases="sum", Estimated_Cases_WHO="sum")).reset_index()
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=yearly.Year, 
            y=yearly.Estimated_Cases_WHO, 
            name='WHO Estimated', 
            mode='lines+markers',
            line=dict(color='red', width=2)
        ))
        fig.add_trace(go.Scatter(
            x=yearly.Year, 
            y=yearly.Reported_Confirmed_Cases, 
            name='Reported Confirmed', 
            mode='lines+markers',
            line=dict(color='navy', width=2)
        ))
        fig.update_layout(margin=dict(t=30, b=10, l=10, r=10), template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    # --- 4. BAR CHART ---
    elif point_option == "05 Bar Chart: Comparative Deaths":
        st.subheader("Comparative Global Reported Deaths by Country")
        country_deaths = df.groupby("Country").agg(dict(Reported_Deaths="sum")).reset_index()
        country_deaths = country_deaths.sort_values(by="Reported_Deaths", ascending=False).head(10)
        fig = go.Figure(data=list(tuple((go.Bar(
            x=country_deaths.Country,
            y=country_deaths.Reported_Deaths,
            marker_color="salmon"
        ),))))
        fig.update_layout(margin=dict(t=30, b=10, l=10, r=10), template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    # --- 5. SCATTER PLOT ---
    elif point_option == "06 Scatter Plot: Climate-Intervention Link":
        st.subheader("Relationship of Rainfall Anomalies vs. Confirmed Cases")
        fig = go.Figure()
        for country in df.Country.unique():
            country_df = df.query("Country == @country")
            fig.add_trace(go.Scatter(
                x=country_df.Rainfall_Anomaly_mm,
                y=country_df.Reported_Confirmed_Cases,
                mode='markers',
                name=str(country),
                marker=dict(size=12)
            ))
        fig.update_layout(xaxis_title="Rainfall Anomaly (mm)", yaxis_title="Confirmed Cases", margin=dict(t=30, b=10, l=10, r=10), template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    # --- 6. BOX PLOT ---
    elif point_option == "07 Box Plot: Parasite Strain Variance":
        st.subheader("Distribution Spread of Plasmodium Vivax Parasite Strain")
        fig = go.Figure()
        for region in df.WHO_Region.unique():
            region_df = df.query("WHO_Region == @region")
            fig.add_trace(go.Box(
                y=region_df.Plasmodium_Vivax_Pct,
                name=str(region)
            ))
        fig.update_layout(yaxis_title="Vivax Proportion Percentage (%)", margin=dict(t=30, b=10, l=10, r=10), template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    # --- 7. HEATMAP ---
    elif point_option == "08 Heatmap: Correlation Matrix":
        st.subheader("Feature Correlation Grid Matrix Analysis")
        corr_cols = list(('Reported_Confirmed_Cases', 'Estimated_Cases_WHO', 'Reported_Deaths', 'Estimated_Deaths_WHO', 'Bednets_Distributed'))
        corr_matrix = df.filter(items=corr_cols).corr()
        fig = go.Figure(data=list(tuple((go.Heatmap(
            z=corr_matrix.values.tolist(),
            x=corr_matrix.columns.tolist(),
            y=corr_matrix.index.tolist(),
            colorscale="Viridis",
            zmin=-1, zmax=1
        ),))))
        fig.update_layout(margin=dict(t=30, b=10, l=10, r=10), template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    # --- 8. AREA CHART ---
    elif point_option == "09 Area Chart: Intervention Scaling":
        st.subheader("Cumulative Scale-up of Bednets Intervention Over Time")
        bednets_yearly = df.groupby("Year").agg(dict(Bednets_Distributed="sum")).reset_index()
        fig = go.Figure(data=list(tuple((go.Scatter(
            x=bednets_yearly.Year,
            y=bednets_yearly.Bednets_Distributed,
            fill='tozeroy',
            line=dict(color='deepskyblue')
        ),))))
        fig.update_layout(margin=dict(t=30, b=10, l=10, r=10), template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    # --- 9. COUNT & VIOLIN PLOTS ---
    elif point_option == "10 Count & Violin Plots: Data Density":
        st.subheader("Data Profiles Tracking Frequency & Density Spread")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Tracked Record Counts per Region**")
            prov_counts = df.WHO_Region.value_counts().reset_index()
            prov_counts.columns = ('WHO_Region', 'Count')
            fig_count = go.Figure(data=list(tuple((go.Bar(
                x=prov_counts.WHO_Region,
                y=prov_counts.Count,
                marker_color="violet"
            ),))))
            fig_count.update_layout(margin=dict(t=30, b=10, l=10, r=10), template="plotly_dark")
            st.plotly_chart(fig_count, use_container_width=True)
            
        with c2:
            st.markdown("**Probability Density Spread of Estimated Deaths**")
            fig_violin = go.Figure()
            for country in list(islice(df.Country.unique(), 4)):
                country_df = df.query("Country == @country")
                fig_violin.add_trace(go.Violin(
                    y=country_df.Estimated_Deaths_WHO,
                    name=str(country),
                    box_visible=True,
                    meanline_visible=True
                ))
            fig_violin.update_layout(margin=dict(t=30, b=10, l=10, r=10), template="plotly_dark")
            st.plotly_chart(fig_violin, use_container_width=True)