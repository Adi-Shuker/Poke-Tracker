from typing import List
from fastapi import APIRouter
from fastapi import status
from pokemon import Pokemon
from models.pokemon import Pokemon as pokemon_model
from pokemons_api import Pokemons_API, ElementNotExistError
from fastapi.responses import JSONResponse


router = APIRouter()
pokemon_API = Pokemons_API()


@router.get("/pokemons/{pokemon_name}", status_code=status.HTTP_200_OK)
async def get_pokemon(pokemon_name):
    try:
        # update types
        pokemon = pokemon_API.get_pokemon(pokemon_name)
        types = []
        for type in pokemon.types:
            types.append(f'("{type}", {pokemon.id})')
        pokemon_model.insert_pokemons_types(types)
        return pokemon_model.get_pokemon_by_id(pokemon.id)
    except ElementNotExistError as e:
        return JSONResponse({"Error": "Pokemon does not exist"},
                            status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JSONResponse({"Error": e}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get("/pokemons", tags=["pokemons"], status_code=status.HTTP_200_OK)
async def get_pokemons_by_type(pokemon_type):
    try:
        return pokemon_model.pokemons_by_type(pokemon_type)
    except Exception as e:
        return JSONResponse({"Error": e},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.post("/pokemons", status_code=status.HTTP_201_CREATED)
async def add_pokemon(pokemons: List[Pokemon]):
    try:
        for pokemon in pokemons:
            pokemon_types = []
            pokemon_model.insert_pokemons(
                [f'({pokemon.id}, "{pokemon.name}",{pokemon.height},{pokemon.weight})'])
            for type in pokemon.types:
                pokemon_types.append(f'("{type}", {pokemon.id})')
            pokemon_model.insert_pokemons_types(pokemon_types)
            return {"status": "Success. Added pokemons"}
    except Exception as e:
        return JSONResponse({"Error": e},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
