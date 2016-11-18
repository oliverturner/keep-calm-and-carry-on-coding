import requests
import datetime
import time
import os

def get_events():
    events = []
    meetup_api_key = os.getenv("MEETUP_API_KEY")

    url = "http://api.meetup.com/2/events?group_id=11854362,18245435,17124182,18976100,18926332&status=upcoming&order=time&limited_events=False&%20desc=false&offset=0&format=json&page=200&key={}".format(meetup_api_key)

    r = requests.get(url)
    data = r.json()

    now = datetime.date.today()
    delta = datetime.timedelta(days=14)

    events = [x for x in data["results"] if (convert_meetup_datetime(x["time"]) - now) < delta]

    for event in events:
        event["time"] = convert_meetup_datetime(event["time"])
    return events

def convert_meetup_datetime(meetupdatetime):
   return datetime.datetime.fromtimestamp(meetupdatetime / 1000.0).date()

