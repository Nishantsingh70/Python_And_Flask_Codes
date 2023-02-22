from flask import Flask
from flask import request
from flask import render_template
import subprocess

app = Flask("MyVariableApp")

@app.route("/")
def home():
   print("home")
   return "I am on home page"


@app.route("/menu", methods=["GET"])
def mymenu():
   name = request.args.get("x")
   c = request.args.get("y")
   return render_template("mymenu.html", myname=name, cname=c)


@app.route("/form", methods=["GET"])
def myform():
   return render_template("myform.html")


