import folium
map = folium.Map(location=[45.3311, -121.6625], zoom_start=4)
folium.Marker([45.3311, -121.6625]).add_to(map)
folium.Marker([9.537, -13.677]).add_to(map)
folium.Marker([40.712784, -74.005941]).add_to(map)
map.save("map.html")