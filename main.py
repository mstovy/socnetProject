import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import os
# from mpl_toolkits.basemap import Basemap

path = os.path.dirname(__file__)
checkin_file_path = os.path.join(path, "gowalla_checkins_average.csv")
nodes_df = pd.read_csv(checkin_file_path)
edges_file_path = os.path.join(path, "Gowalla_edges.csv")
edges_df = pd.read_csv(edges_file_path)
graph = nx.Graph()
user_ids = nodes_df['UserID']

# m = BaseMap(
#     projection = 'merc',
#     ellps = 'WGS84',
#     llcrnrlon=-130,
#     llcrnrlat=25,
#     urcrnrlon=-60,
#     urcrnrlat=50,
#     lat_ts=0,
#     resolution='i',
#     suppress_ticks=True)

def create_nodes():
    for index, row in nodes_df.iterrows():
        graph.add_node(row['UserID'], pos=(row['Latitude'], row['Longitude']))

def create_edges():
    print(edges_df)
    for index, row in edges_df.iterrows():
        if (row['Source'] in user_ids) and  (row['Destination'] in user_ids):
            graph.add_edge(row['Source'], row['Destination'])

def draw_map():
    nx.draw(graph)
    plt.show()

if __name__ == "__main__":
    create_nodes()
    create_edges()
    draw_map()