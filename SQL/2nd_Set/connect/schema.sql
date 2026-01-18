CREATE TABLE Users
(
    "id" INTEGER NOT NULL,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "username" TEXT UNIQUE NOT NULL,
    "password" TEXT  UNIQUE NOT NULL,
    PRIMARY KEY("id")
);



CREATE TABLE Schools
(
    "id" INTEGER NOT NULL,
    "name" TEXT,
    "type" TEXT,
    "location" TEXT,
    "founded_year" INTEGER,
    PRIMARY KEY("id")
);


CREATE TABLE Companies
(
    "id" INTEGER NOT NULL,
    "name" TEXT NOT NULL,
    "industry" TEXT,
    "location" TEXT,
    PRIMARY KEY("id")
);



CREATE TABLE Connections_with_people
(
    "user1_id" INTEGER NOT NULL,
    "user2_id" INTEGER NOT NULL,
    PRIMARY KEY("user1_id", "user2_id"),
    FOREIGN KEY("user1_id") REFERENCES Users("id"),
    FOREIGN KEY("user2_id") REFERENCES Users("id"),
    CHECK(user1_id < user2_id)
);



CREATE TABLE Connections_with_schools
(
    "user_id" INTEGER NOT NULL,
    "school_id" INTEGER NOT NULL,
    "start_date" NUMERIC NOT NULL,
    "end_date" NUMERIC,
    "degree" TEXT,
    PRIMARY KEY("user_id", "school_id", "start_date"),
    --we can add "degree" to catch edge cases: same person entering the same school at the same date for two distinct degrees
    FOREIGN KEY("user_id") REFERENCES Users("id"),
    FOREIGN KEY("school_id") REFERENCES Schools("id")
);



CREATE TABLE Connections_with_companies
(
    "id" INTEGER PRIMARY KEY
    "user_id" INTEGER NOT NULL,
    "company_id" INTEGER NOT NULL,
    "start_date" NUMERIC NOT NULL,
    "end_date" NUMERIC,
    "title" TEXT,
    FOREIGN KEY("user_id") REFERENCES Users("id"),
    FOREIGN KEY("company_id") REFERENCES Companies("id")
    UNIQUE("user_id", "company_id", "start_date"),
    -- this is the other way to do it: keep a surrogate PK but add a UNIQUE constraint to forbid duplicates
    --we can add "title" to catch edge cases: same person entering the same company at the same date for two distinct roles

);

