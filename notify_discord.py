import requests
import socket
import os
import datetime
import netifaces as ni


with open("webhook_url.txt") as f:
    webhook_url = f.read()
header = "Content-Type: application/json"


def getIPaddress(nface: str) -> str:
    """
    Get IPv4 Address of NIC.

    Args:
        nface str: NIC Name

    Returns:
        IP Address v4
    """

    return ni.ifaddresses(nface)[ni.AF_INET][0]["addr"]


def main():

    hostname = socket.gethostname()
    bot_usernm = f"{hostname} notification"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M%S%z")

    data = {
        "username": bot_usernm,
        "embeds": [
            {
                "title": "Login notification",
                "description": f'{os.getenv("PAM_USER")} logged in to {hostname} from {os.getenv("PAM_RHOST")}'
                f'({getIPaddress("en01")}, {getIPaddress("ts01")})',
                "color": 0x248046,
                "timestamp": timestamp
            },
        ],
    }

    requests.post(webhook_url, json=data)


if __name__ == "__main__":
    main()
