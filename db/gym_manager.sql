DROP TABLE member_classes;
DROP TABLE members;
DROP TABLE classes;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255),
    duration INT
);

CREATE TABLE member_classes (
    id SERIAL PRIMARY KEY
    member_id INT REFERENCES  members(id) ON DELETE CASCADE,
    class_id INT REFERENCES classes(id) ON DELETE CASCADE,
    review TEXT
);