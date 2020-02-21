import constants
import pyowm
import telebot

bot = telebot.TeleBot(constants.token)

def weather(message):
    city = message.text
    owm = pyowm.OWM(constants.OWMKEY, language='ru')

    observation = owm.weather_at_place(city)
    w = observation.get_weather()

    temperature = w.get_temperature("celsius")["temp"]
    humidity = w.get_humidity()
    wind = w.get_wind()["speed"]
    desc = w.get_detailed_status()

    bot.send_message(message.chat.id, "В городе " + str(city) + " сейчас " + str(desc) + ".")
    bot.send_message(message.chat.id, "Температура: " + str(temperature) + "°C.")
    bot.send_message(message.chat.id, "Ветер: " + str(wind) + "м/с.")
    bot.send_message(message.chat.id, "Влажность: " + str(humidity) + "%.")
