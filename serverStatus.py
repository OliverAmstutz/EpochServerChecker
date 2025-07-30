import socket
from enum import Enum

from config import load_config


def is_server_online(timeout=1):
    config = load_config()
    host = config['URL']
    port = config['PORT']
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True, ServerStatus.ONLINE
    except OSError as e:
        return False, ServerStatus.OFFLINE

class ServerStatus(Enum):
    ONLINE = ("✅ Server is ONLINE since {minutes} min", 0)
    OFFLINE = ("❌ Server is OFFLINE since {minutes} min", 0)

    def format_message(self, minutes):
        return self.value.format(minutes=minutes)

    def __init__(self, message, minutes):
        self.message = message
        self.minutes = minutes
