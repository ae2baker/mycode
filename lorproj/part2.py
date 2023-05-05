#!/usr/bin/python3

import requests

url= "http://127.0.0.1:2224/api/characters" # grab the http address in the flask output, put that here- have the /endpoint that returns json data (/characters ?)

response= requests.get(url).json()

character_data = []
for character in response['characters']:
    character_data = {
        'name': character['name'],
        'race': character['race'],
        'gender': character['gender'],
        'birth': character['birth'],
        'death': character['death'],
        'realm': character['realm']
    }
    character_data.append(character_data)

# Print the character data
for character in character_data:
    print(f"Name: {character['name']}")
    print(f"Race: {character['race']}")
    print(f"Gender: {character['gender']}")
    print(f"Birth: {character['birth']}")
    print(f"Death: {character['death']}")
    print(f"Realm: {character['realm']}")
    print("")

# this just prints out the data; you'll want to add a for loop and perhaps print each character in a nice fashion
#print(response)
