from flask import Flask, request, render_template, make_response, redirect, url_for, Response
import datetime
from simplepush import send, send_encrypted
import secrets

app = Flask(__name__)

pushid = "ew6ZRa"
pushpassword = "pushme"
pushsalt = "fps03c0q"
local = "http://127.0.0.1:5000"


good = ['I like my beer cold… my TV loud… and my homosexuals flaming.','I am so smart. I am so smart. S-M-R-T, I mean S-M-A-R-T.', 'You’ll have to speak up. I’m wearing a towel.', 'Oh, look! Pantyhose. Practical and alluring.', '“I think Smithers picked me because of my motivational skills. Everyone says they have to work a lot harder when I’m around.', 'The problem in the world today is communication… too much communication']


@app.route('/')
def home():
	title = "Home"
	return render_template("index.html", data=secrets.choice(good), title=title)

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

@app.route('/woohoo', methods=['GET'])
def woohoo():
	return secrets.choice(good)


if __name__ == "__main__":
	app.run(debug=True)
