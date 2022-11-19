from fastapi import FastAPI
from pydantic import BaseModel
from random import randint
import random

app = FastAPI()


class StarWars(BaseModel):
    Star_Wars_Character: str
    Lightsaber_Color: str or None = None
    Birthplace: str
    Specie: str
    Rank: str or None = None
    Ship: str or None = None


# lijsten voor op te vragen in de api
Star_Wars_Characters = ["Anakin Skywalker", "Darth Vader", "Chewbacca", "Han Solo", "Obi-Wan-Kenobi", "Leia Organa",
                        "Ahsoka Tano", "R2D2"]
Lightsaber_Colors = ["Green", "Blue", "red", "Purple", "White", "Yellow", "Black"]
Birthplaces = ["Coruscant", "Naboo", "Batuu", "Tattooine", "Kashyyyk", "Cato Neimoidia"]
Species = ["Human", "Jawa", "Ewok", "Wookie", "Gungan", "Rodian", "Kaminoan"]
Ranks = ["Youngling", "Padawan", "Jedi Knight", "Jedi Master", "Sith Acolyte", "Sith Master", "Sith Lord",
         "Dark Council"
    , "Jedi Grand Master", ]
Ships = ["Millenium Falcon", "Death Star", "Star Destroyer", "Slave 1", "TIE fighter", "X-Wing", "Starfighter"]


# ik wil eerst een random star wars karakter opvragen als "eerste get request"
@app.get("/StarWars/Characters")
async def get_item():
    return random.choice(Star_Wars_Characters)


@app.get("/StarWars/Characters/CreateRandom")
async def get_items():
    return random.choice(Star_Wars_Characters + Lightsaber_Colors + Birthplaces + Species + Ranks + Ships)
