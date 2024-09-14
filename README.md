Projeto Jogo de Estratégia
Este é um projeto baseado em FastAPI para um jogo de estratégia estilo "War", onde jogadores podem escolher exércitos, receber objetivos, territórios e distribuir tropas.

Funcionalidades Implementadas:
1- Como jogador, gostaria de escolher a cor do exército. 
2- Como jogador, gostaria de receber um objetivo.
3- Como jogador, gostaria de receber territórios no início do jogo.
4- Como jogador, gostaria que fosse definida a ordem dos jogadores. 
5- Como jogador, gostaria de receber e distribuir os exércitos no início do jogo. 
 
Rotas:
POST/criar-jogo // Funcionalidade 1,2,3. 
POST/definir-ordem // Funcionalidade 4.
POST/distribuir-tropas //Funcionalidade 5.
GET/jogadores // Listar todos os jogadores e territorios.

*Executando o Projeto*
Clone o repositório e navegue até o diretório.
Instale as dependências
"pip install fastapi uvicorn pydantic"
Execute o servidor FastAPI: 
uvicorn controller:app --reload

Acesse o servidor rodando na URL: http://127.0.0.1:8000/.
