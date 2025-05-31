import os
from dotenv import load_dotenv
from typing import Dict, List

# Load environment variables from .env file
load_dotenv()

# Logging settings
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL = 'INFO'

# Database settings
DB_PATH = "wallet_monitor.db"

# Telegram settings
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', 'YOUR_CHAT_ID')

# Moralis settings
MORALIS_API_KEY = "your key"

# Monitoring settings
POLLING_INTERVAL = 60  # seconds
SIGNIFICANT_CHANGE_THRESHOLD = 0.05  # 5%

# Monitoring Settings
MONITORING_INTERVAL = 300  # seconds (5 minutes)
MAX_RETRIES = 3
RETRY_DELAY = 60  # seconds

# Analysis Settings
MIN_TRANSACTION_VALUE_USD = 100  # Minimum USD value to consider a transaction significant

# Notification Settings
ENABLE_NOTIFICATIONS = True
NOTIFICATION_CHANNELS = {
    "telegram": {
        "enabled": True,
        "bot_token": "our tocken",
        "chat_id": None  # Will be set after /start command
    },
    "discord": {
        "enabled": False,
        "webhook_url": "YOUR_WEBHOOK_URL"
    }
}

# Wallet Settings
TRACKED_WALLETS = [
#Here you need to enter the numbers of the wallets you will be tracking
] 
