DROP TABLE earthquakes;
DROP TABLE users;

CREATE TABLE earthquakes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(50),
    time BIGINT,
    magnitude decimal (2, 4),
    latitude decimal (3, 6),
    longitude decimal (3, 6),
    url varchar(200)
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstName varchar (50),
    lastName varchar (50),
    email varchar (100)
);