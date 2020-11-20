import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt, mpld3
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

axes = plt.axes(projection = ccrs.Mercator())  # create a set of axes with Mercator projection
axes.add_feature(cf.COASTLINE) 
axes.set_extent([-128,-62,20,50])

def create_nodes():
    for index, row in nodes_df.iterrows():
        graph.add_node(row['UserID'], pos=(row['Latitude'], row['Longitude']))

def create_edges():
    print(edges_df)
    for index, row in edges_df.iterrows():
        graph.add_edge(row['Source'], row['Destination'])

def draw_map():
    for index, row in edges_df.iterrows():
        if index == 100:
            break
        source_long = nodes_df.loc[nodes_df['UserID']==row['Source']]['Longitude']
        source_lat = nodes_df.loc[nodes_df['UserID']==row['Source']]['Latitude']

        destination_long = nodes_df.loc[nodes_df['UserID']==row['Destination']]['Longitude']
        destination_lat = nodes_df.loc[nodes_df['UserID']==row['Destination']]['Latitude']
        print(source_long, source_lat, destination_long, destination_lat)
        print(row['Source'], row['Destination'])

        plt.plot([source_long, destination_long],[source_lat, destination_lat], color = 'blue', linewidth=0.05, marker='.', markersize = 0.1, transform=ccrs.Geodetic())
    # plt.savefig('gowalla_network_map.png')
    plt.draw()
    fig = plt.figure(1,figsize=(100, 50))
    # fig, ax = plt.subplots()
    # ax = axes.plot(111)
    # plt.show()
    # html_fig = mpld3.fig_to_html(fig)
    mpld3.save_html(fig, 'test.html')
    # plt.show()
    # mpld3.display(fig)
    # place plot in html format?
    # fig = plt.figure(figsize = (20,10))
    # html_plot = mpld3.display(fig)
    # # mpld3.save_html(html_plot, "gowalla_network_map1.html")

    # test plot
    #print(html_plot)
    # plt.show()

    # write to file
    # with open("gowalla_network_map2.html", "w") as file:
    #     file.write(html_plot)

if __name__ == "__main__":
    start = time.perf_counter()
    #create_nodes()
    #create_edges()
    draw_map()
    stop = time.perf_counter()
    print("it took ", stop - start, " seconds to draw the map")
