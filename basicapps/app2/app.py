from flask import Flask
from flask.globals import request
from flask.templating import render_template


app = Flask("MenuApp")

@app.route("/")
def homePage():
    return "Welcome To The Windows 10 Menu Program <b>WEB UI</>!"

@app.route("/input")
def cmdInput():
    return render_template('myForm.html')

@app.route("/output")
def cmdOutput():
    output = request.args.get("output")
    return render_template("output.html", cmdOutput=output)