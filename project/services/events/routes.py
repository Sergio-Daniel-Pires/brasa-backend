import json

import flask
from flask_restx import Namespace, Resource

from project.utils.middleware import middleware
from project.utils.parsers import echo_parser
from methods import list_events

events_ns = Namespace("Events", description="Route to retrieve info about next sport events")

@events_ns.route("/list")
class ListEvents(Resource):
    @events_ns.doc(expect=[ echo_parser ])
    @middleware()
    def post(self, user_data):
        return list_events(user_data)
