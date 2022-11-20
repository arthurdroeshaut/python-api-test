from fastapi import FastAPI, Query
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
    star_wars_character: str
    lightsaber_color: str or None = None
    birthplace: str
    species: str
    rank: str or None = None
    ship: str or None = None


# lijsten voor op te vragen in de api
star_wars_characters = ["Anakin Skywalker", "Darth Vader", "Chewbacca", "Han Solo", "Obi-Wan-Kenobi", "Leia Organa",
                        "Ahsoka Tano", "R2D2"]
lightsaber_colors = ["Green", "Blue", "red", "Purple", "White", "Yellow", "Black"]
birthplaces = ["Coruscant", "Naboo", "Batuu", "Tattooine", "Kashyyyk", "Cato Neimoidia", "unknown"]
species = ["Human", "Jawa", "Ewok", "Wookie", "Gungan", "Rodian", "Kaminoan"]
ranks = ["Youngling", "Padawan", "Jedi Knight", "Jedi Master", "Sith Acolyte", "Sith Master", "Sith Lord",
         "Dark Council", "Jedi Grand Master"]
ships = ["Millenium Falcon", "Death Star", "Star Destroyer", "Slave 1", "TIE fighter", "X-Wing", "Starfighter"]

Character_Luke = {
            "id": 1,
            "Star_Wars_Character": "Luke Skywalker",
            "Lightsaber_color": "Green",
            "Species": "Human",
            "Rank": "Jedi Knight",
            "Ship": "X-Wing",
      },
Character_Vader = {
            "id": 2,
            "Star_Wars_Character": "Darth Vader",
            "Lightsaber_color": "Red",
            "Species": "Human",
            "Rank": "Jedi-Master",
            "Ship": "Death Star",
      },


# ik wil eerst een random StarWars Character opvragen als "eerste get request"
@app.get("/StarWars/Characters")
async def get_item():
    return random.choice(star_wars_characters)


# ik wil hierna een random LightSaberColor uit de lijst opvragen. "als 2e get request)
@app.get("/StarWars/Characters/LightsaberColor")
async def get_items():
    return random.choice(lightsaber_colors)


# hierna een random Birthplace (dit is grotendeels om te zien of dit werkt) en voor in de website
@app.get("/StarWars/Characters/Birthplace")
async def get_items():
    return random.choice(birthplaces)


# hierna een random Species (dit is grotendeels om te zien of dit werkt) en voor in de website
@app.get("/StarWars/Characters/Species")
async def get_items():
    return random.choice(species)


# hierna een random Rank (dit is grotendeels om te zien of dit werkt) en voor in de website
@app.get("/StarWars/Characters/Rank")
async def get_items():
    return random.choice(ranks)


# hierna een random Ship (dit is grotendeels om te zien of dit werkt) en voor in de website
@app.get("/StarWars/Characters/Ship")
async def get_items():
    return random.choice(ships)


# dit is mijn post, hiermee kun je zelf gegevens ingeven per categorie en worden deze weergegeven op de website.
@app.post("/StarWars/CreateYourOwn")
async def create_character(starwars: StarWars):
    star_wars_characters.append(starwars.star_wars_character)
    species.append(starwars.species)
    birthplaces.append(starwars.birthplace)
    if starwars.lightsaber_color:
        lightsaber_colors.append(starwars.lightsaber_color)
    if starwars.rank:
        ranks.append(starwars.rank)
    if starwars.ship:
        ships.append(starwars.ship)
    return starwars




