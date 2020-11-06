import os
import reverse_geocoder as rg
# import NodeClass

class NodeClass:
    # id = 0
    #x_coord = 0
    #y_coord = 0
    def __init__(self, idV, x_coord, y_coord):
        self.idV = idV
        self.x_coord = x_coord
        self.y_coord = y_coord

path = os.path.dirname(__file__)
x = os.path.join(path,"Gowalla_totalCheckins.txt")

nlist = []
xCord = 0
yCord = 0

f = open(x, "r")
for i in f:
    j = i.split()
    idVar = j[0]
    xCord = j[3]
    yCord = j[4]
    #print(checkin_set)
    #twod_array[i] = checkin_set
    node = NodeClass(idVar, xCord, yCord)

# set boundaries for lat and long
# dont include outside boundries
# boundaries set for outside the US
# with geocoder take out all non US countries
# in geocoder this is the 'cc' field
# create new file .csv format w/ pandas