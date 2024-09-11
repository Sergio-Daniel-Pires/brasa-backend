from typing import Any

from flask_restx import Namespace, Resource

from brasa.services.sports.methods import retrieve_sports
from brasa.utils.middleware import middleware

sports_ns = Namespace("Sport", description="Returned mapped sports")

@sports_ns.route("/list")
class ListSports(Resource):

    @sports_ns.doc()
    @middleware()
    def get(self, user_data: dict[str, Any]):
        return retrieve_sports()
