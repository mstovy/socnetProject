import networkx as nx
import pandas as pd
from mpl_toolkits.basemap import Basemap

path = os.path.dirname(__file__)
checkin_file_path = os.path.join(path, "gowalla_checkins_average.csv")
df = pd.read_csv(checkin_file_path)
edges_file_path = os.path.join(path, "Gowalla_edges.txt")
graph = nx.Graph()

def create_nodes():
    for index, row in df.iterrows():
        graph.add_node(row['UserID'], pos(row['Latitude'], row['Longitude']))

def create_edges():
    for index, row 

if __name__ == "__main__":
    create_nodes()