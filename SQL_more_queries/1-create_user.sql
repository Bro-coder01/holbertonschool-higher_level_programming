-- Creates user_0d_1 and grants all server privileges.

-- Creates the user if it does not already exist.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- Ensures that the required password is set.
ALTER USER 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- Grants all privileges on the MySQL server.
GRANT ALL PRIVILEGES ON *.*
TO 'user_0d_1'@'localhost';
