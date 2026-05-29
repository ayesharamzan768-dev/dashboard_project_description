import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from filters import apply_filters

# Page layout configuration
st.set_page_config(page_title="Development Projects Dashboard", layout="wide")
st.title("📊 Pakistan Development Projects Dashboard")

# Load Data
@st.cache_data
def load_data():
    # Replace with your actual file path or github link
    df = pd.read_excel("clean_data.xlsx") 
    df.columns = df.columns.str.strip()
    return df

try:
    df_raw = load_data()
    
    # Apply sidebar filters
    df = apply_filters(df_raw)
    
    # Library selection toggle for professor's criteria
    chart_library = st.sidebar.radio("🎨 Select Chart Library", ["Plotly (Interactive)", "Matplotlib/Seaborn (Static)"])

    if df.empty:
        st.warning("⚠️ Selected filters ke mutabiq koi data available nahi hai. Please filters change karein.")
    else:
        # ----------------------------------------------------
        # 1 to 3 Charts/Tables Code should be here...
        st.info("Showing Charts 1, 2, 3 (Working)...")
        
        # ----------------------------------------------------
        # 4th Point: Target Province Breakdown (FIXED)
        st.subheader("📌 4. Projects Breakdown by Target Province")
        
        target_col = 'Target Province'
        if target_col in df.columns:
            # Group data safely
            province_counts = df[target_col].value_counts().reset_index()
            province_counts.columns = [target_col, 'Count']
            
            col1, col2 = st.columns([1, 2])
            with col1:
                st.write("### Data Table")
                st.dataframe(province_counts, use_container_width=True)
                
            with col2:
                if chart_library == "Plotly (Interactive)":
                    fig = px.bar(province_counts, x=target_col, y='Count', 
                                 title="Projects by Target Province",
                                 labels={target_col: "Province", "Count": "Number of Projects"},
                                 color=target_col)
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    fig, ax = plt.subplots(figsize=(8, 4))
                    sns.barplot(data=province_counts, x=target_col, y='Count', ax=ax, palette="Set2")
                    plt.xticks(rotation=45)
                    plt.title("Projects by Target Province")
                    st.pyplot(fig)
        else:
            st.error(f"❌ Error: '{target_col}' column data mein nahi mila. Please check format.")

        # ----------------------------------------------------
        # 5th Point: Status/Type Breakdown
        st.subheader("📌 5. Project Status Breakdown")
        status_col = 'Project Status' if 'Project Status' in df.columns else (df.columns[3] if len(df.columns) > 3 else None)
        if status_col:
            status_df = df[status_col].value_counts().reset_index()
            status_df.columns = [status_col, 'Count']
            
            col1, col2 = st.columns(2)
            with col1:
                st.dataframe(status_df, use_container_width=True)
            with col2:
                if chart_library == "Plotly (Interactive)":
                    fig = px.pie(status_df, names=status_col, values='Count', title="Project Status Share")
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    fig, ax = plt.subplots()
                    ax.pie(status_df['Count'], labels=status_df[status_col], autopct='%1.1f%%', startangle=90)
                    st.pyplot(fig)

        # ----------------------------------------------------
        # 6th Point: Development Partners Analysis
        st.subheader("📌 6. Top Development Partners")
        partner_col = 'Development Partner'
        if partner_col in df.columns:
            partner_df = df[partner_col].value_counts().head(10).reset_index()
            partner_df.columns = [partner_col, 'Count']
            
            if chart_library == "Plotly (Interactive)":
                fig = px.bar(partner_df, y=partner_col, x='Count', orientation='h', title="Top 10 Partners")
                st.plotly_chart(fig, use_container_width=True)
            else:
                fig, ax = plt.subplots(figsize=(8, 4))
                sns.barplot(data=partner_df, y=partner_col, x='Count', ax=ax)
                st.pyplot(fig)

        # ----------------------------------------------------
        # 7th & 8th Point: Financials (Commitment vs Spending)
        st.subheader("📌 7 & 8. Financial Overview: Total Commitments & Disbursements")
        # Check for dynamic financial column names
        amt_cols = [c for c in df.columns if 'Amount' in c or 'Commitment' in c or 'Disbursement' in c]
        if len(amt_cols) >= 2:
            df_fin = df.groupby('Year')[amt_cols[:2]].sum().reset_index()
            st.dataframe(df_fin, use_container_width=True)
            
            if chart_library == "Plotly (Interactive)":
                fig = px.line(df_fin, x='Year', y=amt_cols[:2], title="Financial Trends Over Time")
                st.plotly_chart(fig, use_container_width=True)
            else:
                fig, ax = plt.subplots(figsize=(8, 4))
                df_fin.set_index('Year')[amt_cols[:2]].plot(kind='line', ax=ax, marker='o')
                st.pyplot(fig)
        else:
            st.warning("Financial columns (Commitment/Disbursement) detail not found for analysis.")

        # ----------------------------------------------------
        # 9th & 10th Point: Sector and Region Matrix
        st.subheader("📌 9 & 10. Sector vs Target Region Matrix")
        sector_col = 'Sector' if 'Sector' in df.columns else None
        if sector_col and target_col in df.columns:
            matrix_df = pd.crosstab(df[sector_col], df[target_col])
            st.write("### Cross-Tabulation View")
            st.dataframe(matrix_df, use_container_width=True)
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.heatmap(matrix_df, annot=True, cmap="YlGnBu", fmt='d', ax=ax)
            st.title("Sector vs Region Distribution Heatmap")
            st.pyplot(fig)

except Exception as e:
    st.error(f"❌ Dashboard Main Error: {e}")
