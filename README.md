# UFO Dashboard
## Judah Orli Perillo
#### January, 2021

This is an extension of a data exploration project from 2017, though with more emphasis on app development. I used a combination of BeautifulSoup and Pandas to scrape UFO reports from the National UFO Reporting Center website (http://www.nuforc.org/) and save them to csv. I used OpenRefine to clean data and then hosted the large file on GitHub so I could access it via link. I created a Python web application with Flask. It has a little widget that spits out a random report on page load and when a link is clicked, via a JavaScript XMLHTTPRequest to the Python back-end. I frankensteined Plotly's Dash framework into the Flask to generate the map and graph on the dashboard (for this I followed a tutorial here: https://hackersandslackers.com/plotly-dash-with-flask/). The app is currently hosted on DigitalOcean and can be accessed at this link: https://ufodashboard-l99s5.ondigitalocean.app/

Some things I would like to include in the future are:
  - a live database instead of loading up data via csv
  - the ability to submit a new report
  - interactivity with the plotly dash parts, such as indicating a year or state and updating graphs accordingly
  - scraping and including different types of paranormal report data, such as bigfoot sightings
  - report look up by dat
  
The file "nuforc-scrape.py" is the python script I used to pull the data off the NUFORC website. I developed this in Jupyter Notebook and exported it as a .py script.
