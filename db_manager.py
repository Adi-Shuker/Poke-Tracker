# TODO - query extesion, error handling

import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="poke_tracker",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

if connection.open:
    print("the connection is opened")


def insert_pokemons(pokemons):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT ignore into pokemons(id, name, height, weight) values{','.join(pokemons)};"
            cursor.execute(query)
            connection.commit()
            result = cursor.fetchall()
            print(result)
    except:
        print("DB Error")


def insert_types(types):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT ignore into types(name) values{','.join(types)};"
            cursor.execute(query)
            connection.commit()
            result = cursor.fetchall()
            print(result)
    except:
        print("DB Error")


def insert_trainers(trainers):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT ignore into trainers(name, town) values{','.join(trainers)};"
            print(query)
            cursor.execute(query)
            connection.commit()
            result = cursor.fetchall()
            print(result)
    except:
        print("DB Error")


def insert_pokemons_trainers(pokemon_trainer):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT ignore into pokemons_trainers(pokemon_id, trainer_name) values{','.join(pokemon_trainer)};"
            cursor.execute(query)
            connection.commit()
            result = cursor.fetchall()
            print(result)
    except:
        print("DB Error")


def insert_pokemons_types(pokemons_types):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT ignore into pokemons_types(type_name, pokemon_id) values{','.join(pokemons_types)};"
            cursor.execute(query)
            connection.commit()
            result = cursor.fetchall()
            print(result)
    except:
        print("DB Error")


# queries

# ex1
def heaviest_pokemon():
    try:
        with connection.cursor() as cursor:
            query = "SELECT name FROM pokemons WHERE weight = (SELECT MAX(weight) FROM pokemons);"
            cursor.execute(query)
            result = cursor.fetchall()
            heaviest_pokemon_name = result[0]["name"]
            return (heaviest_pokemon_name)
    except:
        print("DB Error")

# ex2


def pokemons_by_type(type):
    try:
        with connection.cursor() as cursor:
            query = f'SELECT name FROM pokemons_types as pt, pokemons as p WHERE pt.type_name = "{type}" AND pt.pokemon_id = p.id'
            cursor.execute(query)
            print(query)
            results = cursor.fetchall()
            pokemons_by_type_arr = []
            for res in results:
                pokemons_by_type_arr.append(res["name"])
            return (pokemons_by_type_arr)
    except:
        print("DB Error")

# ex3


def find_owners(pokemon_name):
    try:
        with connection.cursor() as cursor:
            query = f'SELECT trainer_name FROM pokemons_trainers as pt, pokemons as p WHERE p.name = "{pokemon_name}" AND pt.pokemon_id = p.id'
            cursor.execute(query)
            results = cursor.fetchall()
            trainer_by_pokemon = []
            for res in results:
                trainer_by_pokemon.append(res["trainer_name"])
            return (trainer_by_pokemon)
    except:
        print("DB Error")


# ex4
def find_roster(trainer_name):
    try:
        with connection.cursor() as cursor:
            query = f'SELECT name FROM pokemons as p, pokemons_trainers as pt WHERE pt.trainer_name = "{trainer_name}" AND pt.pokemon_id = p.id;'
            cursor.execute(query)
            results = cursor.fetchall()
            pokemons_of_trainer = []
            for res in results:
                pokemons_of_trainer.append(res["name"])
            return (pokemons_of_trainer)
    except:
        print("DB Error")


def delete_pokemon_of_trainer(pokemon_id, trainer_name):
    try:
        with connection.cursor() as cursor:
            query = f'DELETE FROM pokemons_trainers where pokemon_id={pokemon_id} and trainer_name="{trainer_name}";'
            print(query)
            cursor.execute(query)
            connection.commit()
            results = cursor.fetchall()
    except:
        print("DB Error")


def evolve_pokemon_of_trainer(old_pokemon_id, new_pokemon_id, trainer_name):
    try:
        with connection.cursor() as cursor:
            query = f'UPDATE pokemons_trainers SET pokemon_id ={new_pokemon_id} WHERE pokemon_id={old_pokemon_id} and trainer_name="{trainer_name}";'
            cursor.execute(query)
            connection.commit()
            results = cursor.fetchall()
            return results
    except:
        print("DB Error")


def get_pokemon_by_id(pokemon_id):
    try:
        with connection.cursor() as cursor:
            query = f'SELECT p.id, p.name, p.height, p.weight,GROUP_CONCAT( DISTINCT pokemons_types.type_name) as types,GROUP_CONCAT(DISTINCT pokemons_trainers.trainer_name) as trainers FROM pokemons as p join pokemons_types on pokemons_types.pokemon_id = p.id join pokemons_trainers on pokemons_trainers.pokemon_id = p.id WHERE p.id = {pokemon_id} group by p.id'
            cursor.execute(query)
            results = cursor.fetchall()
            return results
    except:
        print("DB Error")

# todo


def get_pokemons_by_types_and_trainer(trainer_name, pokemon_type):
    try:
        with connection.cursor() as cursor:
            query = ""
            # cursor.execute(query)
            # results = cursor.fetchall()
            return trainer_name + pokemon_type
    except:
        print("DB Error")
