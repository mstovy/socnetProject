import networkx as nx
from mpl_toolkits.basemap import Basemap

def read_gowalla_checkins(listNodes):
    with open("Gowalla_totalCheckins.txt") as checkins:
        for i in checkins:
            print(i)

if __name__ == "__main__":
    a = []
    read_gowalla_checkins(a)