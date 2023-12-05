from telegram import Update
from telegram.ext import CallbackContext
import bot_logic

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! Use /help to get help.')

def help(update: Update, context: CallbackContext):
    bot_logic.send_help_button(update, context)
    

