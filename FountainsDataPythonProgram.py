#get data
import json

a = 0

with open('FountainData.json', 'r') as data_file:
    data = json.load(data_file)

for element in data:
    if 'id' in element:
         a = a + 1
         print(element['id'])
         print(a)
         del element['id']


with open('FountainData.json', 'w') as data_file:
    myData = json.dump(data, data_file, indent=4)

print('Finished!')
