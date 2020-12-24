import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])


def color_generator(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation <= 3000:
        return 'orange'
    else:
        return 'red'


myMap = folium.Map(location=[35.869999, -106.570999], zoom_start=6)

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, name, el in zip(lat, lon, name, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=name,
                                      fill_color=color_generator(el), color='grey', fill_opacity=0.7, radius=7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=(open('world.json', encoding='utf-8-sig').read()),
                             style_function=lambda x: {'fillColor': 'yellow' if x['properties']['POP2005'] < 10000000
                            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                            else 'red'}))


myMap.add_child(fgv)
myMap.add_child(fgp)
myMap.add_child(folium.LayerControl())


myMap.save("Map.html")
