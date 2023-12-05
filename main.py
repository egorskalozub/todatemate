from telegram.ext import Updater, CommandHandler
import config
import handlers

def main():
    updater = Updater(token=config.TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", handlers.start))
    dp.add_handler(CommandHandler("help", handlers.help))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
