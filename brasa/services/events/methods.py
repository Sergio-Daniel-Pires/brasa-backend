import datetime as dt
from typing import Any

from brasa.utils import find_collection

from .models import SportEvent


def list_events(user_data: dict[str, Any]) -> Any:
    start_date = user_data.get("start_date", dt.datetime.now().strftime("%m-%d"))
    end_date = user_data.get("end_date", dt.datetime.now().strftime("%m-%d"))
    sport = user_data.get("sport", "")

    if sport == "":
        raise ValueError("'sport' is a required parameter")

    year_now = dt.datetime.now().year
    start_date = int(dt.datetime.strptime(start_date, "%m-%d").replace(year=year_now).timestamp() * 1000)
    end_date = int(dt.datetime.strptime(end_date, "%m-%d").replace(year=year_now).timestamp() * 1000)

    mdb_conn = find_collection("sports_events")

    return [
        SportEvent.from_dict(sport).to_human() for sport in mdb_conn.find({
            "start_date": { "$gte": start_date }, "end_date": { "$lte": end_date }, "sport_name": sport
        })
    ]
