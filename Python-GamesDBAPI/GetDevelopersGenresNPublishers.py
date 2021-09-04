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

endpoints = ['Developers','Genres','Publishers']

for endpoint in endpoints:

    response = requests.get("http://api.thegamesdb.net/v1/{}?apikey=a94068d9ef3e220c798a35644136368664b13ded607779d7f48050da7bc504c1".format(endpoint))
    data = response.json()
    print(data.keys())
    print(data['data']['count'])

    with open(r'\\MSPIGGY\PiggyShare\import\{}.json'.format(endpoint), 'w') as json_file:
        json.dump(data, json_file)
