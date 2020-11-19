#1. import Flask
from flask import Flask, jsonify

#2 Create an app
app = Flask(__name__)

hello_list-["hello", "World!"]

#3 create route
@app.route("/")
def home():
    return "Hi"

@app.route("/normal")
def normal():
    return str(hello_list)

@app.route("/jsonified")
def jsonified():
    return jsonify(hello_list)

if__name__=="__main__":
    app.run()
    
    