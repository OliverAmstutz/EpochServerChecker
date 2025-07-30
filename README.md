# Project Epoch Server Monitor

This Python script monitors the status of the **Project Epoch** server and sends real-time updates to a Discord channel using webhooks.

## 🚀 Features

- Periodically checks server status.
- Sends status updates to Discord via webhook.
- Easy setup and deployment.
- Secrets handled via `.env` file.

![img.png](assets/DiscordOutputExample.png)

---

## 📦 Requirements

- Python **3.8+**
- Dependencies listed in `requirements.txt`

---

## 🛠️ Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-user/project-epoch-monitor.git
   cd project-epoch-monitor
   
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   
3. **setup your discord webhook**

    See this link: [Discord Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)

4. **Update your DISCORD_WEBHOOK_URL in the .env file**
    ```text
    DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/your_webhook_url
   ```

   The structure should look like this:
    ```bash
   .
    ├── main.py              # Entry point of the application
    ├── .env                 # Contains the Discord webhook URL (not committed)
    ├── requirements.txt     # Python dependencies
    └── README.md            # This file
   
5. **Run the script**
    ```bash
    python main.py