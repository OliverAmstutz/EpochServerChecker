import signal
import sys
import time

import schedule

import config
from discordNotify import send_discord_message
from discord_message_service import DiscordMessageService
from serverStatus import is_server_online

discord_service = DiscordMessageService()

def job():
    online, status_enum = is_server_online()
    discord_service.post_or_edit(status_enum)

def shutdown_handler(signum, frame):
    goodbye_message = "⚠️ Scheduler script is shutting down now."
    print(goodbye_message)
    send_discord_message(goodbye_message)
    sys.exit(0)

def startup_handler():
    startup_message = "✅ Scheduler script started successfully."
    print(startup_message)
    send_discord_message(startup_message)

def run_scheduler():
    signal.signal(signal.SIGINT, shutdown_handler)
    startup_handler()

    job()

    config_values = config.load_config()
    scheduler_interval = config_values['SCHEDULER_INTERVAL_SECONDS']
    schedule.every(scheduler_interval).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

