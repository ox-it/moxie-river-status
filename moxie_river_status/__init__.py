from flask import Blueprint

from .views import Status


def create_blueprint(blueprint_name, conf):
    river_blueprint = Blueprint(blueprint_name, __name__, **conf)

    river_blueprint.add_url_rule('/',
            view_func=Status.as_view('status'))
    return river_blueprint
