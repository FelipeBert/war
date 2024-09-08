import uuid
import random
from player import Player
from typing import List
from objective_card import ObjectiveCard
from territory import Territory
from troopDistributionItem import TroopDistributionItem

class Game():
    def __init__(self):
        self.game_id = uuid.uuid4()
        self.players = []
        self.objective_deck = self.create_objective_deck()
        self.territories = self.create_territories()

    def set_players(self, players: List[Player]):
        colors = set()

        for player in players:
            if player.color in colors:
                raise ValueError(f"Color {player.color.name} has already been used")
            colors.add(player.color)
            self.players.append(player)

        self.assign_objective()
        self.assign_territories()
        self.assign_troops()

    def set_order(self, dice_results: List[int]):
        if len(dice_results) != len(self.players):
            raise ValueError("The number of dice results does not correspond to the number of players.")
        
        results = list(zip(self.players, dice_results))
        
        results_sorted = sorted(results, key=lambda x: x[1], reverse=True)
        
        self.players = [player for player, _ in results_sorted]

    def show_players(self):
        return [
            {"Name": player.name, "Color": player.color.name,
             "id": str(player.player_id),
             "Objective": player.objective_card,    
             "Troops": player.troops,
             "Territories": player.territories,
             "Game id": self.game_id}
            for player in self.players
        ]
    
    def assign_troops(self):
        for player in self.players:
            troops = len(player.territories) / 2
            player.troops = max(1, int(troops))

    def assign_territories(self):
        random.shuffle(self.territories)
        num_players = len(self.players)

        for i, player in enumerate(self.players):
            player_territores = self.territories[i::num_players]
            player.assign_territories(player_territores)
    
    def assign_objective(self):
        for player in self.players:
            player.objective_card = self.draw_objective_card()

    def create_territories(self):
        return [
            Territory("América do Sul"),
            Territory("Europa"),
            Territory("Ásia"),
            Territory("Oceania"),
            Territory("América do Norte"),
            Territory("África"),
            Territory("América Central"),
            Territory("Caribe"),
            Territory("Oriente Médio"),
            Territory("Sudeste Asiático"),
            Territory("Europa Oriental"),
            Territory("Ásia Central"),
            Territory("Oceania Oriental"),
            Territory("Oceania Ocidental"),
            Territory("Ásia Oriental"),
            Territory("Ásia Meridional"),
            Territory("Ásia Setentrional"),
            Territory("África Oriental"),
            Territory("África Ocidental"),
            Territory("África Central"),
            Territory("África Austral"),
            Territory("América do Sul Oriental"),
            Territory("América do Sul Ocidental"),
            Territory("América Central Norte"),
            Territory("América Central Sul"),
            Territory("Caribe Oriental"),
            Territory("Caribe Ocidental"),
            Territory("Oriente Médio Norte"),
            Territory("Oriente Médio Sul"),
            Territory("Europa Ocidental"),
            Territory("Europa Meridional"),
            Territory("Europa Setentrional"),
            Territory("Europa Central"),
            Territory("Sudeste Asiático Norte"),
            Territory("Sudeste Asiático Sul"),
            Territory("Sudeste Asiático Central"),
            Territory("Ásia Central Norte"),
            Territory("Ásia Central Sul")
        ]

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
            "Destruir totalmente OS EXÉRCITOS AMARELOS.",
            "Destruir totalmente OS EXÉRCITOS VERMELHOS.",
            "Destruir totalmente OS EXÉRCITOS PRETOS.",
            "Destruir totalmente OS EXÉRCITOS BRANCO.",
            "Destruir totalmente OS EXÉRCITOS VERDES."
        ]
        return [ObjectiveCard(description) for description in objectives]
    
    def draw_objective_card(self):
        return self.objective_deck.pop(random.randint(0, len(self.objective_deck) - 1))