<div align="center">

[![Laliga](https://raw.githubusercontent.com/jaschrs/LaLigaAPI/refs/heads/master/.github/LaLiga_EA_Sports_2023_Vertical_Logo.svg.png)](#readme)
<img width="250" height="250" alt="image" src="https://github.com/user-attachments/assets/6102a70a-6910-459c-a663-cf842da51969" />

Note: Currently does not support player statistics

[Help](#help)

[![Unofficial](https://img.shields.io/badge/Unofficial%20API-Not%20affiliated%20with%20FotMob%20Or%20LaLiga-red?style=for-the-badge)](#legal-notice)
</div>

# Overview
With support from the highly popular football tracker "FotMob", this API provides the latest and most accurate information from The Campeonato Nacional de Liga de Primera División (LaLiga). Including live table updates, player statistics, and even fixtures. 

# Legal Notice
This project is an unofficial API for LaLiga information. It is not affiliated with, endorsed by, or associated with FotMob.

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
3. Run main.py
4. Follow link that appears in terminal
5. Make requests with that link

(Tested with Pycharm)

# Endpoints
/table

Returns the live LaLiga table in order
```js
[
  "laliga_table",
  [
    {
      "position": int league position,
      "team_name": "club name",
      "played": int games played,
      "won": int games won,
      "drawn": int drawn games,
      "lost": int games lost,
      "goals_for": int goals scored by the team,
      "goals_against": int goals scored against the team,
      "goal_difference": int goals for subracted by goals against,
      "points": int league points
    },
...
```

/fixtures/[matchweek]

Returns the fixtures occurring on specified matchweek
```js
{
  "fixtures mw [matchweek specified]": [
    {
      "home_team": "home team name",
      "away_team": "away team name",
      "round": int matchweek,
      "canceled": boolean if match is canceled,
      "started": boolean if match has begun,
      "finished": boolean if match has concluded,
      "match_date_utc": "match date and time",
      "home_score": int home team score if applicable,
      "away_score": int score of away team if applicable
    },
...
```

# Help
Ask AI with the proper context
