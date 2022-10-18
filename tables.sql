CREATE DATABASE poke_tracker;
CREATE TABLE pokemons(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    height INT,
    weight INT
);
CREATE TABLE types(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);
CREATE TABLE pokemon_type(
    type_id INT,
    pokemon_id INT,
    FOREIGN KEY (type_id) REFERENCES types(id),
    FOREIGN KEY (pokemon_id) REFERENCES pokemons(id)
);
CREATE TABLE trainers(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    town VARCHAR(100)
);
CREATE TABLE pokemon_trainer(
    pokemon_id INT,
    trainer_id INT,
    FOREIGN KEY (pokemon_id) REFERENCES pokemons(id),
    FOREIGN KEY (trainer_id) REFERENCES trainers(id)
);
INSERT into pokemons(id, name, height, weight)