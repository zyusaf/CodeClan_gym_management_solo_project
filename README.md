Gym Management Web Application

This project was built for week 5 of the CodeClan professional development course. The objective was to build a full stack web application to put it into practice what was learnt in previous weeks. The brief was to build a piece of software to help them to manage memberships, and register memebers for classes.

It was built using Flask, PostgreSQL, psycopg2 and HTML/CSS.

Pre-requisites and usage:

Install Python3

Install postgreSQL

Install Flask:pip3 install flask

Install psycopg2: pip3 install psycopg2

Clone/download the project and navigate to that directory in your terminal client

Create the database: createdb gym_manager

Create the database table structure: psql -d gym_manager -f db/gym_manager.sql

Start Flask: flask run

Navigate to the site in your browser at http://localhost:5000