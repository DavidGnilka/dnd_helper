from flask import request, Blueprint
import sqlite3

import models.player_model as pm
from backend.utils.responses import success, error

player_bp = Blueprint("players", __name__)

@player_bp.route("/players/test", methods=["GET"])
def get_players_test():
    return {"msg": "Test for /players/test was successfull"}

@player_bp.route("/players", methods=["GET"])
def get_players():
    try:
        players = pm.PlayerModel.get_all()
        return success(players or [])

    except sqlite3.Error:
        return error("Database error",500)
    except Exception as e:
        return error("Internal error",500)

@player_bp.route("/players/<int:id>", methods=["GET"])
def get_player_by_id(id):
    try:
        player = pm.PlayerModel.get_by_id(id)
        if not player:
            return error("Player not found",404)
        return success(player)

    except sqlite3.Error:
        return error("Database error",500)
    except Exception as e:
        return error("Internal error",500)

@player_bp.route("/players", methods=["POST"])
def post_player():
    try:
        data = request.get_json()
        if not data:
            return error("Invalid JSON",400)
        if not data.get("name"):
            return error("Name required",400)
        player_id = pm.PlayerModel.create(data.get("name"),data.get("hp"))
        return success({"id":player_id,"name": data.get("name"), "hp": data.get("hp")},201)

    except sqlite3.Error:
        return error("Database error",500)
    except Exception as e:
        return error("Internal error",500)

@player_bp.route("/players/<int:id>", methods=["PUT"])
def update_player(id):
    try:
        data = request.get_json()
        if not data:
            return error("Invalid JSON",400)
        success_update = pm.PlayerModel.update(id,data.get("name"),data.get("hp"))
        if not success_update:
            return error("Player not found",404)
        return success({"name": data.get("name"), "hp": data.get("hp")},200)

    except sqlite3.Error:
        return error("Database error",500)
    except Exception as e:
        return error("Internal error",500)

@player_bp.route("/players/<int:id>", methods=["DELETE"])
def delete_player(id):
    try:
        success_delete = pm.PlayerModel.delete(id)
        if not success_delete:
            return error("Player not found",404)
        return success()

    except sqlite3.Error:
        return error("Database error",500)
    except Exception as e:
        return error("Internal error",500)