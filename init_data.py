import json
from models.trainer import Trainer as trainer_model
from models.pokemon import Pokemon as pokemon_model

with open('data/poke_data.json', 'r') as data_file:
    json_data = data_file.read()
    poke_data = json.loads(json_data)
    pokemon_values = []
    types_values = []
    pokemon_type_values = []
    trainers_values = []
    pokemon_trainer_values = []
    for pokemon in poke_data:
        pokemon_id = pokemon.get("id")
        pokemon_name = pokemon.get("name")
        type = pokemon.get("type")
        height = pokemon.get("height")
        weight = pokemon.get("weight")
        pokemon_values.append(
            f'({pokemon_id}, "{pokemon_name}",{height},{weight})')
        types_values.append(f'("{type}")')
        pokemon_type_values.append(f'("{type}", {pokemon_id})')
        owned_by = pokemon.get("ownedBy")
        for trainer in owned_by:
            trainer_name = trainer.get('name')
            trainer_town = trainer.get('town')
            trainers_values.append(f'{trainer_name, trainer_town}')
            pokemon_trainer_values.append(f'({pokemon_id}, "{trainer_name}")')

    pokemon_model.insert_pokemons(pokemon_values)
    pokemon_model.insert_types(types_values)
    trainer_model.insert_trainers(trainers_values)
    pokemon_model.insert_pokemons_types(pokemon_type_values)
    trainer_model.insert_pokemons_trainers(pokemon_trainer_values)
