from flask_restx import Namespace, Resource

from brasa.utils.middleware import middleware
from brasa.utils.parsers import list_events_parser

from .methods import list_events

events_ns = Namespace("Events", description="Route to retrieve info about next sport events")

@events_ns.route("/list")
class ListEvents(Resource):
    @events_ns.doc(expect=[ list_events_parser ])
    @middleware()
    def post(self, user_data):
        return list_events(user_data)
