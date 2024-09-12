from flask import Flask, Response
from prometheus_client import Counter, generate_latest

from brasa.utils.logger import log

route_ok_utilization_total: Counter = Counter(
    "route_ok_utilization_total", "Number times each route was consumed with success",
    [ "route" ]
)

route_error_utilization_total: Counter = Counter(
    "route_error_utilization_total", "Number times each route was consumed with error",
    [ "route", "status_code" ]
)

events_retrieved_total: Counter = Counter(
    "events_retrieved_total", "Number times each event information was retrieved",
    [ "sport" ]
)

def inc_route_ok(route: str):
    route_ok_utilization_total.labels(route=route).inc()

def inc_route_error(route: str, status_code: int):
    route_error_utilization_total.labels(route=route, status_code=status_code).inc()

def inc_sport_info(sport: str):
    events_retrieved_total.labels(sport=sport).inc()

def setup_metrics(app: Flask):
    log.info("Setting up /metrics endpoint")

    @app.route('/metrics')
    def metrics():
        return Response(generate_latest(), mimetype='text/plain')
