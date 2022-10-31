from typing import List
from models.db_connection import connection
from fastapi import status
from fastapi.responses import JSONResponse


class Pokemon():
    id: int
    name: str
    types: List
    height: int
    weight: int
    trainers: List

    def get_id(pokemon_name):
        query = f"select id from pokemons where name='{pokemon_name}'"
        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchone().get("id")

    def insert_pokemons(pokemons):
        try:
            with connection.cursor() as cursor:
                query = f"INSERT ignore into pokemons(id, name, height, weight) values{','.join(pokemons)};"
                cursor.execute(query)
                connection.commit()
        except Exception as e:
            return JSONResponse({"Error": e},
                                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def insert_types(types):
        try:
            with connection.cursor() as cursor:
                query = f"INSERT ignore into types(name) values{','.join(types)};"
                cursor.execute(query)
                connection.commit()
        except Exception as e:
            return JSONResponse({"Error": e},
                                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def insert_pokemons_types(pokemons_types):
        try:
            with connection.cursor() as cursor:
                query = f"INSERT ignore into pokemons_types(type_name, pokemon_id) values{','.join(pokemons_types)};"
                cursor.execute(query)
                connection.commit()
        except Exception as e:
            return JSONResponse({"Error": e},
                                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def heaviest_pokemon():
        try:
            with connection.cursor() as cursor:
                query = "SELECT name FROM pokemons WHERE weight = (SELECT MAX(weight) FROM pokemons);"
                cursor.execute(query)
                result = cursor.fetchall()
                heaviest_pokemon_name = result[0]["name"]
                return (heaviest_pokemon_name)
        except Exception as e:
            return JSONResponse({"Error": e},
                                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def pokemons_by_type(type):
        try:
            with connection.cursor() as cursor:
                query = f'''
                SELECT DISTINCT name FROM pokemons_types as pt,
                pokemons as p WHERE pt.type_name = "{type}" 
                AND pt.pokemon_id = p.id
                '''
                cursor.execute(query)
                pokemons = cursor.fetchall()
                pokemons_by_type_arr = []
                for res in pokemons:
                    pokemons_by_type_arr.append(res["name"])
                return [pokemon["name"] for pokemon in pokemons]
        except Exception as e:
            return JSONResponse({"Error": e},
                                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_pokemon_by_id(pokemon_id):
        try:
            with connection.cursor() as cursor:
                query = f'''
                SELECT p.id, p.name, p.height, p.weight,
                GROUP_CONCAT(DISTINCT pokemons_types.type_name) as types 
                FROM pokemons as p join pokemons_types
                WHERE p.id = {pokemon_id} group by p.id;
                '''
                cursor.execute(query)
                results = cursor.fetchall()
                return results
        except Exception as e:
            return JSONResponse({"Error": e},
                                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
