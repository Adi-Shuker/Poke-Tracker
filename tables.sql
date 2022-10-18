-- CREATE DATABASE poke_tracker;
use poke_tracker;
CREATE TABLE pokemons(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    height INT,
    weight INT
);
CREATE TABLE types(name VARCHAR(50) PRIMARY KEY);
CREATE TABLE pokemons_types(
    type_name VARCHAR(50),
    pokemon_id INT,
    FOREIGN KEY (type_name) REFERENCES types(name),
    FOREIGN KEY (pokemon_id) REFERENCES pokemons(id)
);
CREATE TABLE trainers(
    name VARCHAR(50) PRIMARY KEY,
    town VARCHAR(100)
);
CREATE TABLE pokemons_trainers(
    pokemon_id INT,
    trainer_name VARCHAR(50),
    FOREIGN KEY (pokemon_id) REFERENCES pokemons(id),
    FOREIGN KEY (trainer_name) REFERENCES trainers(name)
);