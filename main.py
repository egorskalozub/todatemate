from telegram.ext import Updater
import handlers
import config

def main():
    updater = Updater(token=config.TELEGRAM_API_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add handlers
    handlers.register(dp)

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
