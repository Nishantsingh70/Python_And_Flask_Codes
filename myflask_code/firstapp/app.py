from flask import Flask, render_template
import subprocess

app = Flask("MyIIEC")

@app.route("/search")
def mysearch():
   print("search")
   return("<b>search</b>")

@app.route("/mail")
def mymail():
   print("mail")
   return render_template("e.html")

@app.route("/date")
def cdate():
   data = subprocess.getoutput("date /t")
   print(data)
   return(data)



