from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.environ.get("FOOTBALL_API_KEY")

HEADERS = {
    "X-Auth-Token": API_KEY
}

@app.route("/")
def home():
    return {"status": "Betwise backend live"}

@app.route("/matches")
def matches():
    r = requests.get(
        "https://api.football-data.org/v4/matches",
        headers=HEADERS
    )
    return jsonify(r.json())

if __name__ == "__main__":
    app.run()
