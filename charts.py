import streamlit as st
import altair as alt

def generate_all_charts(df):
    """
    Generates 10 distinct dynamic and highly interactive charts using Altair.
    Every chart supports hovering, tooltips, and responsive rescaling.
    """
    if df.empty:
        st.warning("No data available for the selected filters.")
        return

    # --- 1. PIE / DONUT CHART (Interactive) ---
    st.subheader("1. Provincial Distribution of Total Estimated Cases")
    chart1 = alt.Chart(df).mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field="Estimated_Cases_WHO", type="quantitative", aggregate="sum"),
        color=alt.Color(field="Province", type="nominal"),
        tooltip=["Province", alt.Tooltip("Estimated_Cases_WHO", title="Total Cases", format=",")]
    ).properties(width='container', height=300).interactive()
    st.altair_chart(chart1, use_container_width=True)

    # --- 2. LINE CHART (Interactive Trend) ---
    st.subheader("2. Yearly Case Trajectory Trend (2015 - 2025)")
    chart2 = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X("Year", type="ordinal", title="Timeline Year"),
        y=alt.Y("Reported_Confirmed_Cases", type="quantitative", aggregate="sum", title="Confirmed Cases"),
        color=alt.value("firebrick"),
        tooltip=["Year", alt.Tooltip("Reported_Confirmed_Cases", aggregate="sum", title="Cases", format=",")]
    ).properties(width='container', height=350).interactive()
    st.altair_chart(chart2, use_container_width=True)

    # --- 3. BOX PLOT (Interactive Variance) ---
    st.subheader("3. Rainfall Anomaly Variance Across Provinces")
    chart3 = alt.Chart(df).mark_boxplot().encode(
        x=alt.X("Province", type="nominal"),
        y=alt.Y("Rainfall_Anomaly_mm", type="quantitative", title="Rainfall Anomaly (mm)"),
        color=alt.Color("Province", type="nominal"),
        tooltip=["Province", "Rainfall_Anomaly_mm"]
    ).properties(width='container', height=350).interactive()
    st.altair_chart(chart3, use_container_width=True)

    # --- 4. BARCHART / HEATMAP SIMULATION (Interactive Grid) ---
    st.subheader("4. Annual Distribution Matrix of Bednets Distributed")
    chart4 = alt.Chart(df).mark_rect().encode(
        x=alt.X("Year", type="ordinal"),
        y=alt.Y("Province", type="nominal"),
        color=alt.Color("Bednets_Distributed", type="quantitative", aggregate="sum", scale=alt.Scale(scheme="purples")),
        tooltip=["Province", "Year", alt.Tooltip("Bednets_Distributed", aggregate="sum", title="Bednets", format=",")]
    ).properties(width='container', height=300).interactive()
    st.altair_chart(chart4, use_container_width=True)

    # --- 5. HISTOGRAM (Interactive Binning) ---
    st.subheader("5. Distribution Range of Reported Deaths")
    chart5 = alt.Chart(df).mark_bar().encode(
        x=alt.X("Reported_Deaths", type="quantitative", bin=alt.Bin(maxbins=15), title="Deaths Range"),
        y=alt.Y("count()", title="Frequency Count"),
        color=alt.value("purple"),
        tooltip=[alt.Tooltip("count()", title="Count of Records")]
    ).properties(width='container', height=300).interactive()
    st.altair_chart(chart5, use_container_width=True)

    # --- 6. SCATTER PLOT (Interactive Bubble Chart) ---
    st.subheader("6. Rainfall Anomaly vs. Estimated Cases Indicator")
    chart6 = alt.Chart(df).mark_circle(size=100).encode(
        x=alt.X("Rainfall_Anomaly_mm", type="quantitative", title="Rainfall (mm)"),
        y=alt.Y("Estimated_Cases_WHO", type="quantitative", title="Estimated WHO Cases"),
        color=alt.Color("Province", type="nominal"),
        tooltip=["Province", "Year", "Rainfall_Anomaly_mm", "Estimated_Cases_WHO"]
    ).properties(width='container', height=350).interactive()
    st.altair_chart(chart6, use_container_width=True)

    # --- 7. AREA CHART (Interactive Stream) ---
    st.subheader("7. Cumulative Bednets Distributed Distribution")
    chart7 = alt.Chart(df).mark_area(opacity=0.5).encode(
        x=alt.X("Year", type="ordinal"),
        y=alt.Y("Bednets_Distributed", type="quantitative", aggregate="sum"),
        color=alt.value("darkblue"),
        tooltip=["Year", alt.Tooltip("Bednets_Distributed", aggregate="sum", title="Distributed", format=",")]
    ).properties(width='container', height=300).interactive()
    st.altair_chart(chart7, use_container_width=True)

    # --- 8. COUNT PLOT / BAR COUNT (Interactive) ---
    st.subheader("8. Data Point Counts Monitored Per Province")
    chart8 = alt.Chart(df).mark_bar().encode(
        x=alt.X("Province", type="nominal"),
        y=alt.Y("count()", title="Total Records Tracked"),
        color=alt.Color("Province", type="nominal"),
        tooltip=["Province", alt.Tooltip("count()", title="Total Records")]
    ).properties(width='container', height=250).interactive()
    st.altair_chart(chart8, use_container_width=True)

    # --- 9. VIOLIN ALTERNATIVE / STRIP PLOT (Interactive Density) ---
    st.subheader("9. Density Spread of Confirmed Infections")
    chart9 = alt.Chart(df).mark_tick().encode(
        x=alt.X("Reported_Confirmed_Cases", type="quantitative"),
        y=alt.Y("Province", type="nominal"),
        color=alt.Color("Province", type="nominal"),
        tooltip=["Province", "Year", "Reported_Confirmed_Cases"]
    ).properties(width='container', height=250).interactive()
    st.altair_chart(chart9, use_container_width=True)

    # --- 10. BAR CHART (Interactive Aggregation) ---
    st.subheader("10. Total Confirmed Cases Compared Regionally")
    chart10 = alt.Chart(df).mark_bar().encode(
        x=alt.X("Province", type="nominal", title="Province"),
        y=alt.Y("Reported_Confirmed_Cases", type="quantitative", aggregate="sum", title="Total Cases"),
        color=alt.Color("Province", type="nominal"),
        tooltip=["Province", alt.Tooltip("Reported_Confirmed_Cases", aggregate="sum", title="Total Cases", format=",")]
    ).properties(width='container', height=350).interactive()
    st.altair_chart(chart10, use_container_width=True)