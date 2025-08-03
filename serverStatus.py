import socket
from enum import Enum

from config import load_config


class ServerStatus(Enum):
    BOTH_ONLINE = "✅ Both LOGIN and KAZAN server are ONLINE (Login: {login_minutes} min, Kazan: {kazan_minutes} min)"
    LOGIN_ONLY = "⚠️ Only LOGIN server is ONLINE (Login: {login_minutes} min)"
    KAZAN_ONLY = "⚠️ Only KAZAN server is ONLINE (Kazan: {kazan_minutes} min)"
    BOTH_OFFLINE = "❌ Both LOGIN and KAZAN server are OFFLINE"

    def format_message(self, login_minutes, kazan_minutes):
        return self.value.format(login_minutes=login_minutes, kazan_minutes=kazan_minutes)


def get_combined_server_status():
    config = load_config()
    login_host = config['LOGIN_IP']
    login_port = config['LOGIN_PORT']
    kazan_host = config['KAZAN_IP']
    kazan_port = config['KAZAN_PORT']

    login_online = _is_server_online(login_host, login_port)
    kazan_online = _is_server_online(kazan_host, kazan_port)

    if login_online and kazan_online:
        return ServerStatus.BOTH_ONLINE
    elif login_online:
        return ServerStatus.LOGIN_ONLY
    elif kazan_online:
        return ServerStatus.KAZAN_ONLY
    else:
        return ServerStatus.BOTH_OFFLINE


def _is_server_online(host, port, timeout=1):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False
