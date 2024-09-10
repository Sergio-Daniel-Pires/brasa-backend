import json

import pytest


class TestOk:
    @pytest.mark.parametrize("message", [
        "Hello World", "Echo bot"
    ])
    def test_normal_echo (self, client, message: str):
        with client:
            data = json.dumps({ "message": message, "echo_type": "None" })

            req = client.post("/echo/string", data=data)

            assert req.json["result"] == message, f"Expected same message, got {req.text}"
            assert req.status_code == 200, f"Expected status 200, got {req.status_code}"
        
    @pytest.mark.parametrize(["message", "reverse"], [
        ( "Hello", "olleH" ), ( "World", "dlroW" )
    ])
    def test_reverse_echo (self, client, message: str, reverse: str):
        with client:
            data = json.dumps({ "message": message, "echo_type": "Reverse" })

            req = client.post("/echo/string", data=data)

            assert (
                req.json["result"] == reverse
            ), f"Expected reversed message ({reverse}), got {req.text}"
            assert req.status_code == 200, f"Expected status 200, got {req.status_code}"
