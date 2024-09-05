import uuid
from player import Player
from colors import Color
from typing import List

class Game():
    def __init__(self):
        self.game_id = uuid.uuid4()
        self.players = []

    def set_players(self, players: List[Player]):
        colors = set()

        for player in players:
            if player.color in colors:
                raise ValueError(f"Color {player.color.name} has already been used")
            colors.add(player.color)
            self.players.append(player)

    def show_players(self):
        return [
            {"Name": player.name, "Color": player.color.name, "id": str(player.player_id)}
            for player in self.players
        ]