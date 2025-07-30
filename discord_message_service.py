import time

from discordNotify import send_discord_message, edit_discord_message

class DiscordMessageService:
    def __init__(self):
        self.message_id = None
        self.last_message_content = None
        self.last_message_time = None
        self.recent_message = None

    def post_or_edit(self, status_enum):
        current_time = time.time()
        self._update_timer_if_status_changed(status_enum, current_time)

        minutes_since_last = int((current_time - self.last_message_time) / 60)
        message_text = self._format_message(status_enum, minutes_since_last)

        if self.last_message_content != status_enum:
            self._send_new_message(status_enum, message_text)
        else:
            self._edit_existing_message_if_needed(message_text)

    def _update_timer_if_status_changed(self, status_enum, current_time):
        if self.last_message_content != status_enum:
            self.last_message_time = current_time

    @staticmethod
    def _format_message(status_enum, minutes):
        return status_enum.message.format(minutes=minutes)

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