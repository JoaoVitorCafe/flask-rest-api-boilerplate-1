from errors import bp

@bp.route("/", methods=["GET"])
def errors():
    return "Errors route is running OK!"