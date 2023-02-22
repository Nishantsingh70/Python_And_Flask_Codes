from flask import Flask
from flask import render_template
from flask import request


app = Flask("Hot Reload App")

#static route => http://127.0.0.1:5554/name
@app.route("/form")
def myform():
    return render_template("basic.html")

# dynamic route => http://127.0.0.1:5554/name/nisahnt, http://127.0.0.1:5554/name/vimal
@app.route("/name/<y>")
def myname(y):
    return y

#@app.route("/data", methods=["GET"])
@app.route("/data", methods=["POST"])
def mydata():
    #if request.method == "GET":
    if request.method == "POST":
       #data = request.args.get("x")  # used with get method
       data = request.form.get("x")  # used with POST method
       print(data)
       return data


#app.run()
#app.run(port=5554)
app.run(port=5554, debug=True)