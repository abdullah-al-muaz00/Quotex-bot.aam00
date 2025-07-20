# AAM Quotex Signal Bot

This is a Telegram bot for Quotex binary trading signals.

## Features

- Sends signals for 10 market pairs every 3 minutes
- Sends signal and result messages with fancy formatting
- Integrates Forex Factory news filter (to be implemented)
- Includes a Flask web server with `/test` route to send test messages
- Configurable via `.env` file

## Setup

1. Rename `.env.example` to `.env` and set your `BOT_TOKEN` and `CHAT_ID`.
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the bot:

```
python web.py
```

## Deployment

Deploy on Railway or any other VPS with environment variables set.

## Usage

- Visit `/test` route to send a test message to your Telegram.
