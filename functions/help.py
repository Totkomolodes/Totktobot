from telebot import types
from config import bot


def help_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start_0 = types.KeyboardButton("/start")
    lib = types.KeyboardButton("/library")
    help_0 = types.KeyboardButton("/help")
    start_keeping = types.KeyboardButton("/start_keeping")
    markup.add(start_0, lib, start_keeping, help_0)
    bot.send_message(message.chat.id, f"/library - ссылка на библиотеку telebot\n"
                                      f'/start - команда приветствия\n'
                                      f'/start_keeping - команда для работы с файлами на Яндекс Диске бота.\n'
                     , parse_mode="html", reply_markup=markup)

# @bot.message_handler(commands=["author"])
# def author(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Перейти", url="https://vk.com/niggers13371"))
#     bot.send_message(message.chat.id, "Cсылка на мой ВК", parse_mode="html", reply_markup=markup)

#
# markup_0 = types.InlineKeyboardMarkup()
# markup_0.add(types.InlineKeyboardButton(text="загрузить на диск", callback_data='qwerty'))
# markup_0.add(types.InlineKeyboardButton(text="скачать с диска", callback_data='qwerty'))
# markup_0.add(types.InlineKeyboardButton(text="удалить с диска", callback_data='qwerty'))
# bot.send_message(message.chat.id, question_message_0, parse_mode="html", reply_markup=markup_0)
# bot.register_next_step_handler(message, determinant_0)
# def my_videos(message):
#     def slicing(message1):
#         if message1.text == "1":
#             cs_vid = open(cs_path, "rb")
#             bot.send_video(message1.chat.id, cs_vid)
#         elif message1.text == "2":
#             tundra_vid = open(tundra_path, "rb")
#             bot.send_video(message1.chat.id, tundra_vid)
#         elif message1.text == "3":
#             ets_vid = open(ets_path, "rb")
#             bot.send_video(message1.chat.id, ets_vid)
#         else:
#             bot.send_message(message.chat.id, "Ошибка ввода!", parse_mode="html")
#
#     movie_text = f"Из какой игры ты хочешь увидеть момент?(1:CS, 2:War Thunder, 3:ETS)"
#     bot.send_message(message.chat.id, movie_text, parse_mode="html")
#     bot.register_next_step_handler(message, slicing)
#
