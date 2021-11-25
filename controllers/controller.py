from flask import render_template, request  # ADDED
from app import app
from models.event_list import add_new_event, events, you_submitted
from models.Event import Event


@app.route("/")
def home():
    return render_template("base.html", title="test")


@app.route("/events")
def index():
    return render_template("index.html", title="Events", events=events)


@app.route("/events/new")
def new_index():
    return render_template("index2.html", title="Add New Event")


@app.route("/events", methods=["POST"])
def add_event():
    event_date = request.form["date"]
    event_name = request.form["name"]
    event_guests = request.form["num_guests"]
    event_location = request.form["location"]
    event_description = request.form["description"]

    new_event = Event(
        event_date, event_name, event_guests, event_location, event_description
    )


    return new_index()


# @app.route("/events", methods=["POST"])
# def add_event():
#     return "Some String"
