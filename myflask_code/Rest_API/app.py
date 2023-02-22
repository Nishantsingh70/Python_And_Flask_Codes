from flask import Flask, render_template, request, jsonify


app = Flask("Hot Reload App")

db = [
    {
       #first student
       "id": 1,
       "name": "nishant",
       "contact": [
         {
             "name": "landline",
             "number": 1111
         },
         {
             "name": "mobile",
             "number": 2222
         }
       ]
    },
    {
        #seond student
        "id": 2,
        "name": "vimal",
        "contact": [
            {       
             "name": "landline",
             "number": 1111
            },
            {
             "name": "mobile",
             "number": 2222
            }
        ]
    }
]

##We are representing our API because of it, it is known as Rest API
#CREATE
@app.route("/spost", methods=["POST"])
def f1():
    return "Create a post"

#READ
@app.route("/spost", methods=["GET"] )
def f2():
    # here we are transfering python distionary to js/html page so we have to convert it in JSON format
    return jsonify(db)

#UPDATE
@app.route("/spost", methods=["PUT"])
def f3():
    return "Update a post"

#DELETE
@app.route("/spost", methods=["DELETE"])
def f4():
    return "Delete a post"

#app.run()
#app.run(port=5554)
app.run(port=5554, debug=True)