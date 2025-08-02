import time

from discordNotify import send_discord_message, edit_discord_message
from serverStatus import ServerStatus


class DiscordMessageService:
    def __init__(self):
        self.message_id = None
        self.last_message_content = None
        self.recent_message = None
        self.last_login_time = None
        self.last_kazan_time = None

    def post_or_edit(self, status_enum):
        current_time = time.time()
        self._update_online_timers(status_enum, current_time)

        login_minutes = self._calculate_minutes(self.last_login_time, current_time)
        kazan_minutes = self._calculate_minutes(self.last_kazan_time, current_time)

        message_text = status_enum.format_message(login_minutes, kazan_minutes)

        if self.last_message_content != status_enum:
            self._send_new_message(status_enum, message_text)
        else:
            self._edit_existing_message_if_needed(message_text)

    def _update_online_timers(self, new_status, current_time):
        old_status = self.last_message_content

        # LOGIN server
        was_login_online = old_status in [ServerStatus.BOTH_ONLINE, ServerStatus.LOGIN_ONLY]
        is_login_online = new_status in [ServerStatus.BOTH_ONLINE, ServerStatus.LOGIN_ONLY]

        if is_login_online and not was_login_online:
            self.last_login_time = current_time
        elif not is_login_online:
            self.last_login_time = current_time

        # KAZAN server
        was_kazan_online = old_status in [ServerStatus.BOTH_ONLINE, ServerStatus.KAZAN_ONLY]
        is_kazan_online = new_status in [ServerStatus.BOTH_ONLINE, ServerStatus.KAZAN_ONLY]

        if is_kazan_online and not was_kazan_online:
            self.last_kazan_time = current_time
        elif not is_kazan_online:
            self.last_kazan_time = current_time

    @staticmethod
    def _calculate_minutes(last_time, current_time):
        if last_time is None:
            return 0
        return int((current_time - last_time) / 60)

    def _send_new_message(self, status_enum, message_text):
        self.message_id = send_discord_message(message_text)
        self.last_message_content = status_enum
        self.recent_message = message_text

    def _edit_existing_message_if_needed(self, message_text):
        if self.message_id is not None:
            if self.recent_message != message_text:
                edit_discord_message(self.message_id, message_text)
                self.recent_message = message_text
        else:
            print("This should never happen: message_id is None but last_message_content is equal to status_enum.")
            self.message_id = send_discord_message(message_text)
            self.recent_message = message_text
