#importing modules
from crypt import methods
from cachelib import RedisCache
from flask import Flask, request, redirect, render_template, session
from flask_session import Session
from Application.chartvis import plot

app = Flask(__name__)
SESSION_TYPE = "filesystem"
app.config.from_object(__name__)
Session(app)

def change_chart(year: str, city:str):

    session['dates_chart']["year"] = int(year)
    session['dates_chart']["city"] = city

#Main
@app.route("/")
def index():
    #Creating session variables for the user
    if 'dates_chart' not in session:
        session['dates_chart'] = {
        "year": 2020,
        "city": "Medellin"
        }
    if 'dates_map' not in session:
        session['dates_map'] = {
        "year": 2020,
        "month": 3
        }
    
    return render_template("index.html")

@app.route("/description")
def description():
    
    return render_template("index.html")

@app.route("/model/chart", methods=["GET", "POST"])
def model_chart():

    if request.method == "POST":
        year = request.form["chartyear"]
        city = request.form["chartcity"]
        change_chart(year, city)
        return redirect("/model/chart")
        
    return render_template("chart.html",
    graphJSON=plot(session['dates_chart']['year'], "Application/Results.csv",
    session['dates_chart']["city"]))

@app.route("/model/map")
def model_map():
    
    return render_template("index.html")


