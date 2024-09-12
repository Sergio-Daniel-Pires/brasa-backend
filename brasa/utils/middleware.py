import functools
import traceback
import uuid
from collections.abc import Callable

import flask
from flask import g, request

from brasa import metrics_collector as mc
from brasa.utils.logger import log


def middleware(send_user_data: bool = True):
    def _middleware(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            status_code = 200
            g.request_id = str(uuid.uuid4()).replace("-", "")[0:12]
            response = { "result": None, "message": "Ok", "request_id": g.request_id }

            try:
                if send_user_data:
                    user_data = dict(flask.request.form)
                    user_data.update(flask.request.files)

                    args = ( args[0], user_data, ) + args[1:]


                log.info("Starting request")
                result = func(*args, **kwargs)
                log.info("Finished request")

                # Return file
                if isinstance(result, flask.Response):
                    return result

                response["result"] = result

            except Exception as exc:
                log.error(traceback.format_exc())
                status_code = 400
                response["message"] = f"{type(exc).__name__} Error: {exc}"

            finally:
                route = request.path

                if status_code < 400:
                    mc.inc_route_ok(route)  # Incrementa o contador de sucesso

                else:
                    mc.inc_route_error(route, status_code)

            # Return json
            return response, status_code

        return wrapper

    return _middleware
