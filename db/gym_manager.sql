DROP TABLE member_classes;
DROP TABLE members;
DROP TABLE classes;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255),
    duration INT
);

CREATE TABLE member_sessions (
    id SERIAL PRIMARY KEY
    member_id INT REFERENCES  members(id) ON DELETE CASCADE,
    session_id INT REFERENCES sessions(id) ON DELETE CASCADE,
    review TEXT
);