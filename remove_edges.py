import os
import pandas as pd

path = os.path.dirname(__file__)
checkin_file_path = os.path.join(path, "gowalla_checkins_average.csv")
edges_file_path = os.path.join(path, "Gowalla_edges.csv")

node_df = pd.read_csv(checkin_file_path)
edges_df = pd.read_csv(edges_file_path)

user_ids = node_df['UserID'].tolist()
edges_in_us = {
    'Source': [],
    'Destination': []
}

for index, row in edges_df.iterrows():
    if (row['Source'] in user_ids) and (row['Destination'] in user_ids):
        edges_in_us['Source'].append(row['Source'])
        edges_in_us['Destination'].append(row['Destination'])
    
df = pd.DataFrame.from_dict(edges_in_us, index=False)
df.to_csv('gowalla_edges_only_us.csv')
