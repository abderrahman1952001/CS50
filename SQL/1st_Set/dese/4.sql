SELECT city, COUNT(city) FROM schools
WHERE type = 'Public School'
GROUP BY city
ORDER BY COUNT(city) DESC, city
LIMIT 10;
