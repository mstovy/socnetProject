import pandas as pd
import os
import networkx as nx

path = os.path.dirname(__file__)
checkin_file_path = os.path.join(path, "gowalla_checkins_average.csv")
nodes_df = pd.read_csv(checkin_file_path)
edges_file_path = os.path.join(path, "gowalla_removed_edges_1_2.csv")
edges_df = pd.read_csv(edges_file_path)
graph = nx.Graph()
geocodes = {
    'Latitude': [],
    'Longitude': [],
}

def create_nodes():
    for index, row in nodes_df.iterrows():
        graph.add_node(row['UserID'], pos=(row['Latitude'], row['Longitude']))

def create_edges():
    for index, row in edges_df.iterrows():
        graph.add_edge(row['Source'], row['Destination'])

def communities():
    communities = [community for community in nx.connected_components(graph) if len(community) > 5]
    communities.sort(key=len, reverse=True)
    return communities

def get_geocodes(node):
    node_long = pd.to_numeric(nodes_df.loc[nodes_df['UserID']==node]['Longitude']).to_numpy()[0]
    node_lat = pd.to_numeric(nodes_df.loc[nodes_df['UserID']==node]['Latitude']).to_numpy()[0]

    geocodes['Latitude'].append(node_lat)
    geocodes['Longitude'].append(node_long)

if __name__ == "__main__":
    create_nodes()
    create_edges()
    i = 0
    for community in communities():
        if i == 0:
            i+=1
            continue
        if i == 20:
            break
        for node in community:
            get_geocodes(node)
        i+=1

    df = pd.DataFrame.from_dict(geocodes)
    df.to_csv("large_community_geocodes.csv", index=False)

