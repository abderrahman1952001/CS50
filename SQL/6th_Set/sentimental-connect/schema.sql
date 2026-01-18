CREATE TABLE Users
(
    id INT UNSIGNED AUTOINCREMENT,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    username VARCHAR(30) UNIQUE NOT NULL,
    'password' VARCHAR(30) UNIQUE NOT NULL,
    PRIMARY KEY(id)
);



CREATE TABLE Schools
(
    id INT UNSIGNED AUTOINCREMENT,
    'name' VARCHAR(30) NOT NULL,
    'type' VARCHAR(30) NOT NULL,
    'location' VARCHAR(30),
    founded_year VARCHAR(30),
    PRIMARY KEY(id)

);


CREATE TABLE Companies
(
    id INT UNSIGNED,
    'name' VARCHAR(30) NOT NULL,
    industry VARCHAR(30),
    'location' VARCHAR(30),
    PRIMARY KEY(id)

);



CREATE TABLE Connections_with_people
(
    user1_id INT,
    user2_id INT,
    PRIMARY KEY(user1_id, user2_id),
    FOREIGN KEY(user1_id) REFERENCES Users(id),
    FOREIGN KEY(user2_id) REFERENCES Users(id),
    CHECK(user1_id < user2_id)
);



CREATE TABLE Connections_with_schools
(
    user_id INT,
    school_id INT,
    "start_date" DATE NOT NULL,
    "end_date" DATE,
    "degree" VARCHAR(30),
    PRIMARY KEY(user_id, school_id, start_date),
    --we can add "degree" to catch edge cases: same person entering the same school at the same date for two distinct degrees
    FOREIGN KEY(user_id) REFERENCES Users(id),
    FOREIGN KEY(school_id) REFERENCES Schools(id)
);



CREATE TABLE Connections_with_companies
(
    id INT PRIMARY KEY
    user_id INT,
    company_id INT,
    'start_date' DATE NOT NULL,
    end_date DATE,
    'title' VARCHAR(30),
    FOREIGN KEY(user_id) REFERENCES Users(id),
    FOREIGN KEY("company_id") REFERENCES Companies(id)
    UNIQUE(user_id, company_id, 'start_date'),
    --we can add "title" to catch edge cases: same person entering the same company at the same date for two distinct roles

);

