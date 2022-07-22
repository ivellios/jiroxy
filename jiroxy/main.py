import os
import signal
from http.server import HTTPServer
from threading import Thread

from http_handlers import JiraHttpRequestHandler
from puller import pull
from server import serve


def run(server, token, server_class=HTTPServer, handler_class=JiraHttpRequestHandler):
    try:
        pulling_thread = Thread(target=pull, args=(server, token,))
        pulling_thread.daemon = True
        pulling_thread.start()

        serving_thread = Thread(target=serve, args=(server_class, handler_class, ))
        serving_thread.daemon = True
        serving_thread.start()

        signal.pause()
    except (KeyboardInterrupt, SystemExit):
        print("Stopping the service...")


if __name__ == "__main__":
    token = os.environ.get("JIRA_API_KEY")
    url = os.environ.get("JIRA_QUERY_URL")

    run(url, token)
