from flask_restx import reqparse

list_events_parser = reqparse.RequestParser()
list_events_parser.add_argument(
    "start_date", type=str, help="Start date for events date range. Used format: MM-DD",
    location="form", default="01-01"
)
list_events_parser.add_argument(
    "end_date", type=str, help="Start date for events date range. Used format: MM-DD",
    location="form", default="12-01"
)
list_events_parser.add_argument(
    "sport", type=str, help="Sport Name (from sport list route)",
    location="form", required=True
)
