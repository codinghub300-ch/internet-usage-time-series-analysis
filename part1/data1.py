import pandas as pd
import plotly.express as px

# ================================
# Load Dataset
# ================================
url = "https://raw.githubusercontent.com/TrainingByPackt/Interactive-Data-Visualization-with-Python/master/datasets/share-of-individuals-using-the-internet.csv"
internet_usage_df = pd.read_csv(url)

# ================================
# Common Layout for All Maps
# ================================
common_layout = dict(
    geo=dict(showframe=False, showcoastlines=True, projection_type='natural earth'),
    coloraxis_colorbar=dict(title="% Internet Users", ticksuffix="%"),
    title_font=dict(size=24, family="Arial, sans-serif"),
    font=dict(family="Arial, sans-serif", size=12),
    margin=dict(l=10, r=10, t=50, b=10)
)

# ================================
# Subset for Year 2016
# ================================
internet_2016 = internet_usage_df.query("Year == 2016")

# ================================
# 1️⃣ Worldwide Choropleth (2016)
# ================================
fig_world = px.choropleth(
    internet_2016,
    locations="Code",
    color="Individuals using the Internet (% of population)",
    hover_name="Country",
    hover_data={"Year": True},
    color_continuous_scale=px.colors.sequential.Viridis
)

fig_world.update_layout(
    title_text='🌐 Internet Usage Across the World - 2016',
    **common_layout
)
fig_world.show()

# ================================
# 2️⃣ Asia-Only Choropleth (2016)
# ================================
fig_asia = px.choropleth(
    internet_2016,
    locations="Code",
    color="Individuals using the Internet (% of population)",
    hover_name="Entity",
    hover_data={"Year": True},
    color_continuous_scale=px.colors.sequential.Cividis
)

fig_asia.update_layout(
    geo_scope="asia",
    title_text='🌏 Internet Usage in Asia - 2016',
    **common_layout
)
fig_asia.show()

# ================================
# 3️⃣ Globe-Style Choropleth (2016)
# ================================
fig_globe = px.choropleth(
    internet_2016,
    locations="Code",
    color="Individuals using the Internet (% of population)",
    hover_name="Entity",
    color_continuous_scale=px.colors.sequential.Viridis
)

fig_globe.update_layout(
    title_text='🌍 Internet Usage Across the World - 2016 (Globe View)',
    geo=dict(
        projection_type='natural earth',
        showland=True,
        landcolor='lightgray',
        showocean=True,
        oceancolor='lightblue'
    ),
    **common_layout
)
fig_globe.show()

# ================================
# 4️⃣ Animated Choropleth Over Years
# ================================
# Sort by Year
internet_usage_df.sort_values(by=["Year"], inplace=True)

fig_animated = px.choropleth(
    internet_usage_df,
    locations="Code",
    color="Individuals using the Internet (% of population)",
    hover_name="Entity",
    hover_data={"Year": True},
    animation_frame="Year",
    color_continuous_scale=px.colors.sequential.Viridis,
    range_color=[0, 100]  # Keep scale consistent across years
)

fig_animated.update_layout(
    title_text='📈 Global Internet Usage Growth Over Time',
    **common_layout
)

# Adjust animation speed
fig_animated.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 800

fig_animated.show()