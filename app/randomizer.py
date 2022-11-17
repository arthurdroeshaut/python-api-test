
from fastapi import FastAPI, Query
from random import randint
app = FastAPI()
all_animals = ["badger", "lion", "wolf", "porcupine", "cheetah", "giraffe", 
"panda", "gorilla", "tiger", "koala", "jaguar", "elephant", "blue-and-yellow macaw", "hornbill", "rhinoceros", "kangaroo", "ostridge", "bison", "wallaby"]
@app.get("/zoo")
async def root(number: int = Query(default=5, gt=0, description='This parameter' 
indicates how many animals should be returned by the API. The sex for each animal 
will be determined randomly.')):



    zoo_animals = []
    for i in range(number):
        if randint(0,1) == 0:
            sex = "male"
        else:
            sex = "female"
        new_animal = {'number': i+1, 'species': all_animals[randint(0, 
len(all_animals)-1)], 'sex': sex}
        zoo_animals.append(new_animal)
    return {"animals": zoo_animals}
