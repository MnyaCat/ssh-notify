import requests
import socket
import os
import datetime


with open("webhook_url.txt") as f:
    webhook_url = f.read().strip()
header = "Content-Type: application/json"


def main():

    hostname = socket.gethostname()
    bot_usernm = f"{hostname} notification"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M%S%z")

    data = {
        "username": bot_usernm,
        "embeds": [
            {
                "title": "Login notification",
                "description": f'{os.getenv("PAM_USER")} logged in to {hostname} from {os.getenv("PAM_RHOST")}',
                "color": 0x248046,
                "timestamp": timestamp
            },
        ],
    }

    requests.post(webhook_url, json=data)


if __name__ == "__main__":
    main()
