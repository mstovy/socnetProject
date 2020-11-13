import os
import pandas as pd
from Node import *

path = "/Users/henry/Documents/School/Fall 2020/CSCI 5800/"
checkin_file_path = os.path.join(path, "gowalla_checkins_usa_only.csv")

df = pd.read_csv(checkin_file_path)

user_ids = df['UserID'].unique()

outliers = []

def remove_geocode_outliers():
    average_lat = 0
    average_long = 0

    for user_id in user_ids:
        average_lat = df.loc[df['UserID'] == user_id ]['Latitude'].mean()
        average_long = df.loc[df['UserID'] == user_id ]['Longitude'].mean()
        user_df = df.loc[df['UserID'] == user_id]
    
        for index, row in user_df.iterrows():
            latitude = row['Latitude']
            longitude = row['Longitude']

            lat_diff = abs(average_lat - latitude)
            long_diff = abs(average_long - longitude)

            if lat_diff > 5 or long_diff > 5:
                outliers.append(index)
    
        

if __name__ == "__main__":
    remove_geocode_outliers()
    df = df.drop(outliers)
    df.to_csv('gowalla_us_only_no_outliers.csv', index=False)
