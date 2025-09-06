# Telegram UserBot for Render Deployment

This is a simple Telegram userbot built using Telethon. It monitors a public channel for a trigger phrase and sends a message to a specific user when triggered.

## 🔧 How It Works

- **Monitors**: @Idreez_01
- **Trigger**: "first to send"
- **Responds to**: @Idreez_03
- **Message Sent**:
  ```
  9049164098
  Opay
  OPEYEMI TOLULOPE JOSEPH
  ```

## 🛠 Deployment Instructions on Render

1. Fork or clone this repository.
2. Go to [https://railway.com](https://railway.com).
3. Create a **New Web Service**.
4. Connect your GitHub and select this repo.
5. Set environment variables:
   - `API_ID` → your Telegram API ID
   - `API_HASH` → your Telegram API Hash
6. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python main.py`

The bot will stay online and respond when the trigger phrase is seen in the target channel.
