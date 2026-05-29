import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def generate_all_charts(df):
    """
    Generates 10 distinct mandatory plots based on the filtered dataframe.
    """
    if df.empty:
        st.warning("No data available for the selected filters.")
        return

    sns.set_theme(style="whitegrid")
    
    # --- 1. PIE CHART ---
    st.subheader("1. Provincial Distribution of Total Estimated Cases")
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    prov_data = df.groupby('Province')['Estimated_Cases_WHO'].sum()
    ax1.pie(prov_data, labels=prov_data.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set2"))
    ax1.axis('equal')
    st.pyplot(fig1)
    plt.close()

    # --- 2. LINE CHART ---
    st.subheader("2. Yearly Case Trajectory Trend (2015 - 2025)")
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    # FIXED SYNTAX ERROR: Removed extra bracket from groupby
    yearly = df.groupby('Year')['Reported_Confirmed_Cases'].sum().reset_index()
    sns.lineplot(data=yearly, x='Year', y='Reported_Confirmed_Cases', marker='o', color='firebrick', ax=ax2)
    ax2.set_title("Infection Acceleration Over Time")
    st.pyplot(fig2)
    plt.close()

    # --- 3. BOX PLOT ---
    st.subheader("3. Rainfall Anomaly Variance Across Provinces")
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    sns.boxplot(data=df, x='Province', y='Rainfall_Anomaly_mm', palette="Accent", ax=ax3)
    st.pyplot(fig3)
    plt.close()

    # --- 4. HEATMAP (CORRELATION) ---
    st.subheader("4. Correlation Matrix of Epidemiological Variables")
    fig4, ax4 = plt.subplots(figsize=(8, 5))
    num_cols = ['Reported_Confirmed_Cases', 'Estimated_Cases_WHO', 'Reported_Deaths', 'Rainfall_Anomaly_mm', 'Bednets_Distributed']
    sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax4)
    st.pyplot(fig4)
    plt.close()

    # --- 5. HISTOGRAM ---
    st.subheader("5. Distribution Range of Reported Deaths")
    fig5, ax5 = plt.subplots(figsize=(10, 4))
    sns.histplot(data=df, x='Reported_Deaths', kde=True, color='purple', bins=15, ax=ax5)
    st.pyplot(fig5)
    plt.close()

    # --- 6. SCATTER PLOT ---
    st.subheader("6. Rainfall Anomaly vs. Estimated Cases Indicator")
    fig6, ax6 = plt.subplots(figsize=(10, 4))
    sns.scatterplot(data=df, x='Rainfall_Anomaly_mm', y='Estimated_Cases_WHO', hue='Province', style='Province', s=100, ax=ax6)
    st.pyplot(fig6)
    plt.close()

    # --- 7. AREA CHART ---
    st.subheader("7. Cumulative Bednets Distributed Distribution")
    fig7, ax7 = plt.subplots(figsize=(10, 4))
    area_data = df.groupby('Year')['Bednets_Distributed'].sum().reset_index()
    ax7.fill_between(area_data['Year'], area_data['Bednets_Distributed'], color="skyblue", alpha=0.4)
    ax7.plot(area_data['Year'], area_data['Bednets_Distributed'], color="Slateblue", alpha=0.6)
    ax7.set_xlabel("Year")
    ax7.set_ylabel("Total Distributed Units")
    st.pyplot(fig7)
    plt.close()

    # --- 8. COUNT PLOT ---
    st.subheader("8. Data Point Counts Monitored Per Province")
    fig8, ax8 = plt.subplots(figsize=(8, 3))
    sns.countplot(data=df, x='Province', palette="Pastel1", ax=ax8)
    st.pyplot(fig8)
    plt.close()

    # --- 9. VIOLIN PLOT ---
    st.subheader("9. Density and Spread of Confirmed Infections")
    fig9, ax9 = plt.subplots(figsize=(10, 4))
    sns.violinplot(data=df, x='Province', y='Reported_Confirmed_Cases', palette="muted", ax=ax9)
    st.pyplot(fig9)
    plt.close()

    # --- 10. BAR CHART ---
    st.subheader("10. Total Confirmed Cases Compared Regionally")
    fig10, ax10 = plt.subplots(figsize=(10, 4))
    sns.barplot(data=df, x='Province', y='Reported_Confirmed_Cases', estimator=sum, errorbar=None, palette="dark:salmon_r", ax=ax10)
    st.pyplot(fig10)
    plt.close()