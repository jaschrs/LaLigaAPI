# Importing flask here is redundant but allow to define the type for the app which I like
import flask
from app.local_service import config_local_service
from app.services.table import get_table
from app.services.player_stats import get_player_stats
from app.services.fixtures import get_fixtures

def main():
    # Set up Flask app
    app: flask.app.Flask = config_local_service()

    # Initialize routes
    @app.route("/table")
    def table():
        return get_table()

    @app.route("/player/<player_name>")
    def player(player_name: str):
        return get_player_stats(player_name)

    @app.route("/fixtures/<matchweek>")
    def fixtures(matchweek: int):
        return get_fixtures(matchweek)

    # Run the app
    app.run(debug=True)

if __name__ == "__main__":
    main()
