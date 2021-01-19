import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly as pl
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import re

from ..helpers import reports, us_county_city_mapdata

def init_dashboard(server):
    all_ufo_df = reports
    map_data = us_county_city_mapdata

    us_states_df = all_ufo_df[all_ufo_df["State"].isin(map_data["State"])]
    us_state_counts = us_states_df.groupby(["State"]).size().reset_index(name="Counts")

    state_totals_fig = px.bar(us_state_counts, x="State", y="Counts", labels={"Counts":"Number of Reports"}, title="State Totals, All Time")

    reports_with_map_data = us_states_df.merge(map_data[["City", "County", "State", "State name", "Population", "Density","lat", "lng", "county_lat", "county_lng"]], how="inner", on=["City", "State"])

    county_counts = reports_with_map_data.groupby(["County", "State", "State name", "county_lat", "county_lng"]).size().reset_index(name="Count")
    county_counts["Text"] = county_counts["County"] + " County, " + county_counts["State"] + "<br>Number of reports: " + county_counts["Count"].apply(str)
    county_limits = [(0,99),(100,299),(300,499),(500,699), (700,  999), (1000, 2000)]
    county_colors = ["royalblue","crimson","lightseagreen","orange","purple", "lavender"]
    county_scale = 3

    county_counts_bubble = go.Figure()

    for i in range(len(county_limits)):
        lim = county_limits[i]
        df_sub = county_counts[county_counts["Count"].between(lim[0],lim[1])]
        county_counts_bubble.add_trace(go.Scattergeo(
            locationmode = "USA-states",
            lon = df_sub["county_lng"],
            lat = df_sub["county_lat"],
            text = df_sub["Text"],
            marker = dict(
                size = df_sub["Count"]/county_scale,
                color = county_colors[i],
                line_color="rgb(40,40,40)",
                line_width=0.5,
                sizemode = "area"
            ),
            name = "{0} - {1}".format(lim[0],lim[1])))

    county_counts_bubble.update_layout(
            title_text = "UFO Reports per US County",
            showlegend = True,
            geo = dict(
                scope = "usa",
                landcolor = "rgb(217, 217, 217)",
            )
        )

    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix="/dashapp/"
        # external_stylesheets=[
        #     '/static/dist/css/styles.css',
        # ]
    )

    # Create Dash Layout
    dash_app.layout = html.Div(children=[
        dcc.Graph(
            id="bubble_map",
            figure=county_counts_bubble
        ),
        dcc.Graph(
            id="state_totals",
            figure=state_totals_fig
        )
    ])

    return dash_app.server

