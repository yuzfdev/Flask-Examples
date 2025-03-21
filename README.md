# Book Store App

A simple book store application built using Flask, SQLAlchemy, and PyMySQL.
## Features

- Create new books
- Read all books (displayed on the home page)
- Update existing books
- Delete books from the database

## Installation

To run this application, you'll need to have the following packages installed:

- SQLAlchemy
- Flask
- PyMySQL

you can install them using pip:

```bash
  pip install flask sqlalchemy pymysql
```
    
## Configuration

Create a new file called config.py with the following contents:

```bash
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'

```

### Running the Application
To run the application, execute the following command in your terminal:

```bash
python app.py
```

## Database Schema

The database schema is created using Flask-Migrate. To create the tables, run the following commands:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
This will create a book Table with 4 fields: id(auto increment), title, author, and price
