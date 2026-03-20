from flask import request, Blueprint

game_bp = Blueprint("game", __name__)

@game_bp.route("/game/test", methods=["GET"])
def get_game_test():
    return {"msg": "Test for /game/test was successfull"}