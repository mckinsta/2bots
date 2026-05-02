from telegram.ext import Application, MessageHandler, CommandHandler, filters
from config import TOKEN
from handlers import receive_video, save_id, start

def main():
    app = Application.builder().token(TOKEN).build()

    # 🎥 video handler
    app.add_handler(MessageHandler(filters.VIDEO | filters.Document.ALL, receive_video))

    # 📝 text handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, save_id))

    # 🚀 start command
    app.add_handler(CommandHandler("start", start))

    print("🔥 Chimu Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
