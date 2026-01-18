.import --csv meteorites.csv meteorites_temp

DELETE FROM meteorites_temp WHERE nametype = 'Relict';

UPDATE meteorites_temp SET mass = NULL WHERE mass = '';
UPDATE meteorites_temp SET year = NULL WHERE year = '';
UPDATE meteorites_temp SET lat = NULL WHERE lat = '';
UPDATE meteorites_temp SET long = NULL WHERE long = '';


UPDATE meteorites_temp SET mass = ROUND(mass, 2);
UPDATE meteorites_temp SET lat = ROUND(lat, 2);
UPDATE meteorites_temp SET long = ROUND(long, 2);

CREATE TABLE meteorites
(
    id INTEGER PRIMARY KEY,
    name TEXT,
    class TEXT,
    mass NUMERIC,
    discovery TEXT,
    year NUMERIC,
    lat NUMERIC,
    long NUMERIC
);

INSERT INTO meteorites (name, class, mass, discovery, year, lat, long)
SELECT name, class, mass, discovery, year, lat, long FROM meteorites_temp
ORDER BY year, name;
