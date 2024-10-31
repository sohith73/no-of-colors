import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import requests

TELEGRAM_BOT_TOKEN = "7233143377:AAF-PkwuatMgu_tf08H88EeHLudiI2HrQ6w"


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def send_telegram_message(TELEGRAM_BOT_TOKEN, chat_id, ):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': "Hello world from BusiBud"
    }
    response = requests.post(url, json=payload)
    return response.json()


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    message_text = update.message.text
    chat_id = update.message.chat_id
    if(chat_id):
        send_telegram_message(TELEGRAM_BOT_TOKEN,chat_id)
    print(f"@{user.username}: {message_text}")
    print(f"Chat-ID: {chat_id}")

def main():
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    application.add_handler(message_handler)

    application.run_polling()

if __name__ == "__main__":
    main()
