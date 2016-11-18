from flask import Flask, jsonify, render_template
from event_results import get_events
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
	
@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/techcalendar")
def techcalendar():
    events = get_events()
    google_api_key = os.getenv("GOOGLE_MAP_API_KEY")
    return render_template("techcalendar.html", events = events, google_api_key = google_api_key)
	
# This is a JSON API endpoint to get
# the events list in JSON
@app.route('/techcalendar.json')
def json():
    events = get_events()
    return jsonify(events = events)

if __name__ == "__main__":
    app.run(debug=True)
