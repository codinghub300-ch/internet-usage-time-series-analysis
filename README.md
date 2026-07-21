# Internet Usage Choropleth Map & Time Series Analysis 

Live Demo:
https://internet-usage-time-series-analysis-yevgg4lafo3happisbxxdvc.streamlit.app/

A Python-based data analysis project that combines interactive global data visualization with time series forecasting techniques.

The project is divided into two main parts:
1. Internet Usage Choropleth Map Visualization
2. Time Series Analysis of Weekly Loan Applications

---

##  Project Overview

This project demonstrates how Python can be used for:
- Interactive Data Visualization
- Geographic Analysis
- Time Series Modeling
- Statistical Forecasting
- Residual Diagnostics

The project uses real-world datasets to analyze global internet adoption trends and weekly banking loan application behavior.

---

#  Part 1 — Internet Usage Choropleth Map

This section visualizes global internet usage percentages using interactive choropleth maps built with Plotly Express.

---

##  Dataset

Source Dataset:
- Global internet usage statistics across multiple years

Main Features:
- Country
- Country Code
- Year
- Individuals using the Internet (% of population)

---

##  Technologies Used

- Python
- Pandas
- Plotly Express

---

##  Tasks Performed

###  Data Preparation
- Downloaded dataset
- Filtered records for specific years
- Sorted data chronologically

###  Choropleth Visualization
Generated interactive world maps using:
- Country Codes
- Internet Usage Percentage
- Hover Information
- Plasma Color Scale

###  Geographic Analysis
Analyzed:
- Western vs Eastern internet penetration
- Canada & Australia compared to Europe
- Global internet growth over time

###  Animated Visualization
Used:
- animation_frame = "Year"

to visualize internet adoption growth globally over the years.

###  Globe Projection
Implemented:
- Natural Earth Projection
- Asia-only geographic scope

---

##  Key Insights

- Western Europe and North America showed the highest internet penetration.
- Canada and Australia reached internet usage levels comparable to top European countries.
- Developing regions experienced rapid internet growth after 2005.
- The global digital divide is narrowing over time.

---

#  Part 2 — Time Series Analysis

This section analyzes weekly loan applications using statistical time series techniques.

---

##  Dataset

Excel dataset containing:
- Weekly loan application counts
- Two years of observations

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Statsmodels
- Matplotlib
- Seaborn

---

##  Tasks Performed

###  Time Series Visualization
- Plotted weekly loan applications
- Observed autocorrelation behavior

###  ACF & PACF Analysis
Generated:
- Autocorrelation Function (ACF)
- Partial Autocorrelation Function (PACF)

###  ARIMA Modeling
Selected:
- ARIMA(1,0,1)

for forecasting and autocorrelation modeling.

###  Model Evaluation
Calculated:
- Mean Squared Error (MSE)
- Confidence Intervals
- P-values

###  Residual Diagnostics
Generated:
1. Q-Q Plot
2. Residual vs Fitted Plot
3. Residual Histogram
4. Residual Time Series Plot

---

##  Key Insights

- Loan applications exhibit autocorrelation behavior.
- ARIMA(1,0,1) effectively modeled the time series.
- Residual diagnostics confirmed acceptable model performance.
- Low MSE indicated strong predictive accuracy.


---

## Project Goals
. Visualize global internet adoption trends
. Understand geographic digital disparities
. Analyze autocorrelation in financial data
. Build forecasting models using ARIMA
. Practice statistical diagnostics and visualization

---

##  How to Run

### 1. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn plotly statsmodels reportlab openpyxl

```

---

---

<div align="center">

## 💙 Developed by Coding Hub

Time Series Analysis & Data Visualization Project

© 2026 Coding Hub. All Rights Reserved.

</div>

