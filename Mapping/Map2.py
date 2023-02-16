import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')

lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])


def colorMaker(elevation):
    if elevation < 1500:
        return 'green'
    elif elevation > 3000:
        return 'red'
    else:
        return 'orange'



map = folium.Map(location=[40.588193, -107.799416], zoom_start=6, tiles='Stamen Terrain')

fgv = folium.FeatureGroup(name='Volcanoes')

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+'m', fill_color=colorMaker(el), fill_opacity=0.7, color='grey'))

fgp = folium.FeatureGroup(name='Populaion')


fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save('Map2.html')
