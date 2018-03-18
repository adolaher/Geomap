import folium
import pandas

data = pandas.read_csv("data.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])

map = folium.Map(location=[42.260025,-71.464590], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="Map")

for lat, lon in zip(latitude, longitude):
    fg.add_child(folium.Marker(location=[lat,lon], popup="Volcano", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Map.html")
