from flask import Flask
from flask import request
from flask import render_template
import subprocess

app = Flask("MyCommandApp")

@app.route("/form")
def myform():
   print("form")
   return render_template("myform.html")


@app.route("/cmd", methods=["GET"])
def mycmd():
   print("cmd")
   command  = request.args.get("c")
   print(command)
   return "<pre>" + subprocess.getoutput(command) + "</pre>"





