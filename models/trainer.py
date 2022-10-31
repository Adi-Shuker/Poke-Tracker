from models.db_connection import connection
from fastapi import HTTPException


class Trainer():
    name: str
    town: str

    def insert_trainers(trainers):
        try:
            with connection.cursor() as cursor:
                query = f"INSERT ignore into trainers(name, town) values{','.join(trainers)};"
                print(query)
                cursor.execute(query)
                connection.commit()
        except Exception as e:
            raise HTTPException(
                status_code=500, detail="DB Error - insert_trainers")

    def insert_pokemons_trainers(pokemon_trainer):
        try:
            with connection.cursor() as cursor:
                query = f"INSERT ignore into pokemons_trainers(pokemon_id, trainer_name) values{','.join(pokemon_trainer)};"
                cursor.execute(query)
                connection.commit()
        except Exception as e:
            raise HTTPException(
                status_code=500, detail="DB Error - insert_pokemons_trainers")

    # return array
    def find_owners(pokemon_name):
        try:
            with connection.cursor() as cursor:
                query = f'''
                SELECT DISTINCT trainer_name FROM pokemons_trainers as pt,
                pokemons as p WHERE p.name = "{pokemon_name}" 
                AND pt.pokemon_id = p.id
                '''
                cursor.execute(query)
                results = cursor.fetchall()
                trainer_by_pokemon = []
                for res in results:
                    trainer_by_pokemon.append(res["trainer_name"])
                return (trainer_by_pokemon)
        except Exception as e:
            raise HTTPException(
                status_code=500, detail="DB Error - find_owners")

    def find_roster(trainer_name):
        try:
            with connection.cursor() as cursor:
                query = f'''
                SELECT DISTINCT name FROM pokemons as p, pokemons_trainers as pt
                WHERE pt.trainer_name = "{trainer_name}" AND pt.pokemon_id = p.id;
                '''
                cursor.execute(query)
                results = cursor.fetchall()
                pokemons_of_trainer = []
                for res in results:
                    pokemons_of_trainer.append(res["name"])
                return (pokemons_of_trainer)
        except Exception as e:
            raise HTTPException(
                status_code=500, detail="DB Error - find_roster")

    def delete_pokemon_of_trainer(pokemon_id, trainer_name):
        try:
            with connection.cursor() as cursor:
                query = f'''
                DELETE FROM pokemons_trainers where pokemon_id={pokemon_id} 
                and trainer_name="{trainer_name}";
                '''
                cursor.execute(query)
                connection.commit()
        except Exception as e:
            raise HTTPException(
                status_code=500, detail="DB Error - delete_pokemon_of_trainer")

    def evolve_pokemon_of_trainer(old_pokemon_id, new_pokemon_id, trainer_name):
        try:
            with connection.cursor() as cursor:
                query = f'''
                UPDATE pokemons_trainers SET pokemon_id ={new_pokemon_id}
                WHERE pokemon_id={old_pokemon_id} and trainer_name="{trainer_name}";
                '''
                cursor.execute(query)
                connection.commit()
        except Exception as e:
            raise HTTPException(
                status_code=500, detail="DB Error - evolve_pokemon_of_trainer")
