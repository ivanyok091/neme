import telebot
import requests

    bot.register_next_step_handler(message, ipinfo)

def ipinfo(message):
    bot.reply_to(message, ipfunc(message.text))


bot.polling(none_stop=True, interval=0)
