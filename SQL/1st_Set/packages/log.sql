
-- *** The Lost Letter ***

-- we have the address from which the package (aka, the letter) was sent
-- and the adress to which it was meant to be delivered
-- so we first need to get their respective IDs from the (adresses) table
-- the we get ID of this package from the (packages) table
-- then we look at the (scans) table to get the ID of the address where that package ended up,
-- lastly we go back to the (adresses) table to get that address and its type
-- here are the SQL querries we need:

-- To get the ID of the address from which the package was sent,
-- and the adress to which it was meant to be sent
SELECT id, "address" FROM addresses
WHERE "address" = '900 Somerville Avenue'
    OR "address" = '2 Finnegan Street';

-- we get from that querry only one id; the ID of the sender address, so that address to which she
-- sent her letter isnt in the database
-- anyway, now we get the ID of the package from the (packages) table using the ID of the sender adress
-- we can use a subquerry for that:
SELECT id, contents, to_address_id FROM packages
WHERE from_address_id =
    (SELECT id FROM addresses
        WHERE "address" = '900 Somerville Avenue');

-- we got three packages, thats why i added the "contents" to see which one is our package
-- now that we have the package's ID we will get from the (scans) table where it ended up
SELECT address_id FROM scans
WHERE action = 'Drop'AND
package_id = (SELECT id FROM packages
WHERE from_address_id =
    (SELECT id FROM addresses
        WHERE "address" = '900 Somerville Avenue'));

-- now we get the id
-- we can nest all the previous querries in one querry with three subquerries
SELECT id, "address", "type" FROM addresses
WHERE id = (SELECT address_id FROM scans
WHERE action = 'Drop'AND
package_id = (SELECT id FROM packages
WHERE from_address_id =
    (SELECT id FROM addresses
        WHERE "address" = '900 Somerville Avenue')));

-- so yes, its letter made it up to her friend, but she misspelled her address.





-- *** The Devious Delivery ***
-- this package has no "From" address so we go to the (packages) table and get its ID and content
SELECT id, contents, to_address_id FROM packages
    wHERE from_address_id IS NULL;

-- we got its id, now we go to the (scans) table to see where did it end up:
SELECT address_id FROM scans
WHERE package_id = (SELECT id FROM packages
        wHERE from_address_id IS NULL)
        ORDER BY timestamp DESC
        LIMIT 1;

-- no we go to the (addresse) table and get the address's name and type
SELECT "address", "type" FROM addresses
WHERE id = (SELECT address_id FROM scans
WHERE package_id = (SELECT id FROM packages
        wHERE from_address_id IS NULL)
        ORDER BY timestamp DESC
        LIMIT 1);





SELECT address_id, action, timestamp FROM scans
    WHERE package_id = (SELECT id FROM packages
        wHERE from_address_id IS NULL);







-- *** The Forgotten Gift ***

-- we get the id of the addresses of the sender and the one who is meant to be the receiver
SELECT address, id FROM addresses
WHERE address = '109 Tileston Street'
OR address = '728 Maple Place';

-- now we get the id of the package and its contest using the sender's address
SELECT id, contents, to_address_id FROM packages
WHERE from_address_id = (SELECT id FROM addresses
WHERE address = '109 Tileston Street');

-- we see that the "to_address_id" match the address of his granddaughter, so no mistakes so far

-- now we get where did the package ended up and which driver handled it using the (scans) table
SELECT address_id, action, timestamp, driver_id FROM scans
WHERE package_id = (SELECT id FROM packages
                    WHERE from_address_id =
                        (SELECT id FROM addresses
                        WHERE address = '109 Tileston Street'));

-- now we get the name of the driver from the (drivers) table
SELECT name FROM drivers
wHERE id = (SELECT driver_id FROM scans
            WHERE package_id = (SELECT id FROM packages
                                WHERE from_address_id =
                        (SELECT id FROM addresses
                        WHERE address = '109 Tileston Street'))
            ORDER BY "timestamp" DESC
            LIMIT 1);


