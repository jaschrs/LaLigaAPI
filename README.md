<div align="center">

[![Laliga](https://raw.githubusercontent.com/jaschrs/LaLigaAPI/refs/heads/master/.github/LaLiga_EA_Sports_2023_Vertical_Logo.svg.png)](#readme)

Note: Currently does not support player statistics

[Help](#help)
</div>

# Overview
With support from the highly popular football tracker "FotMob", this API provides the latest and most accurate information from The Campeonato Nacional de Liga de Primera División (LaLiga). Including live table updates, player statistics, and even fixtures. 

# Disclaimer
This project is not affiliated with or endorsed by FotMob. All data is owned by FotMob. This repository only provides code to access that data

- Repository only provides code to access publicy available data.
- Data is sourced from FotMob, and users must respect FotMob’s terms.
- I don’t own or license the data itself.
- The entire project is for educational purposes, not to be used commercially

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
