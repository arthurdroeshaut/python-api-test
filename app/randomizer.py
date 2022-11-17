
from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()
class voetbalspeler(BaseModel):
    voornaam: str
    achternaam: str
    ploeg: str
    nationaliteit: str
    positie: str
    leeftijd: int


alle_voetballers = [ "Cristiano" "Messi" "Mbappe" "Hazard" "De Bruyne" "Neymar" "Reus"]

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


#ik wil eerst een lijst opvragen van alle mogelijke spelers
@app.get("/voetballer")
async def get_item():
    return alle_voetballers

#nu wil ik een lijst opvragen met extra info over de speler "Ronaldo"
@app.get("/voetballer/Ronaldo")
async def get_item():
    return voetballer_Ronaldo

#nu wil ik een lijst opvragen met extra info over de speler "Messi"
@app.get("/voetballer/Messi")
async def get_item():
    return voetballer_Messi

