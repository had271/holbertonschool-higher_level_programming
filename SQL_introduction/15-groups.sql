-- lists the number of records with the same score 
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY 1
ORDER BY score DESC;
