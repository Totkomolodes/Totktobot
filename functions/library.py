from telebot import types
from config import bot

def library_which_i_used(message):
    markup = types.InlineKeyboardMarkup()
    markup2 = types.InlineKeyboardMarkup()
    markup2.add(types.InlineKeyboardButton("Перейти", url="https://pypi.org/project/yadisk/"))
    markup.add(types.InlineKeyboardButton("Перейти", url="https://pypi.org/project/pyTelegramBotAPI/"))
    bot.send_message(message.chat.id, "Посети сайт библиотеки telebot", parse_mode="html", reply_markup=markup)
    bot.send_message(message.chat.id, "Посети сайт библиотеки yadisk", parse_mode="html", reply_markup=markup2)