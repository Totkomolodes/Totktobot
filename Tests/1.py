import os

import telebot
from telebot import types
from telebot.types import Message
import requests
from telebot.types import ReplyKeyboardMarkup
import yadisk
from yadisk.exceptions import PathNotFoundError
import telebot

success_message = "Файл был удачно установлен в хранилище Яндекс Диска"
question_message = "Отправите файл и укажите его название(document, photo, video, audio)"
question_message_2 = "Укажите полное название вашего файла"
question_message_3 = "Укажите полное название вашего файла, который хотите, чтобы я вам отправил"
remove_path = "C:\\Users\\frien\\Desktop\\Рабочий стол 2(основные файлы)\\Работа\\Проекты(мои)\\TELEGA_BOT\\"
ets_path = "C:\\Users\\frien\\Videos\\Euro Truck Simulator 2\\Срыв анекдота про Ванечку_for_proj.mp4"
tundra_path = "C:\\Users\\frien\\Videos\\War Thunder\\Полет без жопы.mp4"
cs_path = "C:\\Users\\frien\\Videos\\Counter-strike  Global Offensive\\-4_for_proj.mp4"
oAuth_token = "y0_AgAAAABpbRZlAADLWwAAAADfKVNbxaZjwUyBRbuCcfp1Tb_c7ZN4QXY"
TOKEN = "6085480866:AAHG4DA54t6XAf6y8wQlsRaA51_8F5mIAaM"
bot = telebot.TeleBot("6085480866:AAHG4DA54t6XAf6y8wQlsRaA51_8F5mIAaM")
clientID = "62cb5932e44f469a9656d29a6ea98680"
Client_secret = "62b85c818e134bd7a5e3f96ac072056a"
redirect_URI = "https://oauth.yandex.ru/verification_code"
token_me = "y0_AgAAAABpbRZlAAmOAwAAAADfShDgpYojS5UpQVSVsgwfSrk54TYkAl0"

y = yadisk.YaDisk(token=token_me)


@bot.message_handler(commands=["start"])
def start(message):
    message_to_user = f"<b>Привет {message.from_user.first_name}</b> <b>{message.from_user.last_name}!</b>"
    bot.send_message(message.chat.id, message_to_user, parse_mode="html")


@bot.message_handler(commands=["help"])
def help_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    author_0 = types.KeyboardButton("/author")
    start_0 = types.KeyboardButton("/start")
    lib = types.KeyboardButton("/library")
    meme = types.KeyboardButton("/meme")
    help_0 = types.KeyboardButton("/help")
    start_keeping = types.KeyboardButton("/start_keeping")
    markup.add(author_0, start_0, lib, meme, start_keeping, help_0)
    bot.send_message(message.chat.id, f"/library - ссылка на библиотеку telebot\n"
                                      f"/author - ссылки на меня\n"
                                      f'/start - команда приветствия\n'
                                      f'/start_keeping - команда сохранения файлов на Яндекс Диске бота.\n'
                                      f"/meme - команда для просмотра видео\n"
                     , parse_mode="html", reply_markup=markup)


@bot.message_handler(commands=["library"])
def library_which_i_used(message):
    markup = types.InlineKeyboardMarkup()
    markup2 = types.InlineKeyboardMarkup()
    markup2.add(types.InlineKeyboardButton("Перейти", url="https://pypi.org/project/yadisk/"))
    markup.add(types.InlineKeyboardButton("Перейти", url="https://pypi.org/project/pyTelegramBotAPI/"))
    bot.send_message(message.chat.id, "Посети сайт библиотеки telebot", parse_mode="html", reply_markup=markup)
    bot.send_message(message.chat.id, "Посети сайт библиотеки yadisk", parse_mode="html", reply_markup=markup2)


