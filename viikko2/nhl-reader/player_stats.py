"""
PlayerStats module.
"""

class PlayerStats:
    """
    Statistics calculator for players.
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        """
        Returns top scorers filtered by nationality.
        """
        filtered_players = filter(
            lambda p: p.nationality == nationality,
            self._players
        )

        return sorted(
            filtered_players,
            key=lambda p: p.points,
            reverse=True
        )
