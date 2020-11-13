import networkx as nx
import pandas as pd
from mpl_toolkits.basemap import Basemap

path = os.path.dirname(__file__)
checkin_file_path = os.path.join(path, "gowalla_checkins_average.csv")
df = pd.read_csv(checkin_file_path)

def create_nodes():
    

if __name__ == "__main__":
    a = []
    read_gowalla_checkins(a)