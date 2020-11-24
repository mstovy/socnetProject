import networkx as nx
import pandas as pd
import os
import itertools

path = os.path.dirname(__file__)
checkin_file_path = os.path.join(path, "gowalla_checkins_average.csv")
nodes_df = pd.read_csv(checkin_file_path)
edges_file_path = os.path.join(path, "gowalla_removed_edges_1_5.csv")
edges_df = pd.read_csv(edges_file_path)
graph = nx.Graph()

class GirvanNewman:
    def __init__(self, graph):
        self.graph = graph
        self.edge_betweenness_dict = self.get_edge_betweenness()

    def get_edge_betweenness(self):
        """gets the edge betweenness in a graph and returns a dictionary {edge: betweenness}"""
        n = 1000
        response = nx.edge_betweenness_centrality(self.graph, k=n)
        return response
        # self.edge_betweenness_dict = response
    
    def get_max_betweenness(self):
        """gets the edges with max edge betweenness
        step 1 of Girvan Newman algorithm"""
        # self.get_edge_betweenness()
        max_betweenness = max(self.edge_betweenness_dict.values())
        return max_betweenness

    def remove_edge_with_max_betweenness(self):
        """removes the edge with max edge betweenness
        step 2 of Girvan Newman algorithm"""
        max_edge_betweenness = self.get_max_betweenness()
        for edge, edge_betweenness in self.edge_betweenness_dict.items():
            if edge_betweenness == max_edge_betweenness:
                self.graph.remove_edge(int(edge[0]), int(edge[1]))
                del self.edge_betweenness_dict[edge]
                return int(edge[0]), int(edge[1])

def create_nodes():
    for index, row in nodes_df.iterrows():
        graph.add_node(row['UserID'], pos=(row['Latitude'], row['Longitude']))
    

def create_edges():
    for index, row in edges_df.iterrows():
        graph.add_edge(row['Source'], row['Destination'])

if __name__ == "__main__":
    create_nodes()
    create_edges()
    girvan_newman = GirvanNewman(graph)
    edges_to_remove = []
    for i in range(0, 10000):
        try:
            edge_to_remove = girvan_newman.remove_edge_with_max_betweenness()
            row = edges_df.loc[(edges_df['Source']==edge_to_remove[0]) & (edges_df['Destination']==edge_to_remove[1])]
            if row.empty:
                row = edges_df.loc[(edges_df['Source']==edge_to_remove[1]) & (edges_df['Destination']==edge_to_remove[0])]
            row_index = row.index[0]
            edges_to_remove.append(row_index)
        except:
            pass
    edges_df = edges_df.drop(edges_to_remove)
    edges_df.to_csv('gowalla_removed_edges_1_5.csv', index=False)
    