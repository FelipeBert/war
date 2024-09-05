import uuid
import random
from player import Player
from colors import Color
from typing import List
from objective_card import ObjectiveCard

class Game():
    def __init__(self):
        self.game_id = uuid.uuid4()
        self.players = []
        self.objective_deck = self.create_objective_deck()

    def set_players(self, players: List[Player]):
        colors = set()

        for player in players:
            if player.color in colors:
                raise ValueError(f"Color {player.color.name} has already been used")
            colors.add(player.color)
            self.players.append(player)

        self.assign_objective()

    def show_players(self):
        return [
            {"Name": player.name, "Color": player.color.name, "id": str(player.player_id), "Objective": player.objective_card}
            for player in self.players
        ]
    
    def assign_objective(self):
        for player in self.players:
            player.objective_card = self.draw_objective_card()

    def create_objective_deck(self):
        objectives = [
            "Conquistar todos os territórios da América do Sul",
            "Conquistar todos os territórios da Europa",
            "Eliminar um jogador específico",
            "Conquistar na totalidade a EUROPA, a OCEANIA e mais um terceiro.",
            "Conquistar na totalidade a ÁSIA e a AMÉRICA DO SUL.",
            "Conquistar na totalidade a EUROPA, a AMÉRICA DO SUL e mais um terceiro.",
            "Conquistar 18 TERRITÓRIOS e ocupar cada um deles com pelo menos dois exércitos.",
            "Conquistar na totalidade a ÁSIA e a ÁFRICA.",
            "Conquistar na totalidade a AMÉRICA DO NORTE e a ÁFRICA.",
            "Conquistar 24 TERRITÓRIOS à sua escolha.",
            "Conquistar na totalidade a AMÉRICA DO NORTE e a OCEANIA.",
            "Destruir totalmente OS EXÉRCITOS AZUIS.",
            "Destruir totalmente OS EXÉRCITOS AMARELOS."
            "Destruir totalmente OS EXÉRCITOS VERMELHOS."
            "Destruir totalmente OS EXÉRCITOS PRETOS.",
            "Destruir totalmente OS EXÉRCITOS BRANCO."
            "Destruir totalmente OS EXÉRCITOS VERDES."
        ]
        return [ObjectiveCard(description) for description in objectives]
    
    def draw_objective_card(self):
        return self.objective_deck.pop(random.randint(0, len(self.objective_deck) - 1))