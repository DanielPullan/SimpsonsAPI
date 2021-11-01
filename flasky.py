from flask import Flask, request, render_template, make_response, redirect, url_for, Response, redirect, url_for
import datetime
from simplepush import send, send_encrypted
import secrets
import os
from flask import send_from_directory



app = Flask(__name__)

pushid = "pushme" ## placeholder data
pushpassword = "passme" ## placeholder data
pushsalt = "saltme" ## placeholder data
local = "http://127.0.0.1:5000" # placeholder data


quotes = ['I like my beer cold… my TV loud… and my homosexuals flaming.',
		'I am so smart. I am so smart. S-M-R-T, I mean S-M-A-R-T.', 
		'You’ll have to speak up. I’m wearing a towel.', 
		'Oh, look! Pantyhose. Practical and alluring.',
		'Aw, 20 dollars? I wanted a peanut.',
		'I believe that children are our future. Unless we stop them now.',
		'If you don’t like your job you don’t strike. You just go in every day and do it really half-assed.',
		'I can’t promise I’ll try, but I’ll try to try.',
		'Trying is the first step towards failure.',
		'I think Smithers picked me because of my motivational skills. Everyone says they have to work a lot harder when I’m around.',
		'Weaseling out of things is important to learn; it’s what separates us from the animals… except the weasel',
		'The problem in the world today is communication… too much communication']


@app.route('/')
def home():
	title = "Home"
	return render_template("index.html", data=secrets.choice(quotes), title=title)


@app.route('/api')
def api(METHODS='get'):
	return secrets.choice(quotes)

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
	return secrets.choice(quotes)

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'), code=302)


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
