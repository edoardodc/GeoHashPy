import json

count = 0

with open('data.json', 'r') as outfile:
    data = json.load(outfile)
    myData = data["Fountains"]
    for element in myData:
        count += 1
        print(count)
        element.pop('properties', None)
        element.pop('type', None)
        element.pop('id', None)
        geometry = element['geometry']
        for el in list(geometry):
            if 'type' == el:
                del geometry['type']

        

        
with open('new.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)





