from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level = logging.INFO, filename = 'bot.log')

def main():
    updater = Updater('312257148:AAEVrE_YJ8Wp8iTr70q5_zIXrIO0uwD3bTY')


    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    updater.start_polling()
    updater.idle()


def greet_user(bot,update):
    text = 'Дорогая, я перезвоню'
    print(text)
    print(update)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

main()