@bot.message_handler(commands=["author"])
def author(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти", url="https://vk.com/niggers13371"))
    bot.send_message(message.chat.id, "Cсылка на мой ВК", parse_mode="html", reply_markup=markup)


@bot.message_handler(content_types=["text"], commands=["meme"])
def my_videos(message):
    def slicing(message1):
        if message1.text == "1":
            cs_vid = open(cs_path, "rb")
            bot.send_video(message1.chat.id, cs_vid)
        elif message1.text == "2":
            tundra_vid = open(tundra_path, "rb")
            bot.send_video(message1.chat.id, tundra_vid)
        elif message1.text == "3":
            ets_vid = open(ets_path, "rb")
            bot.send_video(message1.chat.id, ets_vid)
        else:
            bot.send_message(message.chat.id, "Ошибка ввода!", parse_mode="html")

    movie_text = f"Из какой игры ты хочешь увидеть момент?(1:CS, 2:War Thunder, 3:ETS)"
    bot.send_message(message.chat.id, movie_text, parse_mode="html")
    bot.register_next_step_handler(message, slicing)


@bot.message_handler(commands=["start_keeping"], content_types=["text"])  # хранитель файлов(пока что на комп)
def keeper_of_files_on_yadisk(message):
    def determinant_1(message2):
        if message2.photo is not None:
            downloading_on_computer(message2.photo, message2.caption)
        elif message2.video is not None:
            downloading_on_computer(message2.video, message2.caption)
        elif message2.audio is not None:
            downloading_on_computer(message2.audio, message2.caption)
        elif message2.document is not None:
            downloading_on_computer(message2.document, message2.caption)
        else:
            bot.send_message(message.chat.id, "<b>Я не могу обработать такой формат!</b>", parse_mode="html")

    def determinant_0(message2):
        if message2.text == "загрузить на диск":
            bot.send_message(message.chat.id, question_message, parse_mode="html")  # загрузка на диск
            bot.register_next_step_handler(message, determinant_1)
        elif message2.text == "скачать с диска":
            bot.send_message(message.chat.id, question_message_2, parse_mode="html")  # загрузка с диска
            bot.register_next_step_handler(message, downloading_from_disk)
        elif message2.text == "удалить с диска":
            bot.send_message(message.chat.id, question_message_2, parse_mode="html")  # удаление с диска
            bot.register_next_step_handler(message, deleting)
        else:
            bot.send_message(message.chat.id, "Ошибка ввода", parse_mode="html")

    def negr(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        download = types.KeyboardButton("загрузить на диск")
        upload = types.KeyboardButton("скачать с диска")
        delete = types.KeyboardButton("удалить с диска")

        markup.add(download, upload, delete)
        bot.send_message(message.chat.id, parse_mode="html", reply_markup=markup)

    def determinant_2(message2):
        if message2.photo is not None:
            downloading_on_computer(message2.photo, message2.caption)
        elif message2.video is not None:
            downloading_on_computer(message2.video, message2.caption)
        elif message2.audio is not None:
            downloading_on_computer(message2.audio, message2.caption)
        elif message2.document is not None:
            downloading_on_computer(message2.document, message2.caption)
        else:
            bot.send_message(message.chat.id, "<b>Я не могу обработать такой формат!</b>", parse_mode="html")

    def downloading_on_computer(files, file_name):
        for i in files:
            file_info = bot.get_file(i.file_id)
            response = bot.download_file(file_info.file_path)
            with open(file_name, "wb") as file:
                file.write(response)
        downloading_on_disk(file_name)

    def downloading_from_disk(message2, val):
        try:
            y.download("/" + message2.text, message2.text)  # проверить
            if val == "photo":
                bot.send_photo(message.chat.id, message2.text, parse_mode="html")
            elif val == "video":
                bot.send_video(message.chat.id, message2.text, parse_mode="html")
            elif val == "document":
                bot.send_document(message.chat.id, message2.text, parse_mode="html")
            elif val == "audio":
                bot.send_audio(message.chat.id, message2.text, parse_mode="html")
            else:
                bot.send_message(message.chat.id, "<b>Я не могу обработать такой формат!</b>", parse_mode="html")
        except PathNotFoundError:
            bot.send_message(message.chat.id, "<b>Такой файл не найден</b>", parse_mode="html")

    def deleting(message2):
        try:
            y.remove("/" + message2.text, permanently=True)  # проверить
            bot.send_message(message.chat.id, "<b>Файл удачно удален!</b>", parse_mode="html")
        except PathNotFoundError:
            bot.send_message(message.chat.id, "<b>Такой файл не найден</b>", parse_mode="html")

    def downloading_on_disk(file_name):
        y.upload(file_name, "/" + file_name)
        bot.send_message(message.chat.id, success_message, parse_mode="html")
        os.remove(remove_path + file_name)



# Run
bot.polling(none_stop=True)
