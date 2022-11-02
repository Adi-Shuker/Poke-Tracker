
from unittest.mock import Mock

from fastapi.testclient import TestClient
from models.pokemon import Pokemon as pokemon_model

from server import app


client = TestClient(app)


class Testing:

    def test_get_pokemon_valid_name(self):
        pokemon_res = "ditto"
        pokemon_model.insert_pokemons_types = Mock(
            return_value=[])
        pokemon_model.get_pokemon_by_id = Mock(
            return_value=[{"name": "ditto"}])
        response = client.get("/pokemons/ditto")
        print(response)
        result = response.json()
        assert response.status_code == 200
        assert result[0]["name"] == pokemon_res

    def test_get_pokemon_invalid_name(self):
        pokemon_model.insert_pokemons_types = Mock(
            return_value=[])
        pokemon_model.get_pokemon_by_id = Mock()
        response = client.get("/pokemons/dito")
        assert response.status_code == 404
        assert response.json()[
            "Error"] == "Pokemon does not exist"
