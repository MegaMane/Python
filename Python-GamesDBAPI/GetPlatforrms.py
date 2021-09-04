import requests
import json


""""

http://jonathansoma.com/lede/foundations-2018/classes/apis/multiple-pages-of-data-from-apis/

my_details = {
    'name': 'John Doe',
    'age': 29
}

with open('personal.json', 'w') as json_file:
    json.dump(my_details, json_file)

"""

response = requests.get("http://api.thegamesdb.net/v1/Platforms?apikey=a94068d9ef3e220c798a35644136368664b13ded607779d7f48050da7bc504c1&fields=icon,console,controller,developer,manufacturer,media,cpu,memory,graphics,sound,maxcontrollers,display,overview")
data = response.json()
print(data.keys())
print(data['data']['count'])

with open(r'\\MSPIGGY\PiggyShare\import\Platforms.json', 'w') as json_file:
    json.dump(data, json_file)
