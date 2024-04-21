from auth import bp

@bp.route("/", methods=["GET"])
def auth():
    return "Auth route is running OK!"