-- Lists all cities with the name of their corresponding state.

-- Joins cities with states and sorts the result by city ID.
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
    ON cities.state_id = states.id
ORDER BY cities.id ASC;
