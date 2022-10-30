from asyncio.windows_events import NULL
from msilib.schema import Error
from typing import List
from fastapi import FastAPI, HTTPException  
import uvicorn
import requests
import json
import db_manager
from pokemon import Pokemon
from trainer import Trainer

app = FastAPI()


@app.get("/pokemons/{pokemon_name}")
async def get_pokemon(pokemon_name):
    try:
        # update types
        res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
        pokemon = json.loads(res.text)
        json_types = pokemon["types"]
        pokemon_id = pokemon["id"]
        types = []
        for type in json_types:
            types.append(f'("{type["type"]["name"]}", {pokemon_id})')
        db_manager.insert_pokemons_types(types)
        return db_manager.get_pokemon_by_id(pokemon_id)
    except Exception as e:
        raise HTTPException(status_code = 400, detail="Bad Request - pokemon name does not exist")


# todo filter with trainer_name and pokemon_type
@app.get("/trainers", status_code = 200)
async def get_pokemons_by_trainer_or_type(trainer_name=NULL, pokemon_type=NULL):
    if trainer_name and pokemon_type:
        return db_manager.get_pokemons_by_types_and_trainer(trainer_name, pokemon_type)
    if trainer_name:
        return db_manager.find_roster(trainer_name)
    elif pokemon_type:
        return db_manager.pokemons_by_type(pokemon_type)
    else:
        raise HTTPException(status_code = 400, detail="Bad Request - trainer_name and pokemon_type are NULL")


@app.get("/trainers", status_code = 200)
async def get_trainers_of_pokemon(pokemon_name):
    try:
        return db_manager.find_owners(pokemon_name)
    except:
        raise HTTPException(status_code = 400, detail="Bad Request - pokemon_name does not exist")


@app.post("/pokemons", status_code= 201)
async def add_pokemon(pokemons: List[Pokemon]):
    try:
        for pokemon in pokemons:
            pokemon_types = []
            db_manager.insert_pokemons(
                [f'({pokemon.id}, "{pokemon.name}",{pokemon.height},{pokemon.weight})'])
            for type in pokemon.types:
                pokemon_types.append(f'("{type}", {pokemon.id})')
            db_manager.insert_pokemons_types(pokemon_types)
            pokemon_trainers = []
            for trainer in pokemon.trainers:
                pokemon_trainers.append(f'({pokemon.id}, "{trainer}")')
            db_manager.insert_pokemons_trainers(pokemon_trainers)
    except:
        raise HTTPException(status_code = 500, detail="DB Error - add_pokemon")



@app.post("/trainers", status_code= 201)
async def add_trainers(trainers: List[Trainer]):
    try:
        for trainer in trainers:
            db_manager.insert_trainers([f'("{trainer.name}", "{trainer.town}")'])
    except:
        raise HTTPException(status_code = 500, detail="DB Error - add_trainers")



@app.delete("/pokemons/{pokemon_id}/trainers/{trainer_name}")
async def delete_pokemon_of_trainer(pokemon_id, trainer_name):
    try:
        return db_manager.delete_pokemon_of_trainer(pokemon_id, trainer_name)
    except:
        raise HTTPException(status_code = 500, detail="DB Error - delete_pokemon_of_trainer")

# maybe need to pass the parameters throw the body?


@app.patch("/pokemons/evolve")
async def pokemon_evolve(pokemon_id, pokemon_name, trainer_name):
    try:
        res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
        species_url = json.loads(res.text)["species"]["url"]
        res = requests.get(species_url)
        evolution_chain_url = json.loads(res.text)["evolution_chain"]["url"]
        res = requests.get(evolution_chain_url)
        evolution_chain = json.loads(res.text)["chain"]
        evolve_pokemon_name = ''
        while evolution_chain["species"]['name'] != pokemon_name and len(evolution_chain['evolves_to']):
            evolution_chain = evolution_chain['evolves_to'][0]
        if len(evolution_chain['evolves_to']):
            evolution_chain = evolution_chain['evolves_to'][0]
            evolve_pokemon_name = evolution_chain["species"]['name']
            res = requests.get(
                f'https://pokeapi.co/api/v2/pokemon/{evolve_pokemon_name}')
            new_pokemon_id = json.loads(res.text)["id"]
            db_manager.evolve_pokemon_of_trainer(
                pokemon_id, new_pokemon_id, trainer_name)
        return evolve_pokemon_name
    except:
        raise HTTPException(status_code = 400, detail="Bad Request - pokemon_id / pokemon_name / trainer_name does not exist")


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
