import os
from telethon import TelegramClient, events

# Get credentials from environment variables
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']

# Target channel, trigger word, receiver, and message
channel_username = 'Idreez_01'
trigger_phrase = 'first to send'
receiver_username = '@Idreez_03'
message_to_send = "9049164098\nOpay\nOPEYEMI TOLULOPE JOSEPH"

# Start the user session
client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(chats=channel_username))
async def handler(event):
    if trigger_phrase in event.raw_text.lower():
        await client.send_message(receiver_username, message_to_send)
        print("✅ Trigger detected. Message sent.")

async def main():
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
