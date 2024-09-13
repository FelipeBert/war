import uuid

class Territorio:
    def __init__(self, nome: str):
        self.id_territorio = uuid.uuid4()
        self.nome = nome
        self.tropas = 0

    # Adiciona tropas a um território
    def adicionar_tropas(self, novas_tropas: int):
        self.tropas += novas_tropas

    # Remove tropas de um território
    def remover_tropas(self, numero_tropas: int):
        if numero_tropas > self.tropas:
            raise ValueError("Não há tropas suficientes para remover")
        self.tropas -= numero_tropas

    # Representação do território como string
    def __str__(self):
        return f"Território {self.nome}."
