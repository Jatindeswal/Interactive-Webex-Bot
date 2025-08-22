# Interactive Cisco Webex Bot

## Overview

This project is a Python-based interactive chatbot for the **Cisco Webex** platform. It was developed to showcase practical software engineering skills, including API integration, real-time application logic, and an understanding of Cisco's collaboration ecosystem.

The bot actively listens for messages in a Webex space and is programmed to respond to specific user commands, turning it from a simple script into a functional, automated application.

## Features ✨

- **Real-Time Listening:** The bot continuously monitors a Webex space for new messages.
- **Command-Based Interaction:** It can parse messages and identify specific commands (e.g., `/info`).
- **Automated Responses:** The bot posts pre-programmed replies back to the space when a valid command is received.
- **Ignores Self-Messages:** Logic is included to prevent the bot from replying to its own messages and creating a loop.

## Setup Instructions

To run this bot yourself, you will need to provide your own Webex credentials.

1.  **Clone the Repository:**
    ```sh
    git clone <your_repository_link_here>
    cd <repository_name>
    ```

2.  **Install Dependencies:**
    The project uses the `requests` library.
    ```sh
    pip install requests
    ```

3.  **Get Credentials:**
    - **Bot Access Token:** Go to the [Webex for Developers portal](https://developer.webex.com/), create a new bot, and copy your **Bot Access Token**.
    - **Room ID:** Create a Webex space, invite your bot, and use the "List Rooms" API tool on the developer portal to find the **Room ID** for that space.
    - **Bot Email:** Note the email address of your bot (e.g., `mybot@webex.bot`).

4.  **Update the Script:**
    Open the `interactive_bot.py` file and replace the placeholder values at the top with your credentials:
    - `BOT_ACCESS_TOKEN`
    - `ROOM_ID`
    - `BOT_EMAIL`

## How to Run 🚀

Once the setup is complete, run the bot from your terminal:

```sh
python interactive_bot.py
