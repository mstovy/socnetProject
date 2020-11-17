import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import os
import cartopy.crs as ccrs
import cartopy.feature as cf
from cartopy.io import shapereader as shpreaderl
import time

path = os.path.dirname(__file__)
checkin_file_path = os.path.join(path, "gowalla_checkins_average.csv")
nodes_df = pd.read_csv(checkin_file_path)
edges_file_path = os.path.join(path, "gowalla_edges_only_us.csv")
# shape_path = os.path.join(path, "World_Countries.shp")
edges_df = pd.read_csv(edges_file_path)
graph = nx.Graph()
# shape = nx.read_shp(shape_path)

ax = plt.axes(projection = ccrs.Mercator())  # create a set of axes with Mercator projection
ax.add_feature(cf.COASTLINE) 
ax.set_extent([-128,-62,20,50])

def create_nodes():
    for index, row in nodes_df.iterrows():
        graph.add_node(row['UserID'], pos=(row['Latitude'], row['Longitude']))

def create_edges():
    print(edges_df)
    for index, row in edges_df.iterrows():
        graph.add_edge(row['Source'], row['Destination'])

def draw_map():
    for index, row in edges_df.iterrows():
        source_long = nodes_df.loc[nodes_df['UserID']==row['Source']]['Longitude']
        source_lat = nodes_df.loc[nodes_df['UserID']==row['Source']]['Latitude']

        destination_long = nodes_df.loc[nodes_df['UserID']==row['Destination']]['Longitude']
        destination_lat = nodes_df.loc[nodes_df['UserID']==row['Destination']]['Latitude']
        print(source_long, source_lat, destination_long, destination_lat)
        print(row['Source'], row['Destination'])

        plt.plot([source_long, destination_long],[source_lat, destination_lat], color = 'blue', linewidth=0.05, marker='.', markersize = 0.1, transform=ccrs.Geodetic())

    plt.show()

if __name__ == "__main__":
    start = time.perf_counter()
    #create_nodes()
    #create_edges()
    draw_map()
    stop = time.perf_counter()
    print("it took ", start - stop, " seconds to draw the map")
