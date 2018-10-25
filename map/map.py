import folium
import pandas


map1 = folium.Map(location=[38, -99], zoom_start=4)

fg = folium.FeatureGroup(name="My Map")

data = pandas.read_csv("Volcanoes_USA.txt")
lon = data["LON"]
lat = data["LAT"]
elev = data["ELEV"]


def add_color(val):
    if val< 1500 :
        return 'green'
    elif 1500 <= val < 3000 :
        return 'orange'
    else:
        return 'red'

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+" mt.", icon=folium.Icon(color=add_color(el))))

map1.add_child(fg)
map1.add_child(folium.LayerControl())
map1.save("naksha.html")


