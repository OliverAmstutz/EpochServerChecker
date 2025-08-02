import os

from dotenv import load_dotenv


def load_config():
    load_dotenv(override=True)

    discord_webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
    login_url = os.getenv('LOGIN_URL')
    kazan_url = os.getenv('KAZAN_URL')
    login_port = os.getenv('LOGIN_PORT')
    kazan_port = os.getenv('KAZAN_PORT')
    scheduler_interval_seconds = os.getenv('SCHEDULER_INTERVAL_SECONDS')

    if not discord_webhook_url:
        raise ValueError("Missing DISCORD_WEBHOOK_URL in .env or environment")

    if not login_url:
        raise ValueError("Missing login URL in .env or environment")

    if not login_port:
        raise ValueError("Missing login PORT in .env or environment")

    if not kazan_url:
        raise ValueError("Missing Kazan URL in .env or environment")

    if not kazan_port:
        raise ValueError("Missing Kazan PORT in .env or environment")

    if not scheduler_interval_seconds:
        raise ValueError("Missing SCHEDULER_INTERVAL_SECONDS in .env or environment")

    login_port = int(login_port)
    scheduler_interval_seconds = int(scheduler_interval_seconds)

    return {
        'DISCORD_WEBHOOK_URL': discord_webhook_url,
        'LOGIN_URL': login_url,
        'KAZAN_URL': kazan_url,
        'LOGIN_PORT': login_port,
        'KAZAN_PORT': kazan_port,
        'SCHEDULER_INTERVAL_SECONDS': scheduler_interval_seconds
    }
