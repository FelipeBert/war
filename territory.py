import uuid

class Territory:
    def __init__(self, name: str):
        self.territory_id = uuid.uuid4()
        self.name = name
        self.troops = 0

    def add_troops(self, new_troops: int):
        self.troops += new_troops

    def remove_troops(self, num_troops: int):
        if num_troops > self.troops:
            raise ValueError("Not enough troops to remove")
        self.troops = self.troops - num_troops

    def __str__(self):
        return f"Territory {self.name}."
