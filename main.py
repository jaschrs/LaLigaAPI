from app.localservice import config_localservice
from app.services.table import get_table
from app.services.playerstats import get_player_stats
from app.services.fixtures import get_fixtures
from app.public import publickey

url = publickey.laligafotmobapiurl
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/139.0.0.0 Safari/537.36",
    "X-Mas": publickey.xmaskey
}

if __name__ == "__main__":
    app = config_localservice()

    @app.route("/laliga_table")
    def table():
        return get_table(url, headers)

    @app.route("/player/<player_name>")
    def player(player_name):
        return get_player_stats(player_name)

    @app.route("/fixtures/<matchweek>")
    def fixtures(matchweek):
        return get_fixtures(matchweek)

    app.run(debug=True)