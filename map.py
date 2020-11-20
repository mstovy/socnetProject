import pandas as pd
import os
import json
import numpy

path = os.path.dirname(__file__)
checkin_file_path = os.path.join(path, "gowalla_checkins_average.csv")
nodes_df = pd.read_csv(checkin_file_path)
edges_file_path = os.path.join(path, "gowalla_edges_only_us.csv")
edges_df = pd.read_csv(edges_file_path)
geocodes = {
    'SourceLat': [],
    'SourceLong': [],
    'DestLat': [],
    'DestLong': []
}

for index, row in edges_df.iterrows():
    source_long = pd.to_numeric(nodes_df.loc[nodes_df['UserID']==row['Source']]['Longitude']).to_numpy()[0]
    source_lat = pd.to_numeric(nodes_df.loc[nodes_df['UserID']==row['Source']]['Latitude']).to_numpy()[0]

    destination_long = pd.to_numeric(nodes_df.loc[nodes_df['UserID']==row['Destination']]['Longitude']).to_numpy()[0]
    destination_lat = pd.to_numeric(nodes_df.loc[nodes_df['UserID']==row['Destination']]['Latitude']).to_numpy()[0]
    geocode_entry = []

    geocodes['SourceLat'].append(source_lat)
    geocodes['SourceLong'].append(source_long)
    geocodes['DestLat'].append(destination_lat)
    geocodes['DestLong'].append(destination_long)

    # source = {"lat": source_lat, "long": source_long}
    # dest = {"lat": destination_lat, "long": destination_long}
    # geocode_entry.append(source)
    # geocode_entry.append(dest)
    # geocodes.append(geocode_entry)

df = pd.DataFrame.from_dict(geocodes)
df.to_csv("gowalla_edge_geocodes.csv", index=False)

    