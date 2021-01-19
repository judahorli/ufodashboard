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
    # all_ufo_df['Date'] = pd.to_datetime(all_ufo_df['Date / Time'])
    # all_ufo_df['Posted'] = pd.to_datetime(all_ufo_df['Posted'])

    us_states = ["AL", "AK", "AS", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "GU", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA",
    "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "MP", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "VI", "WA", "WV", "WI", "WY"]
    us_states_df = all_ufo_df[all_ufo_df["State"].isin(us_states)]

    random = us_states_df.sample(n=1)
    city = str(random["City"].iloc[0])
    state = str(random["State"].iloc[0])
    date = str(random["Datetime"].iloc[0])
    shape = str(random["Shape"].iloc[0])
    duration = str(random["Duration"].iloc[0])
    summary = str(random["Summary"].iloc[0])
    posted_date = str(random["Posted"].iloc[0])
    html = "<h3>Random Report</h3><div>datetime: " + date + "</div><div>location: " + city + ", " + state + "</div><div>UFO shape identified as " + shape + " shaped</div><div>duration of incident: " + duration + "</div><div>incident summary: " + summary + "</div>"
    return jsonify(html=html)

