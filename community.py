import pandas as pd
import os
import networkx as nx

path = os.path.dirname(__file__)
checkin_file_path = os.path.join(path, "gowalla_checkins_average.csv")
nodes_df = pd.read_csv(checkin_file_path)
edges_file_path = os.path.join(path, "gowalla_removed_edges_1_5.csv")
edges_df = pd.read_csv(edges_file_path)
graph = nx.Graph()

def create_nodes():
    for index, row in nodes_df.iterrows():
        graph.add_node(row['UserID'], pos=(row['Latitude'], row['Longitude']))

def create_edges():
    for index, row in edges_df.iterrows():
        graph.add_edge(row['Source'], row['Destination'])

def communities():
    response = [community for community in nx.connected_components(graph) if len(community) > 1]
    return response

if __name__ == "__main__":
    create_nodes()
    create_edges()
    for community in communities():
        print(community)

