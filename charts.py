import plotly.graph_objects as go
import streamlit as st
import pandas as pd
from itertools import islice

# 1. PIE CHART
def plot_pie_chart(df):
    st.subheader("1. Provincial Distribution of Estimated Cases")
    country_cases = df.groupby("Country").agg(dict(Estimated_Cases_WHO="sum")).reset_index()
    country_cases = country_cases.sort_values(by="Estimated_Cases_WHO", ascending=False).head(10)
    fig = go.Figure(data=list(tuple((go.Pie(
        labels=country_cases.Country,
        values=country_cases.Estimated_Cases_WHO,
        hole=0.3
    ),))))
    fig.update_layout(margin=dict(t=30, b=10, l=10, r=10), template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

# 2. HISTOGRAM
def plot_histogram(df):
    st.subheader("2. Frequency Distribution of Rainfall Anomaly")
    fig = go.Figure(data=list(tuple((go.Histogram(
        x=df.Rainfall_Anomaly_mm,
        marker_color="skyblue"
    ),))))
    fig.update_layout(bargap=0.1, margin=dict(t=30, b=10, l=10, r=10), template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

# 3. LINE CHART
def plot_line_chart(df):
    st.subheader("3. Yearly Malaria Cases Trend (2000 - 2026)")
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

# 4. BAR CHART
def plot_bar_chart(df):
    st.subheader("4. Total Reported Deaths by Region")
    prov_deaths = df.groupby("WHO_Region").agg(dict(Reported_Deaths="sum")).reset_index()
    fig = go.Figure(data=list(tuple((go.Bar(
        x=prov_deaths.WHO_Region,
        y=prov_deaths.Reported_Deaths,
        marker_color="salmon"
    ),))))
    fig.update_layout(margin=dict(t=30, b=10, l=10, r=10), template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

# 5. SCATTER PLOT
def plot_scatter_plot(df):
    st.subheader("5. Rainfall Anomaly vs. Confirmed Cases")
    fig = go.Figure()
    for country in list(islice(df.Country.unique(), 10)):
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

# 6. BOX PLOT
def plot_box_plot(df):
    st.subheader("6. Plasmodium Vivax Strain Spread")
    fig = go.Figure()
    for region in df.WHO_Region.unique():
        region_df = df.query("WHO_Region == @region")
        fig.add_trace(go.Box(
            y=region_df.Plasmodium_Vivax_Pct,
            name=str(region)
        ))
    fig.update_layout(yaxis_title="Vivax Percentage (%)", margin=dict(t=30, b=10, l=10, r=10), template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

# 7. HEATMAP
def plot_heatmap(df):
    st.subheader("7. Correlation Matrix of Variables")
    corr_cols = list(('Reported_Confirmed_Cases', 'Estimated_Cases_WHO', 'Reported_Deaths', 'Estimated_Deaths_WHO', 'Rainfall_Anomaly_mm', 'Bednets_Distributed'))
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

# 8. AREA CHART
def plot_area_chart(df):
    st.subheader("8. Cumulative Bednets Distributed Over Time")
    bednets_yearly = df.groupby("Year").agg(dict(Bednets_Distributed="sum")).reset_index()
    fig = go.Figure(data=list(tuple((go.Scatter(
        x=bednets_yearly.Year,
        y=bednets_yearly.Bednets_Distributed,
        fill='tozeroy',
        line=dict(color='deepskyblue')
    ),))))
    fig.update_layout(margin=dict(t=30, b=10, l=10, r=10), template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

# 9. COUNT PLOT
def plot_count_plot(df):
    st.subheader("9. Frequency of Tracked Records per Region")
    prov_counts = df.WHO_Region.value_counts().reset_index()
    prov_counts.columns = ('WHO_Region', 'Count')
    fig = go.Figure(data=list(tuple((go.Bar(
        x=prov_counts.WHO_Region,
        y=prov_counts.Count,
        marker_color="violet"
    ),))))
    fig.update_layout(margin=dict(t=30, b=10, l=10, r=10), template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

# 10. VIOLIN PLOT
def plot_violin_plot(df):
    st.subheader("10. Density and Probability Spread of Estimated Deaths")
    fig = go.Figure()
    for country in list(islice(df.Country.unique(), 4)):
        country_df = df.query("Country == @country")
        fig.add_trace(go.Violin(
            y=country_df.Estimated_Deaths_WHO,
            name=str(country),
            box_visible=True,
            meanline_visible=True
        ))
    fig.update_layout(margin=dict(t=30, b=10, l=10, r=10), template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
