from fastapi import APIRouter
from models.trainer import Trainer as trainer_model
from models.pokemon import Pokemon as pokemon_model
from fastapi import status
from pokemons_api import Pokemons_API
from fastapi.responses import JSONResponse


router = APIRouter()
pokemon_API = Pokemons_API()


@router.patch("/pokemons/evolve/{trainer_name}/{pokemon_name}", status_code=status.HTTP_200_OK)
async def pokemon_evolve(pokemon_name, trainer_name):
    try:
        pokemon_evolotion = pokemon_API.get_evolve(pokemon_name)
        pokemon_id = pokemon_model.get_id(pokemon_name)
        trainer_model.evolve_pokemon_of_trainer(
            pokemon_id, pokemon_evolotion.id, trainer_name)
        return pokemon_evolotion
    except Exception as e:
        return JSONResponse({"Error": e},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
