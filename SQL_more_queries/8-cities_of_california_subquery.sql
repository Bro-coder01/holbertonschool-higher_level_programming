-- Lists all cities that belong to California without using JOIN.

-- Selects California cities using a subquery.
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
    SELECT states.id
    FROM states
    WHERE states.name = 'California'
)
ORDER BY cities.id ASC;
