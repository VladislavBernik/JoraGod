import constants
import telebot
import requests
import currency
import weather
from telebot import types

bot = telebot.TeleBot(constants.token)
response = requests.get(constants.url).json()

markup = types.ReplyKeyboardMarkup(True, True)

btn_currency = types.KeyboardButton('Курсы валют')
btn_weather = types.KeyboardButton('Погода')

markup.add(btn_currency, btn_weather)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, чем я могу помочь?', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    if message.text == 'Курсы валют':
        menu = types.ReplyKeyboardMarkup(True, True)
        btn_usd = types.KeyboardButton('USD')
        btn_eur = types.KeyboardButton('EUR')
        btn_rur = types.KeyboardButton('RUR')
        menu.add(btn_usd, btn_eur, btn_rur)
        msg = bot.send_message(message.chat.id, "Узнать наличный курс ПриватБанка", reply_markup=menu)
        bot.register_next_step_handler(msg, currency.process_coin_step)
    elif message.text == 'Погода':
        city = bot.send_message(message.chat.id, "Какой город Вас интересует?")
        bot.register_next_step_handler(city, weather.weather)

if __name__ == '__main__':
    bot.polling(none_stop=True)