# ChiBot 🥀 — The Unhinged Dad Joke Bot

chibot is a Telegram bot with full Gen Z brainrot energy. it's giving unhinged aunty at a family function. it tells dad jokes, but like they're a trauma response. 🥀✨🫠

## Features 🥀
- `/joke` — get a fresh, terrible dad joke.
- `/roast <topic>` — roast literally anything (or anyone).
- `/vibe` — check chibot's current emotional state.
- **Natural Conversation** — talk to chibot directly; it uses Groq's Llama 3.3 for chaotic replies.
- **Asynchronous & Fast** — built with `python-telegram-bot` and `AsyncGroq` for zero lag.

## Tech Stack ✨
- **Language:** Python 3.14+
- **Bot Framework:** [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- **AI Engine:** [Groq](https://groq.com/) (using `llama-3.3-70b-versatile`)
- **Environment:** `python-dotenv` for secret management.

## Setup Instructions 💀

### 1. Prerequisites
- Python 3.10 or higher.
- A Telegram Bot Token (get it from [@BotFather](https://t.me/Botfather)).
- A Groq API Key (get it from the [Groq Console](https://console.groq.com/)).

### 2. Installation
Clone the repo and navigate to the project folder:
```bash
git clone <your-repo-url>
cd Telegram_bot
```

### 3. Environment Variables
Create a `.env` file in the root directory and add your credentials:
```env
TOKEN=your_telegram_bot_token
BOT_USERNAME=@your_bot_username
GROQ_API_KEY=your_groq_api_key
```

### 4. Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 5. Run the Bot
```bash
python3 main.py
```

## Disclaimer 🥀
chibot speaks in lowercase, uses way too many emojis, and is perpetually going through it. it will not apologize for its behavior. 💀

## License
MIT
