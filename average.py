import os
import pandas as pd

path = "/Users/henry/Documents/School/Fall 2020/CSCI 5800/"
checkin_file_path = os.path.join(path, "gowalla_checkins_usa_only.csv")

df = pd.read_csv(checkin_file_path)

df.groupby(['UserID']).mean().to_csv('gowalla_checkins_average.csv')
