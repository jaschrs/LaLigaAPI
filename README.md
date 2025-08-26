<div align="center">

![Laliga](https://raw.githubusercontent.com/jaschrs/LaLigaAPI/refs/heads/master/.github/LaLiga_EA_Sports_2023_Vertical_Logo.svg.png)

Note: Currently only supports table requests
</div>

# Overview
With support from the highly popular football tracker "FotMob", this API provides the latest and most accurate information from The Campeonato Nacional de Liga de Primera División (LaLiga). Including live table updates, player statistics, and even fixtures. 

# Usage
1. Clone repo
2. Run `pip install -r requirements.txt` in the terminal
3. Run main.py
4. Follow link that appears in terminal
5. Make requests with that link
(Tested with Pycharm)

# Endpoints
/laligatable
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

# Help
Ask AI with the proper context
