"""
It is impossible to extract player statistics from fotmob API without first obtaining the team ID and player ID.
This function takes a team name and player name as input, fetches the necessary IDs, and then retrieves and formats the
player's statistics.
One could argue that this function is a bit too long, but breaking it down further would require passing multiple
parameters between functions or files, but I thought it would complicate the code unnecessarily.

Complete LaLiga data -> find team ID -> fetch team data using ID -> find player ID -> fetch player data using ID

"""

import requests
from flask import jsonify
from app.public import PublicKey

def get_player_stats(team_name: str, player_name: str):
    """
    Fetches and formats player statistics for a given player in a specified team from fotmob API.
    :param team_name: team in LaLiga as found on fotmob
    :param player_name: full player name in LaLiga as found on fotmob, can be separated by space during call or %20
    :return: json - JSON response with player statistics
    """

    # Fetch complete LaLiga data to find team ID
    alldata: dict = requests.get(PublicKey.fotmoblaliga, headers=PublicKey.headers).json()
    team_id: int | None = None

    # Find team ID based on team name
    for team in alldata["table"][0]["data"]["table"]["all"]:
        if team["name"].lower() == team_name.lower():
            team_id = team["id"]
            break
    if team_id is None:
        return jsonify({"Team error": f"Team '{team_name}' not found in La Liga or does not exist"}), 404

    # Fetch team data using team ID found above to find player ID
    team_data: dict = requests.get(PublicKey.fotmobteams + str(team_id), headers=PublicKey.headers).json()
    player_id: int | None = None

    # Search for player ID in all squad categories (keeper, midfielder, attacker)
    for idx in (1, 2, 3, 4):  # keeper, midfielder, attacker
        for member in team_data["squad"]["squad"][idx]["members"]:
            if member["name"].lower() == player_name.lower():
                player_id = member["id"]
                break
    if player_id is None:  # stop once found
        return jsonify({"Player error": f"Player '{player_name}' not found in team '{team_name}' or does not exist"}), 404

    # Fetch player data using player ID found above
    player_data: dict = requests.get(PublicKey.fotmobplayers + str(player_id), headers=PublicKey.headers).json()

    # Format the player statistics
    formatted: list = []

    formatted.append(
        {
            "basic": {
                "name": player_data["name"],
                "birthday": player_data["birthDate"],
                "contractEnd": player_data["contractEnd"],
                "isCoach": player_data["isCoach"],
                "isCaptain": player_data["isCaptain"],
                "position(s)":{
                    "main": player_data["positionDescription"]["primaryPosition"]["label"],
                    "secondary": player_data["positionDescription"]["nonPrimaryPositions"]
                },
                "height": player_data["playerInformation"][0]["value"]["numberValue"],
                "shirt": player_data["playerInformation"][1]["value"]["numberValue"],
                "age": player_data["playerInformation"][2]["value"]["numberValue"],
                "preferredFoot": player_data["playerInformation"][3]["value"]["key"],
                "nationality": player_data["playerInformation"][4]["value"]["fallback"],
            },
            "statistics": {
                "league": player_data["mainLeague"]["leagueName"],
                "season": player_data["mainLeague"]["season"],
                "goals": player_data["mainLeague"]["stats"][0]["value"],
                "assists": player_data["mainLeague"]["stats"][1]["value"],
                "started": player_data["mainLeague"]["stats"][2]["value"],
                "mactches": player_data["mainLeague"]["stats"][3]["value"],
                "minutesPlayed": player_data["mainLeague"]["stats"][4]["value"],
                "rating": player_data["mainLeague"]["stats"][5]["value"],
                "yellowCards": player_data["mainLeague"]["stats"][6]["value"],
                "redCards": player_data["mainLeague"]["stats"][7]["value"],
            }
        }
    )

    return jsonify(formatted)