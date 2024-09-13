# game.py

import uuid
import random
from jogador import Jogador
from typing import List
from cartaObjetivo import CartaObjetivo
from territorio import Territorio
from itemDistribuicaoTropas import ItemDistribuicaoTropas

class Jogo:
    def __init__(self):
        self.game_id = uuid.uuid4()
        self.jogadores = []
        self.tempo = 0
        self.baralho_objetivos = self.criar_baralho_objetivos()
        self.territorios = self.criar_territorios()

    def definir_jogadores(self, jogadores: List[Jogador]):
        cores = set()

        for jogador in jogadores:
            if jogador.cor in cores:
                raise ValueError(f"A cor {jogador.cor.name} já foi usada")
            cores.add(jogador.cor)
            self.jogadores.append(jogador)

        self.atribuir_objetivo()
        self.atribuir_territorios()
        self.atribuir_tropas()

    def definir_ordem(self, resultados_dados: List[int]):
        if len(resultados_dados) != len(self.jogadores):
            raise ValueError("O número de resultados dos dados não corresponde ao número de jogadores.")
        
        resultados = list(zip(self.jogadores, resultados_dados))
        
        resultados_ordenados = sorted(resultados, key=lambda x: x[1], reverse=True)
        
        self.jogadores = [jogador for jogador, _ in resultados_ordenados]

    def mostrar_jogadores(self):
        return [
            {"Nome": jogador.nome, "Cor": jogador.cor.name,
             "id": str(jogador.id_jogador),
             "Objetivo": jogador.objetivo_card,    
             "Tropas": jogador.tropas,
             "Territorios": jogador.territorios,
             "ID do Jogo": self.game_id}
            for jogador in self.jogadores
        ]
    
    def atribuir_tropas(self):
        for jogador in self.jogadores:
            tropas = len(jogador.territorios) / 2
            jogador.tropas = max(1, int(tropas))

    def atribuir_territorios(self):
        random.shuffle(self.territorios)
        num_jogadores = len(self.jogadores)

        for i, jogador in enumerate(self.jogadores):
            territorios_jogador = self.territorios[i::num_jogadores]
            jogador.atribuir_territorios(territorios_jogador)
    
    def atribuir_objetivo(self):
        for jogador in self.jogadores:
            jogador.objetivo_card = self.sortear_carta_objetivo()

    def criar_territorios(self):
        return [
            Territorio("América do Sul"),
            Territorio("Europa"),
            Territorio("Ásia"),
            Territorio("Oceania"),
            Territorio("América do Norte"),
            Territorio("África"),
            Territorio("América Central"),
            Territorio("Caribe"),
            Territorio("Oriente Médio"),
            Territorio("Sudeste Asiático"),
            Territorio("Europa Oriental"),
            Territorio("Ásia Central"),
            Territorio("Oceania Oriental"),
            Territorio("Oceania Ocidental"),
            Territorio("Ásia Oriental"),
            Territorio("Ásia Meridional"),
            Territorio("Ásia Setentrional"),
            Territorio("África Oriental"),
            Territorio("África Ocidental"),
            Territorio("África Central"),
            Territorio("África Austral"),
            Territorio("América do Sul Oriental"),
            Territorio("América do Sul Ocidental"),
            Territorio("América Central Norte"),
            Territorio("América Central Sul"),
            Territorio("Caribe Oriental"),
            Territorio("Caribe Ocidental"),
            Territorio("Oriente Médio Norte"),
            Territorio("Oriente Médio Sul"),
            Territorio("Europa Ocidental"),
            Territorio("Europa Meridional"),
            Territorio("Europa Setentrional"),
            Territorio("Europa Central"),
            Territorio("Sudeste Asiático Norte"),
            Territorio("Sudeste Asiático Sul"),
            Territorio("Sudeste Asiático Central"),
            Territorio("Ásia Central Norte"),
            Territorio("Ásia Central Sul")
        ]

    def criar_baralho_objetivos(self):
        objetivos = [
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
        return [CartaObjetivo(descricao) for descricao in objetivos]
    
    def sortear_carta_objetivo(self):
        return self.baralho_objetivos.pop(random.randint(0, len(self.baralho_objetivos) - 1))
