-- Creates hbtn_0d_2 and a user with SELECT access only.

-- Creates the database if it does not already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creates the user if it does not already exist.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- Ensures that the required password is set.
ALTER USER 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- Grants read-only access to the database.
GRANT SELECT ON hbtn_0d_2.*
TO 'user_0d_2'@'localhost';
