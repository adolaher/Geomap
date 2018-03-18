import folium
map = folium.Map(location=[42.260025,-71.464590], zoom_start=6, tiles="Mapbox Bright")

map.add_child(folium.Marker(location=[42.260025,-71.464590], popup="Ashland", icon=folium.Icon(color='red')))

map.save("Map.html")
