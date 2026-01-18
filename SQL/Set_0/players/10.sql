SELECT first_name AS "Players who debuted before 2000"
FROM players
WHERE debut < '2000-01-01'
ORDER BY first_name, last_name;

