from flask import current_app as app
from flask import render_template, jsonify
import pandas as pd
from .helpers import reports

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/random', methods = ['POST'])
def random_report():
    all_ufo_df = reports

    us_states = ["AL", "AK", "AS", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "GU", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA",
    "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "MP", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "VI", "WA", "WV", "WI", "WY"]
    us_states_df = all_ufo_df[all_ufo_df["State"].isin(us_states)]

    random = us_states_df.sample(n=1)
    city = str(random["City"].iloc[0])
    state = str(random["State"].iloc[0])
    date = str(random["Date"].iloc[0])
    timest = str(random["Time"].iloc[0])
    shape = str(random["Shape"].iloc[0])
    duration = str(random["Duration"].iloc[0])
    summary = str(random["Summary"].iloc[0])
    posted_date = str(random["Posted"].iloc[0])
    html = "<h3>Random Report</h3><div><span class=\"bold\">datetime: </span>" + date + "</div><div><span class=\"bold\">location: </span>" + city + ", " + state + "</div><div><span class=\"bold\">duration of incident: </span>" + duration + "</div><div>UFO shape identified as " + shape + " shaped</div><div><span class=\"bold\">incident summary: </span>" + summary + "</div>"
    return jsonify(html=html)
