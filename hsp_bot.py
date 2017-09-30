# -*- coding: utf-8 -*-

from config import MAIRE_TOKEN
import telebot
import constants

bot = telebot.TeleBot(MAIRE_TOKEN)



# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message):
#     bot.send_message(message.chat.id, message.text)

@bot.message_handler(commands='/start')
def start_handler(message):
    text = 'Начните работу с ботом со слов Дорогая, я перезвоню'
    bot.send_message(message.chat.id,text)


@bot.message_handler(commands='/wordcount')
def wordcount(message):
    text = message.text.split()
    bot.send_message(message.chat.id,len(text)-1)

@bot.message_handler(commands='/calc')
def calculator(message):
    text = message.text
    calc_symbols = ['+','-','*',':','/']
    operator = ''
    text = text.replace('/calc', ' ')
    flag = True

    for i in calc_symbols:
        if text.find(i)!=-1:
            operator = i
            digits = text.split(i)
            try:
                digits[0] =int( digits[0])
            except ValueError:
                result = constants.type_error
                flag = False
            if flag:
                try:
                    digits[1]=digits[1][0::len(digits[1])]
                    digits[1] = int(digits[1])
                except ValueError:
                    result = constants.type_error
                    flag = False



    if flag:
        if operator == '+':
            result = digits[0]+digits[1]
        elif operator == '-':
            result = digits[0] - digits[1]
        elif operator == '*':
            result = digits[0]*digits[1]
        elif (operator == ':' or operator=='/'):
            result = digits[0]/digits[1]
        else:
            result = 'сорян, что-то пошло не так'

    result = str(result)
    bot.send_message(message.chat.id, result)







if __name__ == '__main__':
    bot.polling(none_stop=True)