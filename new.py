import cartopy.crs as ccrs
from cartopy.io import shapereader as shpreader
import matplotlib.pyplot as plt
import networkx as nx

name_long ='US'
paises = ['Portugal', 'France', 'Canada', 'Brazil', 'Kazakhstan']
cidades = ['Aveiro', 'Ust-Kamenogorsk', 'Manaus']
links = [('Aveiro', 'Ust-Kamenogorsk'), 
         ('Manaus', 'Ust-Kamenogorsk'),
         ('Aveiro', 'Manaus')]
position = {'Aveiro': (-8.65, 40.6),
            'Manaus': (-60.0, -3.1),
            'Ust-Kamenogorsk': (82.6, 49.97)}

# map using cartopy:
shapename = 'admin_0_countries'
countries_shp = shpreader.natural_earth(resolution='110m',
                                    category='cultural', name=shapename)

ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=0.0, globe=None))
ax.set_global()

for country in shpreader.Reader(countries_shp).records():    
    nome = country.attributes['name_long']
    if nome in paises:
        i = paises.index(nome)
        artist = ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                           facecolor='yellow',
                           #alpha=0.5,
                           zorder=10)
    else:
        artist = ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                           facecolor='0.9',
                           zorder=10)

# add some data over the cartopy map (using networkx):                              
G = nx.Graph()
G.add_nodes_from(cidades)
G.add_edges_from(links)

nx.draw_networkx_nodes(G, position, node_size=20, nodelist=cidades, zorder=20)
edges=nx.draw_networkx_edges(G, position, edgelist=links, zorder=20)

plt.show()