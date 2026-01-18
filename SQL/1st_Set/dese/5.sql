SELECT city, COUNT(city) FROM schools
WHERE type = 'Public School'
GROUP BY city
HAVING COUNT(city) <4
ORDER BY COUNT(city) DESC, city;
