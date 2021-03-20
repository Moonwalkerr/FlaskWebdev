import re
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



## Performing some CRUD Operations on our database

# ----------------------------------------------------
# Create:

# ### creating an object => creating a row inside our table
# jack_snyder = myDb("Jack Snyder",4,'Amazing')
# ### RAM => Storage (database)
# database.session.add(jack_snyder)
# database.session.commit()  # commiting session operation

# russo_bros = myDb("Russo Brothers",44,'Awesome')
# database.session.add(russo_bros)
# database.session.commit() 



# ----------------------------------------------------
# Read :

# record1 = myDb.query.get(1)
# print(record1.age)
### Read - Filter 
# record_age = myDb.query.filter_by(age=44)
# print(record_age.all()[0].name)


# ----------------------------------------------------
# Update
# rec_1 = myDb.query.get(1)
# rec_1.age = 44
# database.session.add(rec_1)
# database.session.commit()


# ----------------------------------------------------
# Delete
rec_2 = myDb.query.get(2)
database.session.delete(rec_2)
database.session.commit()