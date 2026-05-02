from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import CHIMU_BOT_USERNAME

# 🚀 START
def start(update, context):
    update.message.reply_text("👋 Send movie name bhau!")

# 🔍 SEARCH + BUTTON
def search(update, context):
    query = update.message.text.lower().strip()

    # movie_id generate (must match Bot2)
    movie_id = query.replace(" ", "_")

    # Chimu Bot link
    link = f"https://t.me/{CHIMU_BOT_USERNAME}?start={movie_id}"

    keyboard = [
        [InlineKeyboardButton("🎬 Get Movie", url=link)]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        f"🔍 Found: {query}",
        reply_markup=reply_markup
    )
