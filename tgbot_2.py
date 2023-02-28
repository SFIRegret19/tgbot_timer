bot_token = '5157864036:AAHUbQC71KYB7u-lrsqP1C4meEDlD4TCYtg'
from telegram import ReplyKeyboardMarkup, Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext, \
    CallbackQueryHandler
#from credits import bot_token

bot = Bot(token=bot_token)
updater = Updater(token=bot_token)
dispatcher = updater.dispatcher


def alarm(context):
    job = context.job
    context.bot.send_message(job.context, 'ДЗЗЗЫНЬ! Время прошло')


def start(update, context):
    keyboard = [
        [InlineKeyboardButton('Таймер 5', callback_data='1'), InlineKeyboardButton('Таймер 10', callback_data='2')]
    ]

    update.message.reply_text('Нажми на кнопку', reply_markup=InlineKeyboardMarkup(keyboard))


def button(update, context):
    query = update.callback_query
    query.answer()
    if query.data == '1':
        context.job_queue.run_once(alarm, 5, context=update.effective_chat.id, name=str(update.effective_chat.id))
        context.bot.send_message(update.effective_chat.id, 'Таймер поставили')
    elif query.data == '2':
        context.job_queue.run_once(alarm, 10, context=update.effective_chat.id, name=str(update.effective_chat.id))
        context.bot.send_message(update.effective_chat.id, 'Таймер поставили')


start_handler = CommandHandler('start', start)
button_handler = CallbackQueryHandler(button)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(button_handler)

updater.start_polling()
updater.idle()
