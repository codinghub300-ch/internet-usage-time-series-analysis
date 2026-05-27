# ==========================================================
# PART 2 – TIME SERIES ANALYSIS
# Weekly Loan Applications
# Interactive Plots + PDF Report
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import sys

from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.graphics.gofplots import qqplot
from sklearn.metrics import mean_squared_error

# PDF
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

# ==========================================================
# Capture terminal output
# ==========================================================

buffer = io.StringIO()
sys.stdout = buffer

# ==========================================================
# Load Data
# ==========================================================

df = pd.read_excel("Data-Part_2_TSA.xlsx")
series = df["Applications"]

sns.set_theme(style="whitegrid", context="talk")

# ==========================================================
# (a) Plot the time series
# ==========================================================

plt.figure(figsize=(10,5))
plt.plot(series, linewidth=2.5)
plt.title("Weekly Loan Applications")
plt.xlabel("Week")
plt.ylabel("Number of Applications")
plt.tight_layout()
plt.savefig("plot_timeseries.png", dpi=300)
plt.show()   # Interactive display
plt.close()

print("\n(a) Visual Inspection:")
print("If the series shows persistence, trends, or slow decay patterns,")
print("this suggests autocorrelation between weeks.\n")

# ==========================================================
# (b) ACF and PACF
# ==========================================================

fig, ax = plt.subplots(1,2, figsize=(14,5))
plot_acf(series, lags=20, ax=ax[0])
ax[0].set_title("Autocorrelation Function (ACF)")
plot_pacf(series, lags=20, ax=ax[1])
ax[1].set_title("Partial Autocorrelation Function (PACF)")
plt.tight_layout()
plt.savefig("plot_acf_pacf.png", dpi=300)
plt.show()  # Interactive display
plt.close()

# ==========================================================
# (c) Suggest Appropriate Model
# ==========================================================

print("\n(c) Model Suggestion:")
print("If ACF tails off gradually and PACF cuts off after lag p → AR(p)")
print("If PACF tails off and ACF cuts off after lag q → MA(q)")
print("If both tail off → ARMA(p,q)\n")

order = (1,0,1)
print(f"Selected Model: ARIMA{order}")

model = ARIMA(series, order=order)
model_fit = model.fit()

# ==========================================================
# (d) Parameters, CI, and P-values
# ==========================================================

print("\n(d) Model Parameters:")
params = model_fit.params
conf_int = model_fit.conf_int()
pvalues = model_fit.pvalues

results_table = pd.DataFrame({
    "Estimate": params,
    "Lower CI": conf_int.iloc[:,0],
    "Upper CI": conf_int.iloc[:,1],
    "P-value": pvalues
})

print(results_table)

# ==========================================================
# (e) Mean Squared Error
# ==========================================================

fitted = model_fit.fittedvalues
mse = mean_squared_error(series, fitted)

print(f"\n(e) Mean Squared Error (MSE): {mse:.4f}")

# ==========================================================
# (f) Residual Diagnostics
# ==========================================================

residuals = model_fit.resid

fig, axes = plt.subplots(2,2, figsize=(14,10))

qqplot(residuals, line='s', ax=axes[0,0])
axes[0,0].set_title("Normal Probability Plot")

axes[0,1].scatter(fitted, residuals)
axes[0,1].axhline(0, linestyle='--')
axes[0,1].set_title("Residuals vs Fitted")

sns.histplot(residuals, kde=True, ax=axes[1,0])
axes[1,0].set_title("Histogram of Residuals")

axes[1,1].plot(residuals)
axes[1,1].axhline(0, linestyle='--')
axes[1,1].set_title("Residual Time Series")

plt.tight_layout()
plt.savefig("plot_residuals.png", dpi=300)
plt.show()  # Interactive display
plt.close()

# ==========================================================
# Restore stdout
# ==========================================================

sys.stdout = sys.__stdout__
terminal_output = buffer.getvalue()

# ==========================================================
# Create PDF
# ==========================================================

doc = SimpleDocTemplate(
    "Part_2_Time_Series_Report.pdf",
    pagesize=A4
)

styles = getSampleStyleSheet()
elements = []

elements.append(Paragraph("Part 2 – Time Series Analysis Report", styles["Heading1"]))
elements.append(Spacer(1, 0.3*inch))

# Add terminal output
for line in terminal_output.split("\n"):
    elements.append(Paragraph(line, styles["Normal"]))
    elements.append(Spacer(1, 0.1*inch))

elements.append(Spacer(1, 0.3*inch))

# Insert plots
elements.append(Image("plot_timeseries.png", width=6*inch, height=3.5*inch))
elements.append(Spacer(1, 0.3*inch))

elements.append(Image("plot_acf_pacf.png", width=6*inch, height=3.5*inch))
elements.append(Spacer(1, 0.3*inch))

elements.append(Image("plot_residuals.png", width=6*inch, height=4*inch))
elements.append(Spacer(1, 0.3*inch))

# ==========================================================
# Add ARIMA Parameter Table
# ==========================================================

data = [["Parameter", "Estimate", "Lower CI", "Upper CI", "P-value"]]
for i, row in results_table.iterrows():
    data.append([i, f"{row['Estimate']:.4f}", f"{row['Lower CI']:.4f}",
                 f"{row['Upper CI']:.4f}", f"{row['P-value']:.4f}"])

table = Table(data, hAlign='LEFT')
table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#d5dae6")),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('ALIGN',(1,1),(-1,-1),'CENTER')
]))
elements.append(Paragraph("ARIMA Model Parameters:", styles["Heading2"]))
elements.append(table)
elements.append(Spacer(1,0.3*inch))

# ==========================================================
# Add MSE
# ==========================================================

elements.append(Paragraph(f"Mean Squared Error (MSE): {mse:.4f}", styles["Normal"]))
elements.append(Spacer(1,0.3*inch))

# ==========================================================
# Add Sample of Actual vs Fitted
# ==========================================================

sample_df = pd.DataFrame({
    "Actual": series,
    "Fitted": fitted
}).head(10)

sample_data = [list(sample_df.columns)] + sample_df.round(2).values.tolist()
sample_table = Table(sample_data, hAlign='LEFT')
sample_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#d5dae6")),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('ALIGN',(1,1),(-1,-1),'CENTER')
]))
elements.append(Paragraph("Sample of Actual vs Fitted Values:", styles["Heading2"]))
elements.append(sample_table)
elements.append(Spacer(1,0.3*inch))

# ==========================================================
# Build PDF
# ==========================================================

doc.build(elements)
print("✅ PDF Generated: Part_2_Time_Series_Report.pdf")