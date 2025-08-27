<div align="center">

[![Laliga](https://raw.githubusercontent.com/jaschrs/LaLigaAPI/refs/heads/master/.github/LaLiga_EA_Sports_2023_Vertical_Logo.svg.png)](#readme)

Note: Currently does not support player statistics

[Help](#help)
</div>

# Overview
With support from the highly popular football tracker "FotMob", this API provides the latest and most accurate information from The Campeonato Nacional de Liga de Primera División (LaLiga). Including live table updates, player statistics, and even fixtures. 

# Disclaimer
This project is not affiliated with or endorsed by FotMob. All data is owned by FotMob. This repository only provides code to access that data

- Repo only provides code.
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
      "drawn": drawn games,
      "goal_difference": goals for subracted by goals against,
      "goals_against": goals scored against the team,
      "goals_for": goals scored by the team,
      "lost": games lost,
      "played": games played,
      "points": league points,
      "position": leauge position,
      "team_name": club name,
      "won": games won
    },
...
```

/fixtures/[matchweek]

Returns the fixtures occurring on specified matchweek
```js
{
  "fixtures mw [matchweek specified]": [
    {
      "away_score": score of away team,
      "away_team": "away team name",
      "canceled": boolean if match is canceled,
      "finished": boolean if match has concluded,
      "home_score": home team score,
      "home_team": "home team name",
      "match_date_utc": "match date and time",
      "round": "matchweek",
      "started": boolean if match has begun
    },
...
```

# Help
Ask AI with the proper context
