import uuid

class ObjectiveCard:
    def __init__(self, description: str):
        self.description = description
        self.card_id = uuid.uuid4()

    def __str__(self):
        return f"Objetivo: {self.description} (ID: {self.card_id})"