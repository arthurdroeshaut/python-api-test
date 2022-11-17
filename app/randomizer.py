
from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()
class voetbalspeler(BaseModel):
    voornaam: str
    achternaam: str
    nationaliteit: str
    positie: str
    leeftijd: int

voetballer_Ronaldo = {
    "id": 1,
    "voornaam": "Cristiano",
    "achternaam": "Ronaldo",
    "nationaliteit": "Portugees",
    "positie": "aanvaller",
    "leeftijd": 37,
}
speler = {0: voetballer_Ronaldo}
@app.post("/voetballer")
async def create_item(voetballer: voetbalspeler):
    new_key = max(speler, key=voetballer.get)
    voetballer[new_key] = speler
    return voetballer[new_key]
@app.get("/voetballer")
async def get_item():
    return speler
@app.put("/voetballer/{id}")
async def get_item(id: int, voetballer: voetbalspeler):
    voetballer[id] = speler
    return voetballer[id]
