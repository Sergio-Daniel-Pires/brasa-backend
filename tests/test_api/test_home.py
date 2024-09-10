def test_home_return_value (client):
    with client:
        req = client.get("/home/")

        assert req.json["result"] == "Hello World!"
