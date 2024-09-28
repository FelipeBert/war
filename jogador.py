import uuid
from territorio import Territorio
from typing import List
from itemDistribuicaoTropas import ItemDistribuicaoTropas
from abc import ABC, abstractmethod

# Classe Jogador original
class Jogador:
    def __init__(self, nome, cor):
        self.nome = nome
        self.id_jogador = uuid.uuid4()
        self.cartas = []
        self.cartas_disputa = []
        self.cor = cor
        self.carta_objetivo = None
        self.territorios = []
        self.tropas = 0

    def adicionar_carta(self, nova_carta):
        if isinstance(nova_carta, list):
            self.cartas.extend(nova_carta)
        else:
            self.cartas.append(nova_carta)

    def jogar_carta(self):
        if self.tem_cartas:
            return self.cartas.pop(0)
        return None

    def atribuir_territorios(self, territorios: Territorio):
        if isinstance(territorios, list):
            for territorio in territorios:
                self.territorios.append(territorio)
        else:
            self.territorios.append(territorios)

    def distribuir_tropas(self, distribuicao_tropas: List[ItemDistribuicaoTropas]):
        total_tropas_a_distribuir = sum(item.tropas for item in distribuicao_tropas)

        if total_tropas_a_distribuir > self.tropas:
            raise ValueError(f"Não há tropas suficientes. Disponível: {self.tropas}, necessário: {total_tropas_a_distribuir}")
        
        for item in distribuicao_tropas:
            id_territorio = item.id_territorio
            tropas = item.tropas

            territorio = next((t for t in self.territorios if t.id_territorio == id_territorio), None)
                
            if territorio is None:
                raise ValueError(f"Território com ID {id_territorio} não pertence ao jogador {self.nome}")
                
            territorio.adicionar_tropas(tropas)
            
        self.tropas -= total_tropas_a_distribuir

    @property
    def tem_cartas(self):
        return len(self.cartas) > 0

    def adicionar_cartas_disputa(self, carta):
        self.cartas_disputa.append(carta)

    def resolver_disputa(self):
        self.cartas.extend(self.cartas_disputa)
        self.cartas_disputa = []

    def contar_cartas(self):
        return len(self.cartas)

    def obter_id(self):
        return self.id_jogador

    def __str__(self):
        return f"{self.nome} (ID: {self.id_jogador}) tem {len(self.cartas)} cartas e a cor {self.cor}."


# Interface do Decorator
class JogadorDecorator(ABC):
    def __init__(self, jogador: Jogador):
        self._jogador = jogador

    @abstractmethod
    def distribuir_tropas(self, distribuicao_tropas: List[ItemDistribuicaoTropas]):
        pass

class JogadorComContagemDeTropas(JogadorDecorator):
    def __init__(self, jogador: Jogador):
        super().__init__(jogador)
        self.tropas_distribuidas = 0 

    def distribuir_tropas(self, distribuicao_tropas: List[ItemDistribuicaoTropas]):
        self._jogador.distribuir_tropas(distribuicao_tropas)

        tropas_distribuidas = sum(item.tropas for item in distribuicao_tropas)
        self.tropas_distribuidas += tropas_distribuidas
        print(f"Tropas distribuídas até agora: {self.tropas_distribuidas}")

jogador = Jogador(nome="Jogador 1", cor="Azul")
jogador_decorado = JogadorComContagemDeTropas(jogador)

distribuicao_tropas = [ItemDistribuicaoTropas(id_territorio=1, tropas=3), ItemDistribuicaoTropas(id_territorio=2, tropas=2)]
jogador_decorado.distribuir_tropas(distribuicao_tropas)
