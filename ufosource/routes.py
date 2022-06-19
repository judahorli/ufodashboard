from flask import current_app as app
from flask import render_template, jsonify
from ast import literal_eval
import pandas as pd
from .helpers import reports

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/random', methods = ['POST'])
def random_report():
    all_ufo_df = reports
    random = all_ufo_df.sample(n=1)
    link = str(random["Link"].iloc[0])
    city = str(random["City"].iloc[0])
    state = str(random["State"].iloc[0])
    date = str(random["Occurred"].iloc[0])
    shape = str(random["Shape"].iloc[0])
    duration = str(random["Duration"].iloc[0])
    summary = str(random["Summary"].iloc[0])
    posted_date = str(random["Posted"].iloc[0])
    imgs = literal_eval(random["Images"].iloc[0])
    img_html = "<div id=\"images\">"
    if imgs:
        for img in imgs:
            img_html += "<img class=\"ufo_img\" src=\"" + img + "\">"
    img_html += "</div>"
    html = "<h3>Random Report</h3><div><span class=\"bold\">datetime: </span>" + date + "</div><div><span class=\"bold\">location: </span>" + city + ", " + state + "</div><div><span class=\"bold\">duration of incident: </span>" + duration + "</div><div>UFO shape identified as " + shape + " shaped</div><div><span class=\"bold\">incident summary: </span>" + summary + "</div></div>" + img_html + "<a id=\"og_link\" href=\"" + link + "\" target=\"_blank\">original report page</a>"
    return jsonify(html=html)
