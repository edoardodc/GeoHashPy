import json
import requests

<<<<<<< HEAD
g = geocoder.ip('199.7.157.0')

print(g = geocoder.ip('me'))
print(g.latlng)
=======
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
>>>>>>> 0f9695584a3b0e72700bbfd4923d380ac39e474a
