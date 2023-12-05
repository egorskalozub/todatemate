from telegram.ext import CommandHandler, MessageHandler, Filters
import bot_logic

def start(update, context):
    # Handle start command
    bot_logic.handle_start(update, context)

def register(dp):
    dp.add_handler(CommandHandler("start", start))
    # Add more handlers
