from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from game import Game
from player import Player
from colors import Color

app = FastAPI()

class PlayerData(BaseModel):
    name: str
    color: Color

game = Game()

@app.post("/create-game")
def create_game(players: List[PlayerData]):
    try:
        player_obj = [Player(player.name, player.color) for player in players]
        game.set_players(player_obj)
        return {"Message": "Game Created with Sucess!", "Players":game.show_players()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))