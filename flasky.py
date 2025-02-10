from flask import Flask, request, render_template, url_for, Response, redirect, jsonify
import secrets
import json


app = Flask(__name__)


with open('quotes.json', 'r') as f:
    quotes = json.load(f)


@app.route('/')
def home():
	title = "Home"
	return render_template("index.html", data=secrets.choice(quotes), title=title)


@app.route('/api')
def api():
	return jsonify({'quote': secrets.choice(quotes)})

@app.route('/stare')
def stare():
	title = "Nope"
	return render_template('stare.html', title=title)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('stare.html'), 404

@app.route('/humans.txt')
def humans():
	return Response("Made by Dan.", mimetype='text/plain')



if __name__ == "__main__":
	app.run(host="0.0.0.0", port=7420)
