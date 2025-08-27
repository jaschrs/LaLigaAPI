import requests
from flask import jsonify

from app.public import publickey

def get_table():

    data: dict = requests.get(publickey.laligafotmobapiurl, headers=publickey.headers).json()

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