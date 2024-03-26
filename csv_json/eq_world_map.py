import json

from plotly.graph_objs import Layout
from plotly import offline

# explore structure of data
filename = "data/eq_data_30_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    title = eq_dict["properties"]["title"]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(f"{title}<br>({lat}, {lon})")

# map the earthquakes
data = [
    {
        "type": "scattergeo",
        "text": hover_texts,
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": [5 * mag for mag in mags],
            "color": mags,
            "colorscale": "viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]
my_layout = Layout(title="global eqrthquakes")

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_earthquakes.html")
