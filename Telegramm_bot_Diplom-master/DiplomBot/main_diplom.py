import telebot
from telebot import types
import config_diplom
from parsing_currency import *
from parsing_afisha2 import *
from parsing_weather import *


bot = telebot.TeleBot(config_diplom.API_TOKEN)

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)   # кнопки снизу
btn_currency = types.KeyboardButton('Курсы валют')
btn_weather = types.KeyboardButton('Погода')
btn_kino = types.KeyboardButton('Кино')
markup_menu.add(btn_currency, btn_weather, btn_kino)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "ПриВет, Жми на кнопку!", reply_markup=markup_menu)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Курсы валют':
        bot.send_message(message.chat.id, 'Курс валют на сегодня:')
        bot.send_message(message.chat.id, 'Евро - {0}'.format(get_money_euro()))
        bot.send_message(message.chat.id, 'Доллара США - {0}'.format(get_money_usd()))
        bot.send_message(message.chat.id, 'Росс. рубля - {0}'.format(get_money_rus()))
        bot.send_message(message.chat.id, 'Болгарского льва - {0}'.format(get_money_bgn()))
        bot.send_message(message.chat.id, 'Гривны - {0}'.format(get_money_uah()))
        bot.send_message(message.chat.id, 'Польских Злотых - {0}'.format(get_money_pln()))
    elif message.text == 'Кино':
        bot.send_message(message.chat.id, 'Сегодня в кино:')
        bot.send_message(message.chat.id, '{0}'.format(link0()))
        bot.send_message(message.chat.id, '{0}'.format(link1()))
        bot.send_message(message.chat.id, '{0}'.format(link2()))
        bot.send_message(message.chat.id, '{0}'.format(link3()))
        bot.send_message(message.chat.id, '{0}'.format(link4()))
        bot.send_message(message.chat.id, '{0}'.format(link5()))
        bot.send_message(message.chat.id, '{0}'.format(link6()))
        bot.send_message(message.chat.id, '{0}'.format(link7()))
        bot.send_message(message.chat.id, '{0}'.format(link8()))
        bot.send_message(message.chat.id, '{0}'.format(link9()))
        bot.send_message(message.chat.id, '{0}'.format(link10()))
        bot.send_message(message.chat.id, '{0}'.format(link11()))
    elif message.text == 'Погода':
        bot.send_message(message.chat.id, 'Погода в Минске на ближайшие 24 часа:')
        for temp, date in zip(Weather_temp(), Weather_day()):
            bot.send_message(message.chat.id, '{0} - {1} C'.format(date, round(temp)))


if __name__ == '__main__':
    bot.polling(none_stop=True)
