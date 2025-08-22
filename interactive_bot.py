import requests
import json
import time

# --- Interactive Webex Bot ---
# Listens for a '/info' command and replies.

# !!! REPLACE THESE WITH YOUR BOT'S TOKEN AND YOUR ROOM ID !!!
BOT_ACCESS_TOKEN = "ACCESS_TOKEN"
ROOM_ID = "ROOM_ID"
BOT_EMAIL = "BOT_NAME@webex.bot" # IMPORTANT: Put your bot's email here

headers = {
    "Authorization": f"Bearer {BOT_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def get_latest_message():
    """Fetches the latest message from the Webex room."""
    url = f"https://webexapis.com/v1/messages?roomId={ROOM_ID}&max=1"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    messages = response.json().get("items")
    return messages[0] if messages else None

def post_message(text):
    """Posts a message to the Webex room."""
    url = "https://webexapis.com/v1/messages"
    payload = {"roomId": ROOM_ID, "text": text}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response.raise_for_status()
    print("Reply sent successfully!")

# --- Main Loop to listen for commands ---
last_message_id = None 

print(f"Bot is running in room {ROOM_ID}... Waiting for commands.")
while True:
    try:
        latest_message = get_latest_message()
        
        if latest_message and latest_message.get("id") != last_message_id:
            last_message_id = latest_message.get("id")
            
            # Ignore messages from the bot itself
            if latest_message.get("personEmail") != BOT_EMAIL:
                message_text = latest_message.get("text", "").lower()
                print(f"New message received: '{message_text}'")

                # Check for the "/info" command
                if "/info" in message_text:
                    reply = "Hello! I am a bot built to demonstrate Python and API skills for a Cisco internship. I am ready to help!"
                    post_message(reply)
        
        time.sleep(5) # Wait 5 seconds before checking again
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        time.sleep(15)
    except KeyboardInterrupt:
        print("\nBot shutting down.")
        break
