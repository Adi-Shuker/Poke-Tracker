# Get pokemons by type-search normal type return eevee
# evolve eevee and check than eevee is not there

from unittest.mock import Mock

from fastapi.testclient import TestClient

from server import app
import models.db_manager as db_manager


client = TestClient(app)


class Testing:

    def test_get_pokemon_valid_input(self):
        pokemon_res = "ditto"
        db_manager.insert_pokemons_types = Mock(
            return_value=[])
        db_manager.get_pokemon_by_id = Mock(
            return_value=[{"name": "ditto"}])
        response = client.get("/pokemons/ditto")
        result = response.json()
        assert response.status_code == 200
        assert result[0]["name"] == pokemon_res

    def test_get_pokemon_invalid_input(self):
        db_manager.insert_pokemons_types = Mock(
            return_value=[])
        db_manager.get_pokemon_by_id = Mock()
        response = client.get("/pokemons/dito")
        assert response.status_code == 400
        assert response.json()[
            "detail"] == "Bad Request - pokemon name does not exist"
    """
    test evolve:
    1.last in chain 
    2.wrong name (404) api or DB
    3.no pokemon for trainer
    4.no trainer
    5.evolve ti pokemon whan the pokemon already exist in trainer pokemons
    """