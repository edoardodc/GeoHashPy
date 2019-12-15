import json
import pygeohash as pgh

count = 0
latitude = 0.00
longitude = 0.00
geoHash = ''

with open('data.json', 'r') as outfile:
    data = json.load(outfile)
    for element in data:
        count += 1
        print(count)
        element.pop('properties', None)
        element.pop('type', None)
        element.pop('id', None)
        
        geometry = element['geometry']
        for el in list(geometry):
            
            coordinate = geometry['coordinates']
            latitude = coordinate[0]
            longitude = coordinate[1]

        print(latitude)
        print(longitude)
        element.pop('geometry', None)

        l =  {'l': [latitude, longitude]}
        print(l)
        element.update(l)

        geoHash = pgh.encode(latitude, longitude, precision = 10)

        geoHash = {'g': geoHash}
        element.update(geoHash)

            #if el == 'type':
                #del geometry['type']
           
            


        
        

        
with open('new.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)





