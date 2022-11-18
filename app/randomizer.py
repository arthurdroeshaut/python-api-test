
from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class StarWars(BaseModel):
    Star_Wars_Character: str
    Lightsaber_Color: str
    Birthplace: str | None = None
    Species: str
    Rank : str | None = None
    Ship: str |None = None
    
    
    
Star_Wars_Characters = [ "Anakin Skywalker", "Darth Vader", "Chewbacca", "Han Solo", "Obi-Wan-Kenobi", "Leia Organa", "Ahsoka Tano", "R2D2"],
Lightsaber_Colors = [ "Green", "Blue", "red","Purple", "White", "Yellow", "Black"],
Birthplace = ["Coruscant", "Naboo", "Batuu", "Tattooine","Kashyyyk", "Cato Neimoidia"],
Species = ["Human", "Jawa", "Ewok", "Wookie", "Gungan", "Rodian", "Kaminoan"],
Rank = ["Youngling", "Padawan", "Jedi Knight", "Jedi Master", "Sith Acolyte","Sith Master", "Sith Lord", "Dark Council", "Jedi Grand Master",],
Ship = ["Millenium Falcon", "Death Star", "Star Destroyer","Slave 1", "TIE fighter", "X-Wing", "Starfighter" ]



#ik wil eerst een random star wars karakter opvragen
@app.get("/starwars/characters")
async def get_item():
    return random.choice[Star_Wars_Characters]



