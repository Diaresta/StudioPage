from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)

## Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database (MVC Controller- Model, View [html, tec.], Controller [app.py])
db = SQL("sqlite:///clients.db")

#Home page
@app.route("/")
def Home():
    return render_template("index.html")

#My Work page
@app.route("/Portfolio.html")
def Portfolio():
    return render_template("MyWork.html")

#Services page
@app.route("/Services.html")
def Services():
    return render_template("Services.html")

@app.route("/Contact.html", methods=["GET", "POST"])
def Contact():
    if request.method == "POST":

        name = request.form.get("name")
        artist = request.form.get("artist")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        db.execute("INSERT INTO Clients (Name, Band, Email, Subject, Message) VALUES (:name, :artist, :email, :subject, :message)",
                name=name, artist=artist, email=email, subject=subject, message=message)

        return render_template("Contact.html")

    else:
        return render_template("Contact.html")


