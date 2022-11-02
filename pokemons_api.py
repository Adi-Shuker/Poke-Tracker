import requests
import json
from pokemon import Pokemon
from fastapi import HTTPException


class ElementNotExistError(Exception):
    pass


class Pokemons_API:
    base_url = 'https://pokeapi.co/api/v2'

    def get_pokemon(self, pokemon_name):
        try:
            res = requests.get(f'{self.base_url}/pokemon/{pokemon_name}')
            pokemon = json.loads(res.text)
            return Pokemon(
                id=pokemon["id"],
                name=pokemon["name"],
                types=[type["type"]["name"] for type in pokemon["types"]],
                height=pokemon["height"],
                weight=pokemon["weight"]
            )
        except Exception as e:
            raise ElementNotExistError()

    def _get_evolution_chain(self, pokemon_name):
        res = requests.get(f'{self.base_url}/pokemon/{pokemon_name}')
        species_url = json.loads(res.text)["species"]["url"]
        res = requests.get(species_url)
        evolution_chain_url = json.loads(res.text)["evolution_chain"]["url"]
        res = requests.get(evolution_chain_url)
        evolution_chain = json.loads(res.text)["chain"]
        return evolution_chain

    def _get_pokemon_evolution(self, evolution_chain, pokemon_name):
        while evolution_chain["species"]['name'] != pokemon_name and len(evolution_chain['evolves_to']):
            evolution_chain = evolution_chain['evolves_to'][0]
        if len(evolution_chain['evolves_to']) == 0:
            raise HTTPException(
                status_code=400, detail="Bad Request - pokemon can not evolve")
        evolution_chain = evolution_chain['evolves_to'][0]
        evolve_pokemon_name = evolution_chain["species"]['name']
        return evolve_pokemon_name

    def get_evolve(self, pokemon_name):
        evolution_chain = self._get_evolution_chain(pokemon_name)
        evolve_pokemon_name = self._get_pokemon_evolution(
            evolution_chain, pokemon_name)
        res = requests.get(
            f'{self.base_url}/pokemon/{evolve_pokemon_name}')
        pokemon = json.loads(res.text)
        return Pokemon(
            id=pokemon["id"],
            name=pokemon["name"],
            types=[type["type"]["name"] for type in pokemon["types"]],
            height=pokemon["height"],
            weight=pokemon["weight"]
        )
