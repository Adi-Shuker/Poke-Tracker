# Get pokemons by type-search normal type return eevee
# evolve eevee and check than eevee is not there

from unittest.mock import Mock

from fastapi.testclient import TestClient

from server import app
import db_manager


client = TestClient(app)


class Testing:
    # test get_pokemon

    def test_get_pokemon_bt_type(self):
        get_pokemons_by_type = ["ditto"]
        db_manager.pokemons_by_type = Mock(
            return_value=get_pokemons_by_type)
        response = client.get("/pokemons?pokemon_type=normal")

        result = response.json()
        print(result)
        assert response.status_code == 200

    # def test_delete_poke_from_owner_not_exist(self):
    #     deleted_trainer = {"trainer_name": "nosuchowner", "pokimon_id": "1"}
    #     db_manager.delete_pokimon_from_trainer = Mock(side_effect=TypeError())
    #     # mock_owner = json.dumps({"name": "Mina", "town": "Zedon"})
    #     response = client.delete("/trainers/nosuchowner/pokimons/1")
    #     result = response.json()
    #     assert response.status_code == 200
    #     assert result == {}
