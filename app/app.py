from fastapi import FastAPI

app = FastAPI()

my_song = {'artist': 'Against The Current', 'title': 'Weapon'}
neighbour_song = {'artist': 'The Corrs', 'title': 'Breathless'}

@app.get("/song/me")
async def get_my_song():
    return my_song

@app.get("/song/neighbour")
async def get_neighbour_song():
    return neighbour_song