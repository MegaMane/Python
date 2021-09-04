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

platforms = {
#6:"Super Nintendo (SNES)",
7:"Nintendo Entertainment System (NES)",
#18:"Sega Genesis",
#4971:"Nintendo Switch",
}

for platform in platforms.keys():
    #print ("id={}".format(platform))

    response = requests.get("http://api.thegamesdb.net/v1/Games/ByPlatformID?apikey=a94068d9ef3e220c798a35644136368664b13ded607779d7f48050da7bc504c1&id={}&fields=players,publishers,genres,overview,last_updated,rating,platform,coop,youtube,os,processor,ram,hdd,video,sound,alternates".format(platform))
    data = response.json()
    print(data.keys())
    print(data['data']['count'])

    with open(r'\\MSPIGGY\PiggyShare\import\Platform_{}.json'.format(platform), 'w') as json_file:
        json.dump(data, json_file)
        

