import logging
import traceback
from collections.abc import Callable
import functools
import json

import flask

import logging


def middleware(send_user_data: bool = True):
    def _middleware(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            status_code = 200
            response = { "result": None, "message": "Ok" }

            try:
                if send_user_data:
                    user_data = dict(flask.request.form)
                    user_data = dict(json.loads(flask.request.data))
                    user_data.update(flask.request.files)

                    args = [ user_data ] + args


                result = func(*args, **kwargs)

                # Return file
                if isinstance(result, flask.Response):
                    return result

                response["result"] = result

            except Exception as exc:
                logging.error(traceback.format_exc)
                status_code = 400
                response["message"] = f"{type(exc).__name__} Error: {exc}"

            # Return json
            return response, status_code

        return wrapper
