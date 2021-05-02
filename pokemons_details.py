import json
import csv
import requests

i=1
count=1
pokeid_limit = 1118
while i < pokeid_limit+1:
    url2 = "https://pokeapi.co/api/v2/pokemon/"+str(count)
    r = requests.get(url2)
    if r.status_code == 200:
        data = r.json()
        pokeid = data['id']
        pokename = data['name']
        pokeweight = data['weight']
        pokeheight = data['height']
        pokestats = data['stats']
        pokebase = 0
        for statnumber in pokestats:
            pokestatdetail=statnumber['stat']
            checkstat = (str(pokestatdetail).split(':')[1]).split(',')[0]
            test = checkstat.strip()
            if test=="'hp'":
                pokebase=statnumber['base_stat']
        
        if i==1:
            pokelist = {
                pokeid : {
                "pokename" : pokename,
                "pokeweight" : pokeweight,
                "pokeheight" : pokeheight,
                "poke_hp" : pokebase
                }
            }
        elif i>1:
            pokelist[pokeid] = {}
            pokelist[pokeid].update({"pokename" : pokename,"pokeweight" : pokeweight,"pokeheight" : pokeheight,"poke_hp" : pokebase})
        i += 1
        count +=1
    elif r.status_code == 404 and count == 899:
        print('Not Found.')
        count += 9102
    elif r.status_code == 404 and count != 899:
        print('Not Found.')
        count += 1
    else:
        print('I dunno.')
        count += 1


with open('pokefile_details.csv', mode='w', newline='') as pokefile:
    fieldnames = ['id', 'name', 'weight', 'height', 'base_hp']
    writer = csv.DictWriter(pokefile, fieldnames=fieldnames)

    writer.writeheader()

    for _id in pokelist:
        namestr = pokelist[_id]
        print(namestr)
        for data in namestr:
            if str(data)=='pokename':
                name = namestr[data]
            elif str(data)=='pokeweight':
                weight = namestr[data]
            elif str(data)=='pokeheight':
                height = namestr[data]
            elif str(data)=='poke_hp':
                base_hp = namestr[data]
        writer.writerow({'id': _id, 'name': name, 'weight': weight,'height': height,'base_hp': base_hp})
    