from abc import ABC, abstractmethod
import uuid
from typing import List
from territorio import Territorio
from itemDistribuicaoTropas import ItemDistribuicaoTropas

class EstrategiaDistribuicaoTropas(ABC):
    @abstractmethod
    def distribuir(self, jogador, distribuicao_tropas: List[ItemDistribuicaoTropas]):
        pass

class DistribuicaoUniforme(EstrategiaDistribuicaoTropas):
    def distribuir(self, jogador, distribuicao_tropas: List[ItemDistribuicaoTropas]):
        total_tropas = jogador.tropas
        num_territorios = len(jogador.territorios)
        tropas_por_territorio = total_tropas // num_territorios
        
        for territorio in jogador.territorios:
            territorio.adicionar_tropas(tropas_por_territorio)
        
        jogador.tropas = 0  
        
class DistribuicaoConcentrada(EstrategiaDistribuicaoTropas):
    def distribuir(self, jogador, distribuicao_tropas: List[ItemDistribuicaoTropas]):
        total_tropas = jogador.tropas
        
        if jogador.territorios:
            jogador.territorios[0].adicionar_tropas(total_tropas)
            jogador.tropas = 0 

class Jogador:
    def __init__(self, nome, cor, estrategia: EstrategiaDistribuicaoTropas):
        self.nome = nome
        self.id_jogador = uuid.uuid4()
        self.cartas = []
        self.cartas_disputa = []
        self.cor = cor
        self.carta_objetivo = None
        self.territorios = []
        self.tropas = 0
        self.estrategia = estrategia 

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
        self.estrategia.distribuir(self, distribuicao_tropas)

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

estrategia_uniforme = DistribuicaoUniforme()
estrategia_concentrada = DistribuicaoConcentrada()

jogador1 = Jogador("Jogador 1", "Azul", estrategia_uniforme)
jogador2 = Jogador("Jogador 2", "Vermelho", estrategia_concentrada)

jogador1.distribuir_tropas([])
jogador2.distribuir_tropas([])
