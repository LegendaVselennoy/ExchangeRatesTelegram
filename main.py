import telebot
from pycbrf import ExchangeRates
from datetime import datetime

bot=telebot.TeleBot('Token')

@bot.message_handler(commands=['start'])
def start(message):
    markup=telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn1=telebot.types.KeyboardButton('USD')
    itembtn2=telebot.types.KeyboardButton('EUR')
    markup.add(itembtn1,itembtn2)
    bot.send_message(chat_id=message.chat.id,text="<b>Выберите валюту</b>",reply_markup=markup,parse_mode="html")

@bot.message_handler(content_types=['text'])
def message(message):
      message_norm=message.text.strip().lower()

      if message_norm in ['usd','eur']:
        rates=ExchangeRates(datetime.now())
        bot.send_message(chat_id=message.chat.id,text=f"<b>1 {message_norm.upper()} равен {float(rates[message_norm.upper()].rate)} рубля</b>",parse_mode="html")

bot.polling(none_stop=True)