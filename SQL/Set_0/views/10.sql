SELECT "english_title" AS "calmest image from Hokusai" FROM views
WHERE "artist" = 'Hokusai'
ORDER BY "entropy"
LIMIT 1;
