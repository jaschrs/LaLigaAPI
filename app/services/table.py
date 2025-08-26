import requests
from flask import jsonify

def get_table(url, headers):

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()
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