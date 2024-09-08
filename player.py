import uuid
from territory import Territory
from typing import List
from troopDistributionItem import TroopDistributionItem

class Player:
    def __init__(self, name, color):
        self.name = name
        self.player_id = uuid.uuid4()
        self.cards = []
        self.cards_in_dispute = []
        self.color = color
        self.objective_card = None
        self.territories = []
        self.troops = 0

    def add_card(self, newCard):
        if isinstance(newCard, list):
            self.cards.extend(newCard)
        else:
            self.cards.append(newCard)

    def play_card(self):
        if self.have_cards:
            return self.cards.pop(0)
        return None
    
    def assign_territories(self, territories: Territory):
            if isinstance(territories, list):
                for territory in territories:
                    self.territories.append(territory)
            else:
                self.territories.append(territories)

    def distribute_troops(self, troop_distribution: List[TroopDistributionItem]):
        total_troops_to_distribute = sum(item.troops for item in troop_distribution)

        if total_troops_to_distribute > self.troops:
            raise ValueError(f"Not enough troops to distribute. Available: {self.troops}, required: {total_troops_to_distribute}")
        
        for item in troop_distribution:
            territory_id = item.territory_id
            troops = item.troops

            territory = next((t for t in self.territories if t.territory_id == territory_id), None)
                
            if territory is None:
                raise ValueError(f"Territory with ID {territory_id} does not belong to player {self.name}")
                
            territory.add_troops(troops)
            
        self.troops -= total_troops_to_distribute

    @property
    def have_cards(self):
        return len(self.cards) > 0
    
    def add_cards_in_dispute(self, card):
        self.cards_in_dispute.append(card)

    def resolve_dispute(self):
        self.cards.extend(self.cards_in_dispute)
        self.cards_in_dispute = []

    def count_cards(self):
        return len(self.cards)
    
    def get_id(self):
        return self.player_id
    
    def __str__(self):
        return f"{self.name} (ID: {self.player_id}) has {len(self.cards)} cards and {self.color} color."
