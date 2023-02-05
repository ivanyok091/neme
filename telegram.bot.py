import telebot
import requests

bot = telebot.TeleBot('5501488079:AAEPH7EL2SdrKxg7BgF4s0Dkrv8F8Ut-2QM')

def ipfunc(ip):
    try:
        req = requests.get(f"http://ip-api.com/json/{ip}").json()
        return f"""
        Подключение: {req['status']}
        Страна: {req['country']}
        Город: {req['city']}
        Провайдер: {req['isp']}
        Часовой пояс: {req['timezone']}
        """
    except KeyError:
        return 'Это не IP адрес'

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'привет {0.first_name} я бот который узнает где ты находишься по айпи'
                          'бот был создан для агро школьников из майнкравта'.format(message.from_user))

@bot.message_handler(commands=['ip'])
def ipcommand(message):
    bot.reply_to(message,'кажите ваш айпэ')
    bot.register_next_step_handler(message, ipinfo)

def ipinfo(message):
    bot.reply_to(message, ipfunc(message.text))

bot.polling(none_stop=True, interval=0)