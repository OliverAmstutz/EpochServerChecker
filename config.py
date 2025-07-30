import os
from dotenv import load_dotenv

def load_config():
    load_dotenv(override=True)

    discord_webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
    url = os.getenv('URL')
    port = os.getenv('PORT')
    scheduler_interval_seconds = os.getenv('SCHEDULER_INTERVAL_SECONDS')


    if not discord_webhook_url:
        raise ValueError("Missing DISCORD_WEBHOOK_URL in .env or environment")

    if not url:
        raise ValueError("Missing URL in .env or environment")

    if not port:
        raise ValueError("Missing PORT in .env or environment")

    if not scheduler_interval_seconds:
        raise ValueError("Missing SCHEDULER_INTERVAL_SECONDS in .env or environment")

    port = int(port)
    scheduler_interval_seconds = int(scheduler_interval_seconds)

    return {
        'DISCORD_WEBHOOK_URL': discord_webhook_url,
        'URL': url,
        'PORT': port,
        'SCHEDULER_INTERVAL_SECONDS': scheduler_interval_seconds
    }