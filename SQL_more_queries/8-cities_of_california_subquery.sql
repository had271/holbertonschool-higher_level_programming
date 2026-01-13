-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;
-- Lists all the cities of California that can be found
SELECT cities.id, cities.name
FROM cities cities
WHERE state_id = (
  SELECT id
  FROM states
  WHERE name = 'California')
ORDER BY cities.id ASC;
