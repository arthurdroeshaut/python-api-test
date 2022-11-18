
from fastapi import FastAPI
from pydantic import BaseModel
import random


app = FastAPI()
class StarWars(BaseModel):
    

    star_wars_characters = [ "Anakin Skywalker", "Darth Vader", "Chewbacca", "Han Solo", "Obi-Wan-Kenobi", "Leia Organa", "Ahsoka Tano", "R2D2"]
    Lightsaber_Colors = [ "Green," "Blue", "red","Purple", "White", "Yellow", "Black"]
    Birthplace = ["Coruscant", "Naboo", "Batuu", "Tattooine","Kashyyyk", "Cato Neimoidia"]
    Species = ["Human", "Jawa", "Ewok", "Wookie", "Gungan", "Rodian", "Kaminoan"]
    Rank = ["Youngling", "Padawan", "Jedi Knight", "Jedi Master", "Sith Acolyte","Sith Master", "Sith Lord", "Dark Council", "Jedi Grand Master",]




#ik wil eerst een random voetballer opvragen
@app.get("/StarWars")
async def get_item():
    return random.choice(star_wars_characters)



