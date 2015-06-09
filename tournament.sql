
--Delete any pre-exist data.
DROP DATABASE IF EXISTS tournament;

--Create new database.
CREATE DATABASE tournament;

--set connection to the database.
\connect tournament;

--Create a table for players data in database.
--IT has 4 columns. (id, name, wins, losses)
create table players (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    wins INT DEFAULT 0,
    losses INT DEFAULT 0 
);

--Create a table for tournament matches.
--IT has 3 columns. (id, winnner, loser)
create table matches (
    id SERIAL PRIMARY KEY,
    winner INT REFERENCES players(id),
    loser INT REFERENCES players(id)
);