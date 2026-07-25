-- Creates the hbtn_0d_usa database and the cities table.

-- Creates the database if it does not already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Selects the required database.
USE hbtn_0d_usa;

-- Creates the cities table with a foreign key to states.
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
