class PublicKey:
    """
    Class containing public keys and headers for fotmob API requests.
    """

    fotmobteams: str = "https://www.fotmob.com/api/data/teams?id="
    fotmobplayers: str = "https://www.fotmob.com/api/data/playerData?id="
    fotmobtable: str = "https://www.fotmob.com/api/data/tltable?leagueId=87"
    fotmoblaliga: str = "https://www.fotmob.com/api/data/leagues?id=87"
    xmaskey: str = "eyJib2R5Ijp7InVybCI6Ii9hcGkvZGF0YS9wbGF5ZXJEYXRhP2lkPTk5MDk5NiIsImNvZGUiOjE3NTYzMjEzOTY4NDcsImZvbyI6InByb2R1Y3Rpb246ODBmOTc5OWM5ZThkZTI5ZGE5NjhhNDkxYWY3MmZmMjY3OWU2NWY0ZSJ9LCJzaWduYXR1cmUiOiI0OUE3QkVBQjlEMENBNTAyNjU0MTNERUUxNjc0MEVGQiJ9"
    headers: dict = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/139.0.0.0 Safari/537.36",
        "X-Mas": xmaskey
    }