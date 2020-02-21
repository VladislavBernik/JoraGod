from telebot import types
from main import response
import telebot
import constants

bot = telebot.TeleBot(constants.token)

def process_coin_step(message):
    try:
       markup = types.ReplyKeyboardRemove(selective=False)
       for coin in response:
           if (message.text == coin['ccy']):
              bot.send_message(message.chat.id, printCoin(coin['buy'], coin['sale']), reply_markup=markup, parse_mode="Markdown")

    except Exception as e:
       bot.reply_to(message, 'ooops!')

def printCoin(buy, sale):
    '''Вывод курса пользователю'''
    return "💰 *Курс покупки:* " + str(buy) + "\n💰 *Курс продажи:* " + str(sale)

bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()