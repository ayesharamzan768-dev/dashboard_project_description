# Exploratory Data Analysis Dashboard — Malaria Case Study (Pakistan)

### Course Project Documentation
* **Course Title:** Exploratory Data Analysis (EDA)
* **Instructor Name:** Ali Hassan Sherazi
* **Submission Date:** 05-June-2026
* **Project Status:** Deploying to Streamlit Community Cloud

---

## 📋 Project Overview
This project is an interactive, professional-grade Data Visualization Dashboard built using **Streamlit**, **Pandas**, **Matplotlib**, and **Seaborn**. It analyzes the structural trends, mortality rates, and vector control interventions for Malaria cases across Pakistan from 2015 to 2025.

The application features a fully modular script architecture (`app.py`, `charts.py`, `filters.py`) and tracks data variations dynamically across **10 mandatory chart configurations** via linked sidebar filters.

---

## 📂 Modular Structure File Guide
* `data/malaria_data.csv`: Source dataset containing critical epidemiological features.
* `app.py`: The frontend portal managing layout, KPI cards, and dynamic UI updates.
* `filters.py`: Backend data parsing, text clearing, and range masking functions.
* `charts.py`: Visual processing asset creating 10 individual figures (Pie, Line, Box, Heatmap, Histogram, Scatter, Area, Count, Violin, and Bar charts).
* `requirements.txt`: Environment package manifest for Streamlit deployment cloud.

---

## 🛠️ Installation & Local Run Deployment Guide

1. **Navigate into the Project Workspace:**
   ```bash
   cd dashboard_project