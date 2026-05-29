import plotly.express as px
import streamlit as st
import pandas as pd

def generate_all_charts(df):
    """
    Generates exactly 10 distinct interactive Plotly charts.
    100% Bracket-Free Code to prevent markdown parser issues.
    """
    if df.empty:
        st.warning("No data available for the selected filters.")
        return

    # 🚨 Force string type using safe.assign() method to prevent KeyError across all plots
    df = df.assign(Province=df.Province.astype(str))

    # 1. PIE CHART (Category distribution)
    st.subheader("1. Provincial Distribution of Estimated Cases")
    prov_cases = df.groupby("Province").agg(dict(Estimated_Cases_WHO="sum")).reset_index()
    prov_cases = prov_cases.assign(Province=prov_cases.Province.astype(str))
    fig1 = px.pie(
        prov_cases, 
        values="Estimated_Cases_WHO", 
        names="Province",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig1, use_container_width=True)

    # 2. HISTOGRAM (Frequency distribution)
    st.subheader("2. Frequency Distribution of Rainfall Anomaly (mm)")
    fig2 = px.histogram(
        df, 
        x="Rainfall_Anomaly_mm", 
        nbins=10,
        color_discrete_sequence=list(("skyblue",))
    )
    fig2.update_layout(bargap=0.1)
    st.plotly_chart(fig2, use_container_width=True)

    # 3. LINE CHART (Temporal Trend)
    st.subheader("3. Yearly Malaria Cases Trend (2015 - 2025)")
    yearly = df.groupby("Year").agg(dict(Reported_Confirmed_Cases="sum", Estimated_Cases_WHO="sum")).reset_index()
    fig3 = px.line(
        yearly, 
        x="Year", 
        y=list(("Reported_Confirmed_Cases", "Estimated_Cases_WHO")),
        markers=True,
        color_discrete_map=dict(Reported_Confirmed_Cases="navy", Estimated_Cases_WHO="red")
    )
    st.plotly_chart(fig3, use_container_width=True)

    # 4. BAR CHART (Comparison across categories)
    st.subheader("4. Total Reported Deaths by Province")
    prov_deaths = df.groupby("Province").agg(dict(Reported_Deaths="sum")).reset_index()
    prov_deaths = prov_deaths.assign(Province=prov_deaths.Province.astype(str))
    fig4 = px.bar(
        prov_deaths, 
        x="Province", 
        y="Reported_Deaths", 
        color="Province",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig4, use_container_width=True)

    # 5. SCATTER PLOT (Numerical Relationship)
    st.subheader("5. Rainfall Anomaly vs. Confirmed Cases")
    fig5 = px.scatter(
        df, 
        x="Rainfall_Anomaly_mm", 
        y="Reported_Confirmed_Cases", 
        color="Province",
        size="Reported_Deaths",
        hover_data=list(("Year", "Province"))
    )
    st.plotly_chart(fig5, use_container_width=True)

    # 6. BOX PLOT (Variance and outliers)
    st.subheader("6. Plasmodium Vivax Strain Spread by Province")
    fig6 = px.box(
        df, 
        x="Province", 
        y="Plasmodium_Vivax_Pct", 
        color="Province",
        color_discrete_sequence=px.colors.qualitative.Pastel1
    )
    st.plotly_chart(fig6, use_container_width=True)

    # 7. HEATMAP (Feature correlation)
    st.subheader("7. Correlation Matrix of Variables")
    corr_cols = list((
        "Reported_Confirmed_Cases", 
        "Estimated_Cases_WHO", 
        "Reported_Deaths", 
        "Estimated_Deaths_WHO", 
        "Rainfall_Anomaly_mm", 
        "Bednets_Distributed"
    ))
    corr_matrix = df.filter(items=corr_cols).corr()
    fig7 = px.imshow(
        corr_matrix, 
        text_auto=".2f", 
        color_continuous_scale="RdBu_r"
    )
    st.plotly_chart(fig7, use_container_width=True)

    # 8. AREA CHART (Cumulative trends over time)
    st.subheader("8. Cumulative Bednets Distributed Over Time")
    bednets_yearly = df.groupby("Year").agg(dict(Bednets_Distributed="sum")).reset_index()
    fig8 = px.area(
        bednets_yearly, 
        x="Year", 
        y="Bednets_Distributed",
        color_discrete_sequence=list(("#4682B4",))
    )
    st.plotly_chart(fig8, use_container_width=True)

    # 9. COUNT PLOT (Frequency count of records)
    st.subheader("9. Frequency of Tracked Records per Province")
    fig9 = px.histogram(
        df, 
        x="Province", 
        color="Province",
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    st.plotly_chart(fig9, use_container_width=True)

    # 10. VIOLIN PLOT (Probability density spread)
    st.subheader("10. Density and Probability Spread of Estimated Deaths")
    fig10 = px.violin(
        df, 
        x="Province", 
        y="Estimated_Deaths_WHO", 
        color="Province",
        box=True,
        points="all"
    )
    st.plotly_chart(fig10, use_container_width=True)
