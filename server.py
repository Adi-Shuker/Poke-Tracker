from fastapi import FastAPI
import uvicorn
import requests
import json
import db_manager

app = FastAPI()


@app.get("/pokemon/types")
async def get_pokemon_types(name):
    res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    json_types = json.loads(res.text)["types"]
    types = []
    for type in json_types:
        types.append(type["type"]["name"])
    return types


@app.get("/pokemons")
async def get_pokemons_by_trainer(owner):
    return []


@app.get("/trainers")
async def get_trainers_of_pokemon(pokemon):
    return []


@app.post("/pokemons")
async def add_pokemons(name):
    db_manager.insert_trainers([])
    x = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    print(x)
    return


# @app.post("")
# async def add_types():
#     return


# @app.post("")
# async def add_trainers():
#     return


# @app.post("")
# async def add_pokemons_trainers():
#     return


# @app.post("")
# async def add_pokemons_types():
#     return

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
