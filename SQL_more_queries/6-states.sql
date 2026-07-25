-- Creates the hbtn_0d_usa database and the states table.

-- Creates the database if it does not already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Selects the required database.
USE hbtn_0d_usa;

-- Creates the states table if it does not already exist.
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
