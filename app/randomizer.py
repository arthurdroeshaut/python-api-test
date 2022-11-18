
from fastapi import FastAPI
from pydantic import BaseModel
import random


app = FastAPI()
class voetbalspeler(BaseModel):
    volledige_naam: int
    achternaam: int
    ploeg: str
    nationaliteit: str
    positie: str
    leeftijd: int


alle_voetballers = [ "Cristiano"," " "Messi", " " "Ibrahimovic", " " "Hazard", " " "Neymar", " " "Reus"]
alle_ploegen = [ "Manchester United," "Paris Saint German", "FC Barcelona","Borrusia Dortmund", "Real Madrid"]
alle_nationaliteiten = ["Argentijns", "Portugees", "Zweeds", "Braziliaans","Duits", "Belgisch"]
alle_posities = ["Doelman", "Verdediger", "Middenvelder", "Aanvaller"]

#geeft meer info weer over ronaldo om deze later op te vragen
voetballer_Ronaldo = {
    "voornaam": "Cristiano",
    "achternaam": "Ronaldo",
    "ploeg": "Manchester United",
    "nationaliteit": "Portugees",
    "positie": "aanvaller",
    "leeftijd": 37,
}
#geeft meer info weer over messi om deze later op te vragen
voetballer_Messi = {
    "voornaam": "Lionel",
    "achternaam": "Messi",
    "ploeg": "Paris Saint German",
    "nationaliteit": "Argentijns",
    "positie": "aanvaller",
    "leeftijd": 35,
}


#ik wil eerst een random voetballer opvragen
@app.get("/voetballer")
async def get_item():
    return random.alle_voetballers

#nu wil ik een lijst opvragen met extra info over de speler "Ronaldo"
@app.get("/voetballer/Ronaldo")
async def get_item():
    return voetballer_Ronaldo

#nu wil ik een lijst opvragen met extra info over de speler "Messi"
@app.get("/voetballer/Messi")
async def get_item():
    return voetballer_Messi

