DROP TABLE IF EXISTS results;
DROP TABLE IF EXISTS constructors;
DROP TABLE IF EXISTS drivers;
DROP TABLE IF EXISTS races;
DROP TABLE IF EXISTS scores;

CREATE TABLE scores (
    id  SERIAL PRIMARY KEY,
    position INT,
    points INT
);

CREATE TABLE races (
    id SERIAL PRIMARY KEY,
    location VARCHAR(255)
);

CREATE TABLE drivers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    points INT,
    wins INT,
    podiums INT
);

CREATE TABLE constructors(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    driver1_id INT NOT NULL REFERENCES drivers(id),
    driver2_id INT NOT NULL REFERENCES drivers(id),
    points INT
);

CREATE TABLE results(
    id SERIAL PRIMARY KEY,
    position INT,
    win BOOLEAN,
    podium BOOLEAN,
    score_id INT NOT NULL REFERENCES scores(id), 
    driver_id INT NOT NULL REFERENCES drivers(id), 
    constructor_id INT NOT NULL REFERENCES constructors(id), 
    race_id INT NOT NULL REFERENCES races(id) 
);



