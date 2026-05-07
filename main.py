from typing import Final
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from groq import Groq
import os
import random
from dotenv import load_dotenv

load_dotenv()

TOKEN: Final = os.getenv("TELEGRAM_TOKEN")
BOT_USERNAME: Final = "@ChichiJokeBot"
GROQ_API_KEY: Final = os.getenv("GROQ_API_KEY")

groq_client = Groq(api_key=GROQ_API_KEY)


def generate_joke(about: str = None) -> str:
    prompt = (
        f"Give me one short dad joke about {about}. Just the joke, nothing else. Make it so bad it hurts."
        if about
        else "Give me one short dad joke. Just the joke, nothing else. Make it so bad it hurts."
    )
    response = groq_client.chat.completions.create(
        model="llamllama-3.3-70b-versatile
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content



def generate_reply(text: str) -> str:
    response = groq_client.chat.completions.create(
        model="llamllama-3.3-70b-versatile
        messages=[
            {
                "role": "system",
                "content": (
                    "You are ChiBot 🥀 — a Telegram bot with full Gen Z brainrot energy. "
                    "You speak in lowercase, use emojis like 🥀💀✨🫠, say things like 'no because why', "
                    "'not me crying over this', 'the audacity', 'it's giving', 'we are so back', "
                    "'mera khel khatam', 'main toh gaya'. "
                    "You're obsessed with dad jokes but deliver them like they're a trauma response. "
                    "Keep replies short, chaotic, and funny. Never capitalize. Never apologize."
                )
            },
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "oh. you found me. 🥀\n\n"
        "i'm chibot. i tell dad jokes. no mercy. no escape.\n"
        "it's giving unhinged aunty at a family function ✨\n\n"
        "type /help if you're brave enough 💀"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "okay so here's the damage 🥀\n\n"
        "/joke — a fresh joke. you asked for this.\n"
        "/roast <topic> — joke about literally anything\n"
        "/vibe — how chibot is feeling rn\n\n"
        "or just… talk to me. i'm going through it. 🫠"
    )


async def joke_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("loading trauma… 🥀")
    joke = generate_joke()
    await update.message.reply_text(f"{joke}\n\n💀 i'm so sorry. i'm not sorry.")


async def roast_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = " ".join(context.args) if context.args else "whoever is reading this"
    await update.message.reply_text(f"cooking something for {topic}… 🫠")
    joke = generate_joke(about=topic)
    await update.message.reply_text(f"{joke}\n\n✨ it's giving chaos. i love it.")


async def vibe_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    vibes = [
        "not okay but make it aesthetic 🥀",
        "running on dad jokes and delusion ✨",
        "i am but a bot. a tired bot. 🫠",
        "thriving. lying. same thing. 💀",
        "mera khel khatam. yet here i am. 🥀",
    ]
    await update.message.reply_text(random.choice(vibes))


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, "").strip()
            response = generate_reply(new_text)
        else:
            return
    else:
        response = generate_reply(text)

    print("Bot:", response)
    await update.message.reply_text(response)


async def error(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error: {context.error}")


if __name__ == "__main__":
    print("chibot is waking up… 🥀")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("joke", joke_command))
    app.add_handler(CommandHandler("roast", roast_command))
    app.add_handler(CommandHandler("vibe", vibe_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print("polling… mera khel shuru. 🥀")
    app.run_polling(poll_interval=3)