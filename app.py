import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
""" print(data[0]) """
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
""" for pokemon in range(len(data)):
     print (data[pokemon]["name"]) """
# Add a language choice feature and print the pokemons name based on the user input
language = input('what language do u want (english, japanese, chinese, or french) - ')
for pokemon in range(len(data)):
     print (data[pokemon]["name"][language])
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
y= input('what typ of pokemon do u wanna see - ')
print('')

print(data[pokemon]["type"])
for i in range(len(data)):
     print(data[i]["type"])
     if data[i]["type"] == y:
          print(data[i]["type"])

""" for pokemon in range(len(data)):
     z=[]
     pokemon == 0
     if data[pokemon]["type"][pokemon]==y:
          z.append(data[pokemon]['name'][language])
          z.append(data[pokemon+1]['name'][language])
          pokemon == 0
print(z) """
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
