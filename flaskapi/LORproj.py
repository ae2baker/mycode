#!/usr/bin/env python3
"""Lord of the Rings Character API | Chris Baker"""

from flask import Flask, render_template, jsonify, request, session
import requests
import sqlite3

app = Flask(__name__)

TOKEN = "JrQhgSTZtzYays5Y9Lio"
API_URL = "https://the-one-api.dev/v2"

# TO DO:
# add a new app.route("/signin") page that uses the render_template() function. Borrow the HTML from one of the labs that creates a form; let a person sign in and save that in a session. Otherwise your "/characters" path will always return "session value required, please log in"

# create a database.db file that has actual data in it so you have something to return in your "/characters" route

# make your part2.py file actually print the data out in a nice way

# JSON data from the Lord of the Rings API
@app.route('/api/characters')
def get_characters():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(f"{API_URL}/character", headers=headers)
    data = response.json()
    return jsonify(data)

# HTML using Jinja2 templating and requires a session value
@app.route('/characters')
def show_characters():
    if 'username' in session:
        conn = sqlite3.connect('LORCharacter.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM characters")
        characters = cursor.fetchall()
        return render_template('characters.html', characters=characters)
    else:
        return "Session value required. Please log in."

# Writing to/reading from a cookie
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    if username:
        session['username'] = username
        return "Login successful. Session created."
    else:
        return "Invalid username. Please try again."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224, debug=True)
