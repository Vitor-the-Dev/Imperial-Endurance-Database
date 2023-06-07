import requests
import json

def find_endurance(consumables):
#Finds a ship's endurance (how many hours it can stay in FTL) by finding how many hours until it's consumables run out
    consumables = consumables.split(' ')
    hours = {'years': 8760, 'year': 8760,
             'months': 730, 'month': 730,
             'week': 168, 'weeks': 168, 
             'days': 24, 'day': 24, 'unknow':-1,}
    

    if len(consumables) == 2:
        if hours[consumables[1]] == -1:
            return -1
        elif consumables[0] != 'unknown':
            return int(consumables[0]) * hours[consumables[1]]
        else:
            return -1
    else:
        return -1
    #Input sanity check

def find_stops(distance):
    starships = requests.get('https://www.swapi.tech/api/starships/')
    starships = json.loads(starships.text)
    #HTTP request to swapi to get all starships, subsequently loading them as a json
    
    starships_list = []
    while starships['next'] != None: 
        for item in starships['results']:
            ship = requests.get(item['url'])
            #Gets http request for each starship properties and get a new ship response with the data of our ships

            ship_json = json.loads(ship.text)
            starships_list.append(ship_json['result']['properties'])
            #Adds the HTTP request to the ship's stats into our ship_json list
        starships = requests.get(starships['next'])
        starships = json.loads(starships.text)

    ships_stops = []
    
    for item in starships_list:
        endurance = find_endurance(item['consumables']) 
        if endurance == 'unknown' or item['MGLT'] == 'unknown':
            stops = 'unknown'
        #Logic to determine whether endurance or MGLT rating are known or unknown

        else:
            stops = int(distance/(int(item['MGLT']) * endurance))
        #finds range of our ship will be required to make by multiplying endurance (in hours) to speed (in Megalights per hour)
        #divides distance/range to find how many stops we will need to make 


        final_ship_stats = str(item['name'] + ': ' + str(stops))
        ships_stops.append(final_ship_stats)
    
    print('Admiral, we estimate these ship models will require this ammount of stops considering their capacity for supplies')
    for item in ships_stops:
        print(item)