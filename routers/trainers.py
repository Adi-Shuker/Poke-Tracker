from typing import List
from fastapi import APIRouter, status
from models.trainer import Trainer as trainer_model
from fastapi.responses import JSONResponse

from trainer import Trainer

router = APIRouter()


@router.get("/trainers/{trainer_name}/pokemons", status_code=status.HTTP_200_OK)
async def get_pokemons_by_trainer(trainer_name):
    try:
        return trainer_model.find_roster(trainer_name)
    except Exception as e:
        return JSONResponse({"Error": e},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get("/trainers", status_code=status.HTTP_200_OK)
async def get_trainers_of_pokemon(pokemon_name):
    try:
        return trainer_model.find_owners(pokemon_name)
    except Exception as e:
        return JSONResponse({"Error": e},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.post("/trainers", status_code=status.HTTP_201_CREATED)
async def add_trainers(trainers: List[Trainer]):
    try:
        for trainer in trainers:
            trainer_model.insert_trainers(
                [f'("{trainer.name}", "{trainer.town}")'])
    except Exception as e:
        return JSONResponse({"Error": e},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.delete("/trainers/{trainer_name}/pokemons/{pokemon_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pokemon_of_trainer(pokemon_id, trainer_name):
    try:
        return trainer_model.delete_pokemon_of_trainer(pokemon_id, trainer_name)
    except Exception as e:
        return JSONResponse({"Error": e},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
