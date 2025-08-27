import requests

from flask import jsonify
from app.public import publickey


def get_fixtures(matchweek: int):

    try:
        int(matchweek)
    except ValueError:
        return jsonify({"Matchweek number error": "Matchweek number must be an integer"}), 400

    if int(matchweek) < 1 or int(matchweek) > 38:
        return jsonify({"Matchweek number error": "Matchweek number must be between 1 and 38"}), 400

    data: dict = requests.get(publickey.laligaentireapi, headers=publickey.headers).json()

    formatted: list = []

    for match in data["matches"]["allMatches"]:
        if match["round"] == matchweek:
            formatted.append(
                {
                "home_team": match["home"]["name"],
                "away_team": match["away"]["name"],
                "round": match["round"],
                "canceled": match["status"]["cancelled"],
                "started": match["status"]["started"],
                "finished": match["status"]["finished"],
                "match_date_utc": match["status"]["utcTime"],
                "home_score": int(match["status"]["scoreStr"].split("-")[0].strip()) if match["status"]["started"] == True else None,
                "away_score": int(match["status"]["scoreStr"].split("-")[1].strip()) if match["status"]["started"] == True else None,
                }
            )

    return jsonify({f"fixtures mw {matchweek}": formatted})