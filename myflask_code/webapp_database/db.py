from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask("DatabaseApp")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb/data.sqlite'

#ORM
db = SQLAlchemy(app)
print(db)

class IIEC(db.Model):
   id = db.Column(db.Integer , primary_key=True , autoincrement=True)
   name = db.Column(db.Text)
   age = db.Column(db.Integer)
   remarks = db.Column(db.Text)

   def __init__(self, name, age, remarks):
       self.name = name
       self.age = age
       self.remarks = remarks

db.create_all()

#Create
"""
jack = IIEC("jack", 20, "Ok")
db.session.add(jack)
db.session.commit()
"""

#Read
"""
r2 = IIEC.query.get(2)
print(r2.name, r2.age, r2.remarks)

rall = IIEC.query.all()
print(rall[0].name)

rage = IIEC.query.filter_by(age=20)
print(rage)
print(rage.all())
"""  

#Update
"""
r1 = IIEC.query.get(1)
r1.age = 30
db.session.add(r1)
db.session.commit()
"""

#Delete
"""
rall = IIEC.query.get(2)
db.session.delete(rall)
db.session.commit()
"""





# 