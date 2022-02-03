#importing modules
from flask import Flask, request, redirect, render_template, session
from flask_session import Session

app = Flask(__name__)
SESSION_TYPE = "filesystem"
app.config.from_object(__name__)
Session(app)

#Main
@app.route("/")
def index():
    #Creating session variables for the user
    if 'dates_chart' not in session:
        session['dates_chart'] = {
        "date": {"year": 2020, "month": 3},
        }
    if 'dates_map' not in session:
        session['dates_map'] = {
        "date": {"year": 2020, "month": 3},
        }
    
    return render_template("index.html")

@app.route("/description")
def description():
    
    return render_template("index.html")

@app.route("/model/chart")
def model_chart():
    
    return render_template("index.html")

@app.route("/model/map")
def model_map():
    
    return render_template("index.html")


