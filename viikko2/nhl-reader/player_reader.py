"""
PlayerReader module.
"""
import requests
from player import Player

class PlayerReader:
    """
    Reads player data from URL.
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, url):
        self._url = url

    def get_players(self):
        """
        Fetches JSON from URL and returns list of Player objects.
        """
        response = requests.get(self._url, timeout=10).json()

        return [Player(player_dict) for player_dict in response]
