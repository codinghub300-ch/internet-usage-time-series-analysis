import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Internet Usage & Time Series Analysis",
    layout="wide"
)

st.title("🌐 Internet Usage & Time Series Analysis")
st.markdown("Project by Coding Hub")

# ======================
# Internet Usage Section
# ======================

st.header("Internet Usage Around The World")

url = "https://raw.githubusercontent.com/TrainingByPackt/Interactive-Data-Visualization-with-Python/master/datasets/share-of-individuals-using-the-internet.csv"

df = pd.read_csv(url)

st.write(df.columns.tolist())
st.write(df.head())

internet_2016 = df[df["Year"] == 2016]

fig = px.choropleth(
    internet_2016,
    locations="Code",
    color="Individuals using the Internet (% of population)",
    hover_name="Entity",
    color_continuous_scale="Viridis"
)

st.plotly_chart(fig, use_container_width=True)

# ======================
# Dataset Preview
# ======================

st.header("Dataset Preview")

st.dataframe(internet_2016.head())

