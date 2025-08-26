from flask import Flask
import os
from app.localservice import config_localservice
from app.services.table import get_table

app = Flask(__name__)

url = "https://www.fotmob.com/api/data/tltable?leagueId=87"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/139.0.0.0 Safari/537.36",
    "X-Mas": os.getenv("X-MAS")
}

if __name__ == "__main__":
    app = config_localservice()

    @app.route("/laliga_table")
    def table():
        return get_table(url, headers)

    app.run(debug=True)