import uuid

class CartaObjetivo:
    def __init__(self, descricao: str):
        self.descricao = descricao
        self.id_carta = uuid.uuid4()

    # Representação da carta objetivo como string
    def __str__(self):
        return f"Objetivo: {self.descricao} (ID: {self.id_carta})"
