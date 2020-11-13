import os
import pandas as pd

top = 49.3457868 # north lat
left = -124.7844079 # west long
right = -66.9513812 # east long
bottom =  24.7433195 # south lat

# path = os.path.dirname(__file__)
path = "/Users/henry/Documents/School/Fall 2020/CSCI 5800/"
checkin_file_path = os.path.join(path, "Gowalla_totalCheckins.txt")

node_dict = {
    "UserID": [],
    "Latitude": [],
    "Longitude": []
    }


def read_checkin_file_generator():
    with open(checkin_file_path) as file:
        for line in file:
            yield line

def check_node_is_in_us(latitude, longitude):
    inside_lat = bottom <= latitude and latitude <= top
    inside_long = left <= longitude and longitude <= right
    response = False
    if inside_lat and inside_long:
        response = True
    return response

def add_nodes_if_in_us():
    for line in read_checkin_file_generator():
        line_split = line.split()
        latitude = float(line_split[2])
        longitude = float(line_split[3])
        node_in_us = check_node_is_in_us(latitude, longitude)
        if node_in_us:
            user_id = line_split[0]
            node_dict["UserID"].append(user_id)
            node_dict["Latitude"].append(latitude)
            node_dict["Longitude"].append(longitude)

def write_to_csv(nodes):
    df = pd.DataFrame.from_dict(nodes)
    df.to_csv("gowalla_checkins_usa_only.csv", index=False)

if __name__ == "__main__":
    add_nodes_if_in_us()
    write_to_csv(node_dict)