from typing import Any
import datetime as dt
from project.utils import find_collection

def list_events(user_data: dict[str, Any]) -> Any:
    start_date = user_data.get("start_date", dt.datetime().strftime("%m-%d"))
    end_date = user_data.get("end_date", dt.datetime().strftime("%m-%d"))
    sport = user_data.get("sport", "")

    if sport == "":
        raise ValueError("'sport' is a required parameter")

    start_date = dt.datetime.strptime(start_date, "%m-%d")
    end_date = dt.datetime.strptime(end_date, "%m-%d")

    mdb_conn = find_collection("sport_events")

    return [
        sport["name"] for sport in mdb_conn.find({
            "start_date": start_date, "end_date": end_date, "sport_name": sport
        })
    ]
