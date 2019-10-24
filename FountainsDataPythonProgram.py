import json
import pygeohash as pgh


print(pgh.encode(19.4354778, -99.1364789, precision = 10))

with open('SmallData.json', 'r') as outfile:
    data = json.load(outfile)
    for element in data:
        latitude = element["l"][0]
        longitude = element["l"][1]
        geoHash = pgh.encode(latitude, longitude, precision = 10)
        print(geoHash)
        element["g"] = geoHash
        
with open('SmallData.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)



print(data)
