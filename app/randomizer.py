
from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()
class voetbalspeler(BaseModel):
    voornaam: str
    achternaam: str
    nationaliteit: str
    positie: str
    leeftijd: int

alle_voetballers = [ "Cristiano", "Messi", "Mbappe", "Hazard", "De Bruyne", "Neymar", "Reus"]
    

voetballer_Ronaldo = {
    "voornaam": "Cristiano",
    "achternaam": "Ronaldo",
    "nationaliteit": "Portugees",
    "positie": "aanvaller",
    "leeftijd": 37,
}

voetballer_Messi = {
    "voornaam": "Lionel",
    "achternaam": "Messi",
    "nationaliteit": "Argentijns",
    "positie": "aanvaller",
    "leeftijd": 35,
}
spelers= {alle_voetballers}
speler = {1: voetballer_Ronaldo}
speler = {2: voetballer_Messi}
@app.post("/voetballer/Ronaldo")
async def create_item(voetballer: voetbalspeler):
    new_key = max(speler, key=voetballer.get)
    voetballer[new_key] = speler
    return voetballer[new_key]

@app.get("/voetballer")
async def get_item():
    return alle_voetballers

@app.get("/voetballer/Ronaldo")
async def get_item():
    return voetballer_Ronaldo

@app.get("/voetballer/Messi")
async def get_item():
    return voetballer_Messi

@app.put("/voetballer/{id}")
async def get_item(id: int, voetballer: voetbalspeler):
    voetballer[id] = speler
    return voetballer[id]
