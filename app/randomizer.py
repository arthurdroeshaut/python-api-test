
from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()
class BusinessCard(BaseModel):
    first_name: str
    last_name: str
    street: str
    number: str = Field(max_length=10)
    addition: str | None = None
    zip: int
    city: str
business_card_brent = {
    "first_name": "Brent",
    "last_name": "Pulmans",
    "street": "Kleinhoefstraat",
    "number": "4",
    "zip": 2440,
    "city": "Geel"
}
cards = {0: business_card_brent}
@app.post("/cards")
async def create_item(card: BusinessCard):
    new_key = max(cards, key=cards.get)+1
    cards[new_key] = card
    return cards[new_key]
@app.get("/cards")
async def get_item():
    return cards
@app.put("/cards/{id}")
async def get_item(id: int, card: BusinessCard):
    cards[id] = card
    return cards[id]
