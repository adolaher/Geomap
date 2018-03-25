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

fg = folium.FeatureGroup(name="Volcano Locations")

for lat, lon, el in zip(latitude, longitude, elevation):
    fg.add_child(folium.CircleMarker(location=[lat,lon], radius = 7, popup=str(el)+" m",
    fill_color=colorize(el), color = "grey", fill=True, fill_opacity=0.5))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('pop_data.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map.html")
