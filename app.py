from flask import Flask, render_template

app = Flask("MyFirstApp")

@app.route("/search")
def mySearch():
    print("Seach page accessed")
    return ("<b>Seaching</b>")

@app.route("/email")
def mySearch2():
    print("Seach page accessed")
    return render_template("index.html")