# controller.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from jogo import Jogo
from jogador import Jogador
from cores import Cor
from itemDistribuicaoTropas import ItemDistribuicaoTropas
from uuid import UUID

app = FastAPI()

# Modelos de entrada para as requisições
class DadosJogador(BaseModel):
    nome: str
    cor: Cor

class ResultadosDados(BaseModel):
    resultados_dados: List[int]

class RequisicaoDistribuicaoTropas(BaseModel):
    id_jogador: UUID
    distribuicao_tropas: List[ItemDistribuicaoTropas]

# Instância do jogo
jogo = Jogo()

# Rota para criar um novo jogo
@app.post("/criar-jogo")
def criar_jogo(jogadores: List[DadosJogador]):
    try:
        jogadores_obj = [Jogador(jogador.nome, jogador.cor) for jogador in jogadores]
        jogo.definir_jogadores(jogadores_obj)
        return {"Mensagem": "Jogo criado com sucesso!", "Jogadores": jogo.mostrar_jogadores()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Rota para listar os jogadores
@app.get("/jogadores")
def obter_jogadores():
    return jogo.mostrar_jogadores()

# Rota para definir a ordem dos jogadores com base nos dados
@app.post("/definir-ordem")
def definir_ordem(resultados_dados: ResultadosDados):
    return jogo.definir_ordem(resultados_dados.resultados_dados)


