import os

# config environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_USER_IDS = os.getenv("TELEGRAM_USER_IDS")
CLAUDE_SECRET_KEY = os.getenv("CLAUDE_SECRET_KEY")
BARD_SECRET_KEY = os.getenv("BARD_SECRET_KEY")

telegram_token = TELEGRAM_BOT_TOKEN
telegram_username = [item.strip() for item in TELEGRAM_USER_IDS.split(",")]
claude_api = CLAUDE_SECRET_KEY
bard_api = BARD_SECRET_KEY
