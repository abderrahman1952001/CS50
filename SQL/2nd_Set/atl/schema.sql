CREATE TABLE Passengers
(
    "id" INTEGER,
    "first_name" TEXT,
    "last_name" TEXT,
    "age" NUMERIC,
    PRIMARY KEY("id")
);




CREATE TABLE Check_Ins
(
    "id" INTEGER,
    "date" NUMERIC,
    "time" NUMERIC,
    "flight_id" INTEGER,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("flight_id") REFERENCES Flights("id")
);




CREATE TABLE Airlines
(
    "id" INTEGER,
    "name" TEXT,
    "concourse" TEXT CHECK("concourse" IN ("A", "B", "C", "D", "E", "F", "T")),
    PRIMARY KEY ("id")
);




CREATE TABLE Flights
(
    "id" INTEGER,
    "flight_number" NUMERIC,
    "airline_id" INTEGER,
    "departing_airport" TEXT,
    "heading_airport" TEXT,
    "departure_date" NUMERIC,
    "departure_time" NUMERIC,
    "arrival_date" NUMERIC,
    "arrival_time" NUMERIC,
    PRIMARY KEY ("id")
    FOREIGN KEY("airline_id") REFERENCES Airlines("id")
);



