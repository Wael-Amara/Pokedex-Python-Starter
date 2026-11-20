import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0]) 
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
for pokemon in range(len(data)):
     print (data[pokemon]["name"]) 
# Add a language choice feature and print the pokemons name based on the user input
def poke_lang():
     global language
     language = input('what language do u want (english, japanese, chinese, or french) - ')
     for pokemon in range(len(data)):
          print (data[pokemon]["name"][language])
poke_lang() 
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
def poke_type():
     pokemon_type = input('What typ of pokemon do u like - ')
     for item in (data):
          if pokemon_type.title() in item['type']:
               print(item['name'][language])
poke_type() 
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
pokemon_search = input('search for pokemon (Ex. if "Char" return Charmander, Charmeleon and Charizard) - ')
pokemon_search = pokemon_search.lower()
x = []
found = False
for pokemon in data:
     poke_name = pokemon['name'][language].lower()
     if pokemon_search in poke_name:
          x.append(pokemon['name'][language])
          found = True
if not found:
     print("No Pokemon found")
if not not found:
     print(x) 
#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
