import json
import csv
import requests


pokeid_limit = 1118

i = 0

while i < pokeid_limit:

    r = requests.get('https://pokeapi.co/api/v2/pokemon/', params={'limit': '1','offset': i})
    if r.status_code == 200:
        data = r.json()
        pokeidstr = data['results'][0]
        pokeid = str(pokeidstr['url']).split('/')[6]
        pokename = pokeidstr['name']
        if i==0:
            pokelist = {
                pokeid: pokename,
            }
        else:
            pokelist[pokeid] = pokename
        i += 1
        print('Found '+str(i))
    elif r.status_code == 404:
        print('Not Found.')
        i += 1
    else:
        print('I dunno.')
        i += 1
        
        
with open('pokemons_list.csv', mode='w', newline='') as pokefile:
    fieldnames = ['id', 'name']
    writer = csv.DictWriter(pokefile, fieldnames=fieldnames)

    writer.writeheader()
    for _id in pokelist:
        name = pokelist[_id]
        writer.writerow({'id': _id, 'name': name})
    