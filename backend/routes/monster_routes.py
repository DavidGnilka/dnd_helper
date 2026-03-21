from flask import request, Blueprint
import sqlite3

import models.monster_model as pm
from backend.utils.responses import success, error

monster_bp = Blueprint("monsters", __name__)

@monster_bp.route("/monsters/test", methods=["GET"])
def get_monsters_test():
    return {"msg": "Test for /monsters/test was successfull."}

@monster_bp.route("/monsters", methods=["GET"])
def get_monsters():
    try:
        monsters = pm.MonsterModel.get_all()
        return success(monsters or [])

    except sqlite3.Error:
        return error("Database error",500)
    except Exception as e:
        return error("Internal error",500)

@monster_bp.route("/monsters/<int:id>", methods=["GET"])
def get_monster_by_id(id):
    try:
        monster = pm.MonsterModel.get_by_id(id)
        if not monster:
            return error("Monster not found",404)
        return success(monster)

    except sqlite3.Error:
        return error("Database error",500)
    except Exception as e:
        return error("Internal error",500)

@monster_bp.route("/monsters", methods=["POST"])
def post_monster():
    try:
        data = request.get_json()
        if not data:
            return error("Invalid JSON",400)
        if not data.get("name"):
            return error("Name required",400)
        if not data.get("hp_dice"):
            return error("HP-dice required",400)
        if not data.get("initiative_dice"):
            return error("Initiative-dice required",400)
        monster_id = pm.MonsterModel.create(data.get("name"),data.get("hp_dice"),data.get("initiative_dice"))
        return success({"id":monster_id,"name": data.get("name"), "hp_dice": data.get("hp_dice"), "initiative_dice":data.get("initiative_dice")},201)

    except sqlite3.Error:
        return error("Database error",500)
    except Exception as e:
        return error("Internal error",500)

@monster_bp.route("/monsters/<int:id>", methods=["PUT"])
def update_monster(id):
    try:
        data = request.get_json()
        if not data:
            return error("Invalid JSON",400)
        success_update = pm.MonsterModel.update(id,data.get("name"),data.get("hp_dice"),data.get("initiative_dice"))
        if not success_update:
            return error("Monster not found",404)
        return success({"name": data.get("name"), "hp_dice": data.get("hp_dice"), "initiative_dice":data.get("initiative_dice")},200)

    except sqlite3.Error:
        return error("Database error",500)
    except Exception as e:
        return error("Internal error",500)

@monster_bp.route("/monsters/<int:id>", methods=["DELETE"])
def delete_monster(id):
    try:
        success_delete = pm.MonsterModel.delete(id)
        if not success_delete:
            return error("Monster not found",404)
        return success()

    except sqlite3.Error:
        return error("Database error",500)
    except Exception as e:
        return error("Internal error",500)