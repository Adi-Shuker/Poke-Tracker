"# Pokemon Tracker
In this project we create a Pokemon API.
we write the server in python and use GET, POST, PUT, DELETE HTTP methods.
we create and insert data to DB with SQL queries
our DB scheme :
// img of scheme

API routes :

Get a specific pokemon (with updated types)
http://localhost:8000/pokemons/{pokemon_name}

Add new trainer
http://localhost:8000/trainers

Get pokemons by type
http://localhost:8000/trainers

Get pokemons by trainer
http://localhost:8000/trainers

Get trainers of a pokemon
http://localhost:8000

Evolve (pokemon x of trainer y)
http://localhost:8000/pokemons/evolve

Delete pokemon of trainer
http://localhost:8000/pokemons/{pokemon_id}/trainers/{trainer_name}")


## Running instructions

### How to initialize the DB ?


### How to run the server ?

1. run `server.py`
   which run the server on port 8000

2. go to http://localhost:8000 and start using the pokemonAPI.