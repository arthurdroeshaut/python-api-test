from fastapi import FastAPI
from pydantic import BaseModel
from random import randint
import random


app = FastAPI()


class StarWars(BaseModel):
    Star_Wars_Character: str
    Lightsaber_Color: str
    Birthplace: str
    Specie: str
    Rank: str
    Ship: str


# lijsten voor op te vragen in de api
Star_Wars_Characters = ["Anakin Skywalker", "Darth Vader", "Chewbacca", "Han Solo", "Obi-Wan-Kenobi", "Leia Organa",
                        "Ahsoka Tano", "R2D2"]
Lightsaber_Colors = ["Green", "Blue", "red", "Purple", "White", "Yellow", "Black"]
Birthplaces = ["Coruscant", "Naboo", "Batuu", "Tattooine", "Kashyyyk", "Cato Neimoidia"]
Species = ["Human", "Jawa", "Ewok", "Wookie", "Gungan", "Rodian", "Kaminoan"]
Ranks = ["Youngling", "Padawan", "Jedi Knight", "Jedi Master", "Sith Acolyte", "Sith Master", "Sith Lord", "Dark Council"
        ,"Jedi Grand Master", ]
Ships = ["Millenium Falcon", "Death Star", "Star Destroyer", "Slave 1", "TIE fighter", "X-Wing", "Starfighter"]


# print(Star_Wars_Characters)
# print(Lightsaber_Colors)
# print(Birthplace)
# print(Species)
# print(Rank)
# print(Ship)


# ik wil eerst een random star wars karakter opvragen als "eerste get request"
@app.get("/StarWars/Characters")
async def get_item():
    return random.choice(Star_Wars_Characters)



