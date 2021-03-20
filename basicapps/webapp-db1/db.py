from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# creating the app
app = Flask(__name__)

# providing the path of database => uri
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///myDb/data.sqlite'
# ORM 
database = SQLAlchemy(app)



# creating a child class that inherits the property of database (parent) class
class myDb(database.Model):
    # initializing schemas and column names
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String)
    age = database.Column(database.Integer)
    remark = database.Column(database.String)

    def __init__(self, name, age, remark):
        self.name = name
        self.age = age
        self.remark = remark


# creating files, schemas, records => db.sqlite file
database.create_all()
