import requests

from config import load_config


def send_discord_message(content):
    config = load_config()
    url_with_wait = config['DISCORD_WEBHOOK_URL'] + "?wait=true"
    data = {"content": content}
    response = requests.post(url_with_wait, json=data)
    if response.status_code == 204 or response.status_code == 200:
        response_json = response.json()
        return response_json['id']
    else:
        print("Failed to send message:", response.text)
        return None

def edit_discord_message(message_id, new_content):
    config = load_config()
    url = config['DISCORD_WEBHOOK_URL']
    edit_url = f"{url}/messages/{message_id}"
    data = {"content": new_content}
    response = requests.patch(edit_url, json=data)
    if response.status_code != 200:
        print("Failed to edit message:", response.text)
