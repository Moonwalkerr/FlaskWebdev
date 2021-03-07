from flask import Flask, request, render_template
import subprocess

app = Flask("MenuApp")

@app.route("/")
def homePage():
    return "Welcome To The Windows 10 Menu Program <b>WEB UI</>!"

@app.route("/input")
def cmdInput():
    return render_template('myForm.html')

@app.route("/output")
def cmdOutput():
    # userName = request.args.get("userName")
    commandInput = request.args.get("output")
    commandOutput =  subprocess.getoutput("commandInput")
    return render_template("output.html", cmdOutput=commandOutput)