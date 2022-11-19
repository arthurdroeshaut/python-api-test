from fastapi import FastAPI
from pydantic import BaseModel
from random import randint
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "https://localhost.tiangolo.com",
    "http://127.0.0.1:5500",
    "https://arthurdroeshaut.github.io"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
Birthplaces = ["Coruscant", "Naboo", "Batuu", "Tattooine", "Kashyyyk", "Cato Neimoidia", "unknown"]
Species = ["Human", "Jawa", "Ewok", "Wookie", "Gungan", "Rodian", "Kaminoan"]
Ranks = ["Youngling", "Padawan", "Jedi Knight", "Jedi Master", "Sith Acolyte", "Sith Master", "Sith Lord",
         "Dark Council", "Jedi Grand Master"]
Ships = ["Millenium Falcon", "Death Star", "Star Destroyer", "Slave 1", "TIE fighter", "X-Wing", "Starfighter"]


# ik wil eerst een random star wars karakter opvragen als "eerste get request"
@app.get("/StarWars/Characters")
async def get_item():
    return random.choice(Star_Wars_Characters)


# ik wil hierna een random LightSaber uit de lijst opvragen.
@app.get("/StarWars/Characters/LightsaberColor")
async def get_items():
    return random.choice(Lightsaber_Colors)


# hierna een random geboorteplaats (dit is grotendeels om te zien of dit werkt
@app.get("/StarWars/Characters/Birthplace")
async def get_items():
    return random.choice(Birthplaces)


@app.get("/StarWars/Characters/Species")
async def get_items():
    return random.choice(Species)


@app.get("/StarWars/Characters/Rank")
async def get_items():
    return random.choice(Ranks)


@app.get("/StarWars/Characters/Ship")
async def get_items():
    return random.choice(Ships)


@app.get("/StarWars/Characters/All")
async def get_item():
    return Star_Wars_Characters


@app.post("/StarWars/CreateYourOwn")
async def create_character(starwars: dict):
    Star_Wars_Characters.append(starwars.Star_Wars_Character)
    Species.append(starwars.Specie)
    Birthplaces.append(starwars.Birthplace)
    if starwars.Lightsaber_Color:
        Lightsaber_Colors.append(starwars.Lightsaber_Color)
    if starwars.Rank:
        Ranks.append(starwars.Rank)
    if starwars.Ship:
        Ships.append(starwars.Ship)
    return starwars
