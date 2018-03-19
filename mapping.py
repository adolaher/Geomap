import folium
import pandas

data = pandas.read_csv("data.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation = list(data["ELEV"])

def colorize(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev < 3000:
     return 'orange'
    else:
        return 'red'

map = folium.Map(location=[42.260025,-71.464590], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="Map")

for lat, lon, el in zip(latitude, longitude, elevation):
    fg.add_child(folium.CircleMarker(location=[lat,lon], radius = 7, popup=str(el)+" m",
    fill_color=colorize(el), color = "grey", fill=True, fill_opacity=0.5))

map.add_child(fg)

map.save("Map.html")
