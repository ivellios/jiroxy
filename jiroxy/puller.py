import os
from time import sleep
from urllib import request


def pull(server, token):
    req = request.Request(f"{server}")
    req.add_header("Authorization", f"Bearer {token}")
    response = request.urlopen(req)
    data = response.read()

    with open("cache.txt", "wb") as f:
        f.write(data)

    sleep(int(os.environ.get("SYNC_EVERY_SECONDS", 60)))
    pull(server, token)
