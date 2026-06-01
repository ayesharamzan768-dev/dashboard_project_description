Global Malaria & Pathogen Intelligence Command Center
​An advanced, interactive web portal designed for global epidemiological surveillance. This project maps chronologically matched case files, vector interventions, and climate anomalies across exactly 125 sovereign nations spanning all 6 official WHO Regions from the years 2000 to 2026.
​This platform is submitted as the final course project for Exploratory Data Analysis, guided by Instructor Ali Hassan Sherazi.
​⚙️ Setup and Deployment Instructions
​Prerequisite Environment
​Ensure you have Python 3.10+ installed. You can verify your system version using:bash
python --version
### Installation
Navigate to your root directory `/dashboard_project/` and install required dependencies:
```bash
pip install -r requirements.txt
Run Locally
​To test the responsive Plotly graphics on your system:
streamlit run app.py
🎯 Navigating the 10 Central Matrix Points
​The sidebar features an option menu structured around 10 distinct, mandatory surveillance layers. Selecting any of the points dynamically replaces the central stage with its corresponding visual plot, analytic descriptions, and its clean filtered spreadsheets:
​01 Executive Summary: Renders unified KPI blocks and a multi-dimensional search/sort spreadsheet.
​02 Pie Chart: Represents the proportional estimated case burden across global territories.
​03 Histogram: Maps the frequency distribution of Precipitation anomalies (Rainfall in mm).
​04 Line Chart: Generates chronological year-on-year curves comparing confirmed cases with WHO estimations.
​05 Bar Chart: Compares the aggregate reported deaths regionally across sovereign borders.
​06 Scatter Plot: Displays the statistical relationship between Rainfall anomalies and confirmed cases.
​07 Box Plot: Represents parasite strain variances (Plasmodium Vivax percentage proportions).
​08 Heatmap: Calculates a multidimensional pearson correlation matrix mapping cases, deaths, and distributed nets.
​09 Area Chart: Shows cumulative interventions (Distributed bednets volume) over the entire timeline.
​10 Count & Violin Plots: Measures data record densities alongside probability distributions of estimated deaths.