from flask import Flask, render_template
import subprocess
app = Flask("MyFirstApp")

@app.route("/search")
def mySearch():
    print("Seach page accessed")
    return ("<b>Seaching</b>")

@app.route("/email")
def mySearch2():
    print("Seach page accessed")
    return render_template("a.html")

@app.route("/date")
def myDate():
    curDate = subprocess.getoutput("date /t")
    print("Date page accessed")
    return curDate