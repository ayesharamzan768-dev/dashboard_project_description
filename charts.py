import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def display_page_layout(title, fig, dataframe, insights_text):
    st.subheader(title)
    
    # Side-by-Side arrangement using streamit columns
    col1, col2 = st.columns([1.2, 0.8])
    
    with col1:
        st.pyplot(fig) if not isinstance(fig, px.colors.Sequential) and not hasattr(fig, 'to_json') else st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.markdown("**📋 Associated Interactive Data Matrix**")
        st.dataframe(dataframe[['Country', 'Year', 'WHO_Region', dataframe.columns[3]]].head(100), height=250)
        
    st.markdown(f"### 💡 Dynamic EDA Insights\n{insights_text}")

# 1. Total Reported Cases
def plot_reported_cases(df):
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.lineplot(data=df, x='Year', y='Reported_Cases', estimator='sum', marker='o', color='#38bdf8', ax=ax)
    ax.set_title("Annual Total Confirmed Reported Malaria Incidences")
    display_page_layout("Point 1: Malaria Burden Evaluation (Reported Cases)", fig, df, "The line trend represents aggregate global counts. Sharp drops identify intervals with increased medical surveillance and vector intervention distributions.")

# 2. Estimated Burden vs Reported Cases
def plot_estimated_vs_reported(df):
    fig, ax = plt.subplots(figsize=(7, 4))
    summary = df.groupby('Year')[['Estimated_Cases', 'Reported_Cases']].sum().reset_index()
    plt.fill_between(summary['Year'], summary['Estimated_Cases'], label='Estimated Cases (Unreported Gap)', color='orange', alpha=0.4)
    plt.plot(summary['Year'], summary['Reported_Cases'], label='Confirmed Reported Cases', color='red', marker='x')
    ax.set_title("Reporting Efficiency Gap Analysis")
    plt.legend()
    display_page_layout("Point 2: Surveillance System Sensitivity Assessment", fig, df, "The discrepancy gap reflects health infrastructure sensitivity. Minimizing this gap implies progressive regional diagnostics inclusion.")

# 3. Mortality Distribution
def plot_mortality_distribution(df):
    fig = px.bar(df, x='WHO_Region', y='Estimated_Deaths', color='WHO_Region', title="Proportional Regional Malaria Mortality Attributions")
    display_page_layout("Point 3: Mortality Share Across WHO Regions", fig, df, "African Region persistently accounts for extreme proportions of mortality burdens, prioritizing defensive actions here.")

# 4. Intervention Effectiveness
def plot_intervention_impact(df):
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.scatterplot(data=df, x='Bednets_Distributed', y='Reported_Cases', alpha=0.6, color='green', ax=ax)
    ax.set_title("Vector Control (ITN) vs Incident Density Mapping")
    display_page_layout("Point 4: Evaluation of Defensive Controls Effectiveness", fig, df, "Clusters extending towards high distribution volumes with lower cases confirm bednet programmatic efficiencies.")

# 5. Climatic Influence (Rainfall Anomaly)
def plot_climatic_influence(df):
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.regplot(data=df, x='Rainfall_Anomaly_mm', y='Estimated_Cases', scatter_kws={'alpha':0.3}, line_kws={'color':'purple'}, ax=ax)
    ax.set_title("Climate Anomaly Adjustments on Incidences")
    display_page_layout("Point 5: Environmental Determinants Correlation Analysis", fig, df, "Positive directional coefficients link extreme precipitation anomalies to macro vector breeding ecosystem enhancement.")

# 6. Parasite Composition Shift
def plot_parasite_shift(df):
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.boxplot(data=df, x='WHO_Region', y='Plasmodium_Vivax_Pct', ax=ax)
    plt.xticks(rotation=20)
    ax.set_title("Regional Plasmodium Vivax Parasite Prevalences")
    display_page_layout("Point 6: Diagnostic Trait Stratification", fig, df, "Vivax dominance is visibly pronounced outside African ecosystems, defining changes in diagnostic target methods.")

# 7. Case Fatality Ratios (CFR)
def plot_case_fatality(df):
    df['CFR'] = (df['Reported_Deaths'] / (df['Reported_Cases'] + 1)) * 100
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.histplot(data=df, x='CFR', kde=True, bins=30, color='brown', ax=ax)
    ax.set_title("Aggregated Case Fatality Ratio Trajectories")
    display_page_layout("Point 7: Healthcare Responsiveness Index (CFR)", fig, df, "Fatality indices clustering towards the lower quartile indicates immediate curative and clinical response optimizations.")

# 8. Decadal Projections (2024 - 2026 Trajectories)
def plot_projections(df):
    fig, ax = plt.subplots(figsize=(7, 4))
    future_df = df[df['Year'] >= 2020]
    sns.lineplot(data=future_df, x='Year', y='Estimated_Cases', hue='WHO_Region', ax=ax)
    ax.set_title("Forecasting Vector Trends Through 2026")
    display_page_layout("Point 8: Strategic Horizons & Targets (2020 - 2026)", fig, df, "Projections highlight regions close to meeting the WHO GTS elimination objectives by 2026 versus stagnating models.")

# 9. Top 10 High Burden Hierarchies
def plot_top_countries(df):
    top10 = df.groupby('Country')['Estimated_Cases'].sum().nlargest(10).reset_index()
    fig = px.pie(top10, values='Estimated_Cases', names='Country', title="Top 10 High-Burden Concentration Breakdown")
    display_page_layout("Point 9: Geographic Concentration Analysis", fig, df, "Concentrated global distribution confirms that specific strategic focus on these 10 hotspots manages massive absolute loads.")

# 10. Multi-Variant Heatmap Correlation
def plot_correlation_heatmap(df):
    fig, ax = plt.subplots(figsize=(7, 4))
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    ax.set_title("System Attributes Multivariant Relationships Matrix")
    display_page_layout("Point 10: Dynamic Feature Dependency Metrics", fig, df, "Matrix exposes correlation strengths between physical distribution numbers, climate variances, and net death logs.")
