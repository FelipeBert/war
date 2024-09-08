from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from game import Game
from player import Player
from colors import Color
from troopDistributionItem import TroopDistributionItem
from uuid import UUID

app = FastAPI()

class PlayerData(BaseModel):
    name: str
    color: Color

class DiceResults(BaseModel):
    dice_results: List[int]

class TroopDistributionRequest(BaseModel):
    player_id: UUID
    troop_distribution: List[TroopDistributionItem]

game = Game()

@app.post("/create-game")
def create_game(players: List[PlayerData]):
    try:
        player_obj = [Player(player.name, player.color) for player in players]
        game.set_players(player_obj)
        return {"Message": "Game Created with Sucess!", "Players":game.show_players()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/players")
def get_players():
    return game.show_players()

@app.post("/set-order")
def set_order(dice_results:DiceResults):
    return game.set_order(dice_results.dice_results)

@app.post("/deploy-troops")
def deploy_troops(troops: TroopDistributionRequest):
    try:
        player = next((p for p in game.players if p.player_id == troops.player_id), None)

        if player is None:
            raise HTTPException(status_code=404, detail="Player not found")

        player.distribute_troops(troops.troop_distribution)

        return {"message": "Troops successfully distributed"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))