from flask import request, Blueprint

player_bp = Blueprint("players", __name__)

@player_bp.route("/players/test", methods=["GET"])
def get_players_test():
    return {"msg": "Test for /players/test was successfull"}

@player_bp.route("/players", methods=["GET"])
def get_players():
    return {"msg": "Get players"}

@player_bp.route("/players/<int:id>", methods=["GET"])
def get_player_by_id(id):
    return {"msg": f"Get player {id}"}

@player_bp.route("/players", methods=["POST"])
def post_player():
    return {"msg": "Post players"}

@player_bp.route("/players/<int:id>", methods=["PUT"])
def update_player(id):
    return {"msg": f"Update player {id}"}

@player_bp.route("/players/<int:id>", methods=["DELETE"])
def delete_player(id):
    return {"msg": f"Delete player {id}"}