import datetime as dt
from typing import Any

from brasa import metrics_collector as mc
from brasa.utils import find_collection
from brasa.utils.logger import log

from .models import SportEvent


def list_events(user_data: dict[str, Any]) -> Any:
    start_date = user_data.get("start_date", dt.datetime.now().strftime("%m-%d"))
    end_date = user_data.get("end_date", dt.datetime.now().strftime("%m-%d"))
    sport = user_data.get("sport", "")

    if sport == "":
        log.error("'sport' is a required, non-empty parameter")
        raise ValueError("'sport' is a required parameter")

    year_now = dt.datetime.now().year
    log.info(f"Finding '{sport}' events in range {start_date} - {end_date}")
    start_date = int(dt.datetime.strptime(start_date, "%m-%d").replace(year=year_now).timestamp() * 1000)
    end_date = int(dt.datetime.strptime(end_date, "%m-%d").replace(year=year_now).timestamp() * 1000)

    mdb_conn = find_collection("sports_events")

    # Increment sport info metric
    mc.inc_sport_info(sport)

    return [
        SportEvent.from_dict(sport).to_human() for sport in mdb_conn.find({
            "start_date": { "$gte": start_date }, "end_date": { "$lte": end_date }, "sport_name": sport
        })
    ]
