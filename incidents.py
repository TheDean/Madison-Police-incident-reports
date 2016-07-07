import feedparser
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

RSS_FEED = "http://www.cityofmadison.com/police/newsroom/incidentreports/rss.cfm?a=71"

@app.route("/")

def get_incidents():
	feed = feedparser.parse(RSS_FEED)
	return render_template("index.html", articles=feed['entries'])

if __name__ == '__main__':
	app.run(port=5000, debug=True, use_reloader=True)