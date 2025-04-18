from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_TOKEN' with the API token from BotFather
TOKEN = "7838020402:AAFcpRVk-8Mk3Dmrye5WGdJMKj8OMJDGZug"

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am your first Telegram bot!')

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()