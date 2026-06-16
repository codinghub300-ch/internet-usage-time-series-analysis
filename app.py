import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

st.set_page_config(
    page_title="Coding Hub Projects",
    layout="wide"
)

st.title("🚀 Coding Hub Projects")
st.markdown("### Internet Usage Analysis & Time Series Analysis")

# ==================================================
# PART 1
# ==================================================

st.header("🌐 Internet Usage Analysis")

url = "https://raw.githubusercontent.com/TrainingByPackt/Interactive-Data-Visualization-with-Python/master/datasets/share-of-individuals-using-the-internet.csv"

df = pd.read_csv(url)

st.dataframe(df, use_container_width=True, height=500)

internet_2016 = df[df["Year"] == 2016]

# World Map

st.subheader("🌍 Worldwide Internet Usage (2016)")

fig_world = px.choropleth(
    internet_2016,
    locations="Code",
    color="Individuals using the Internet (% of population)",
    hover_name="Country",
    color_continuous_scale="Viridis"
)

st.plotly_chart(fig_world, use_container_width=True)

# Asia Map

st.subheader("🌏 Asia Internet Usage (2016)")

fig_asia = px.choropleth(
    internet_2016,
    locations="Code",
    color="Individuals using the Internet (% of population)",
    hover_name="Country",
    color_continuous_scale="Cividis"
)

fig_asia.update_layout(
    geo_scope="asia"
)

st.plotly_chart(fig_asia, use_container_width=True)

# Animated Map

st.subheader("📈 Internet Growth Over Years")

fig_anim = px.choropleth(
    df,
    locations="Code",
    color="Individuals using the Internet (% of population)",
    hover_name="Country",
    animation_frame="Year",
    color_continuous_scale="Viridis",
    range_color=[0,100]
)

st.plotly_chart(fig_anim, use_container_width=True)

# ==================================================
# PART 2
# ==================================================

st.header("📊 Time Series Analysis")

try:

    tsa_df = pd.read_excel("part2/Data-Part_2_TSA.xlsx")

    series = tsa_df["Applications"]

    st.subheader("Weekly Loan Applications")

    fig1, ax1 = plt.subplots(figsize=(10,4))
    ax1.plot(series)
    ax1.set_title("Weekly Loan Applications")
    st.pyplot(fig1)

    st.subheader("ACF & PACF")

    fig2, axes = plt.subplots(1,2, figsize=(12,4))

    plot_acf(series, lags=20, ax=axes[0])
    plot_pacf(series, lags=20, ax=axes[1])

    st.pyplot(fig2)

    st.subheader("ARIMA Model")

    model = ARIMA(series, order=(1,0,1))
    model_fit = model.fit()

    st.write(model_fit.summary())

    st.subheader("Residuals")

    residuals = model_fit.resid

    fig3, ax3 = plt.subplots(figsize=(10,4))
    ax3.plot(residuals)
    ax3.axhline(0)
    ax3.set_title("Residual Time Series")

    st.pyplot(fig3)

except Exception as e:
    st.error(f"Error loading Time Series data: {e}")

# ==================================================
# Footer
# ==================================================

st.markdown("---")
st.markdown("Developed by Coding Hub 💙")


