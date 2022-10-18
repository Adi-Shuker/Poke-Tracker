import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
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
