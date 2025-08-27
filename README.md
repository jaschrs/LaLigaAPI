<div align="center">

[![Laliga](https://raw.githubusercontent.com/jaschrs/LaLigaAPI/refs/heads/master/.github/LaLiga_EA_Sports_2023_Vertical_Logo.svg.png)](#readme)
<img width="250" height="250" alt="image" src="https://github.com/user-attachments/assets/6102a70a-6910-459c-a663-cf842da51969" />

[Help](#help)

[![Unofficial](https://img.shields.io/badge/Unofficial%20API-Not%20affiliated%20with%20FotMob%20Or%20LaLiga-red?style=for-the-badge)](#legal-notice)
</div>

# Overview
With support from the highly popular football tracker "FotMob", this API provides the latest and most accurate information from The Campeonato Nacional de Liga de Primera División (LaLiga). Including live table updates, player statistics, and even fixtures. 

# Legal Notice
This project is an unofficial API for publicly available LaLiga statisic. It is not affiliated with, endorsed by, or associated with FotMob or LaLiga.

All data provided (including but not limited to match results, fixtures, player statistics, and league tables) originates from FotMob.
All rights to this data remain with FotMob and/or their data providers.

This repository only provides the code to access and serve that information. Users of this project are solely responsible for ensuring their use of the data complies with FotMob’s Terms of Service.

- Repository only provides code to access publicy available data.
- Data is sourced from FotMob, and users must respect FotMob’s terms.
- I don’t own or license the data itself.
- The entire project is for educational purposes only

# Usage
1. Clone repository
2. Run `pip install -r requirements.txt` in the terminal
3. Fetch some X-MAS key from request headers found on fotmob's website (preferably from the TLTABLE network request)
4. Paste key in app/public.py/PublicKey.xmaskey
5. Run main.py
6. Follow link that appears in terminal
7. Make requests with that link

(Tested with Pycharm)

# Endpoints

Endpoint|Description
:---|:---
/table|Returns the live LaLiga table in order
/fixtures/[matchweek number]|Returns the fixtures occurring on specified matchweek
/[team name]/[player name]|Returns player statistics specifically in LaLiga

Example output: /table

```json
[
  "laliga_table",
  [
    {
      "position": 1,
      "team_name": "Villarreal",
      "played": 2,
      "won": 2,
      "drawn": 0,
      "lost": 0,
      "goals_for": 7,
      "goals_against": 0,
      "goal_difference": 7,
      "points": 6
    },
```

Example output: /fixtures/[matchweek]

```json
{
  "fixtures mw 2": [
    {
      "home_team": "Real Betis",
      "away_team": "Deportivo Alaves",
      "round": 2,
      "canceled": false,
      "started": true,
      "finished": true,
      "match_date_utc": "2025-08-22T19:30:00Z",
      "home_score": 1,
      "away_score": 0
    },
```

Example output: /[team name]/[player name]
```json
[
  {
    "basic": {
      "name": "Tajon Buchanan",
      "birthday": {
        "utcTime": "1999-02-08T00:00:00.000Z",
        "timezone": "UTC"
      },
      "contractEnd": {
        "utcTime": "2030-06-30T00:00:00.000Z",
        "timezone": "UTC"
      },
      "isCoach": false,
      "isCaptain": false,
      "position(s)": {
        "main": "Right Midfielder",
        "secondary": [
          {
            "label": "Left Midfielder",
            "key": "leftmidfielder"
          },
          {
            "label": "Right Winger",
            "key": "rightwinger"
          }
        ]
      },
      "height": 183,
      "shirt": 17,
      "age": 26,
      "preferredFoot": "right",
      "nationality": "Canada"
    },
    "statistics": {
      "league": "LaLiga",
      "season": "2025/2026",
      "goals": 3,
      "assists": 0,
      "started": 1,
      "mactches": 2,
      "minutesPlayed": 133,
      "rating": 8.35,
      "yellowCards": 0,
      "redCards": 0
    }
  }
]
```

# Help
Usage help? : Ask AI

Legal questions? : Read legal notice

X-MAS key should be refreshed every 24hrs
