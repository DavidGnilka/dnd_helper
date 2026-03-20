from flask import request, Blueprint

monster_bp = Blueprint("monsters", __name__)

@monster_bp.route("/monsters/test", methods=["GET"])
def get_monsters_test():
    return {"msg": "Test for /monsters/test was successfull."}

@monster_bp.route("/monsters", methods=["GET"])
def get_monsters():
    return {"msg": "Get monsters"}

@monster_bp.route("/monsters/<int:id>", methods=["GET"])
def get_monster_by_id(id):
    return {"msg": f"Get monster {id}"}

@monster_bp.route("/monsters", methods=["POST"])
def post_monster():
    return {"msg": "Post monsters"}

@monster_bp.route("/monsters/<int:id>", methods=["PUT"])
def update_monster(id):
    return {"msg": f"Update monster {id}"}

@monster_bp.route("/monsters/<int:id>", methods=["DELETE"])
def delete_monster(id):
    return {"msg": f"Delete monster {id}"}