import requests
from flask import jsonify
from app.public import publickey

def get_table():
    """
    Fetches and formats the current La Liga table from fotmob API.
    :return: json - JSON response with the formatted league table
    """

    # Fetch data from fotmob API
    data: dict = requests.get(publickey.fotmobtable, headers=publickey.headers).json()

    # Format the league table
    formatted = [
        {
            "position": team["idx"],
            "team_name": team["name"],
            "played": team["played"],
            "won": team["wins"],
            "drawn": team["draws"],
            "lost": team["losses"],
            "goals_for": int(team["scoresStr"].split("-")[0]),
            "goals_against": int(team["scoresStr"].split("-")[1]),
            "goal_difference": team["goalConDiff"],
            "points": team["pts"]
        }
        for team in data[0]["data"]["table"]["all"]
    ]

    return jsonify("laliga_table", formatted)