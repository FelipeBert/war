import uuid

class Player:
    def __init__(self, name, color):
        self.name = name
        self.player_id = uuid.uuid4()
        self.cards = []
        self.cards_in_dispute = []
        self.color = color

    def add_card(self, newCard):
        if isinstance(newCard, list):
            self.cards.extend(newCard)
        else:
            self.cards.append(newCard)

    def play_card(self):
        if self.have_cards:
            return self.cards.pop(0)
        return None
    
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
