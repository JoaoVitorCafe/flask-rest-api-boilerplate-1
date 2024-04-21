from users import bp
from flask import jsonify
from models.Users import Users


@bp.route("/", methods=["GET"])
def get_users():
    users = Users.query.all()

    users_list = [{'id': user.id_user, 'name': user.name, 'age': user.age} for user in users]

    return jsonify({'users': users_list}), 200


@bp.route("/<id_user>", methods=["GET"])
def get_user_by_id(id_user):
    user = Users.query.filter_by(id_user=id_user).first()

    if user is None:
        return jsonify({}), 404 

    return jsonify({'username': user.name}), 200