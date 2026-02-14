"""
Player module.
"""

class Player:
    """
    Class representing a single player.
    """
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.assists = player_dict['assists']
        self.goals = player_dict['goals']
        self.team = player_dict['team']

    @property
    def points(self):
        """
        Calculate total points.
        """
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals} + {self.assists} = {self.points}"
