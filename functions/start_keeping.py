import os

import requests
from telebot import types
from telebot.types import InputFile

from config import bot, question_message, question_message_2, success_message, \
    remove_path, y, question_message_0, question_message_4, vid_list, doc_list, pic_list, types_list
from yadisk.exceptions import PathNotFoundError


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
            bot.send_message(message.chat.id, question_message, parse_mode="html")
            bot.register_next_step_handler(message, determinant_1)
        elif message2.text == "скачать с диска":
            bot.send_message(message.chat.id, question_message_4, parse_mode="html")
            bot.register_next_step_handler(message, downloading_from_disk)
        elif message2.text == "удалить с диска":
            bot.send_message(message.chat.id, question_message_2, parse_mode="html")
            bot.register_next_step_handler(message, deleting)
        else:
            bot.send_message(message.chat.id, "Ошибка ввода", parse_mode="html")

    def downloading_on_computer(files, file_name):
        for i in files:
            file_info = bot.get_file(i.file_id)
            response = bot.download_file(file_info.file_path)
            with open(file_name, "wb") as file:
                file.write(response)
        downloading_on_disk(file_name)

    def downloading_from_disk(message2):
        shared_mess = message2.text.split(", ")
        type_of_file = shared_mess[-1]
        name = shared_mess[0]
        y.download(f"/{name}", f"{name}")
        if type_of_file == "photo":
            bot.send_photo(message.chat.id, InputFile(name))
        elif type_of_file == "document":
            bot.send_document(message.chat.id, InputFile(name))
        elif type_of_file == "audio":
            bot.send_audio(message.chat.id, InputFile(name))
        elif type_of_file == "video":
            bot.send_video(message.chat.id, InputFile(name))
        else:
            bot.send_message(message.chat.id, "<b>Я не могу обработать такой тип!</b>", parse_mode="html")
        os.remove(name)

    def deleting(message2):
        try:
            y.remove("/" + message2.text, permanently=True)
            bot.send_message(message.chat.id, "<b>Файл удачно удален!</b>", parse_mode="html")
        except PathNotFoundError:
            bot.send_message(message.chat.id, "<b>Такой файл не найден</b>", parse_mode="html")

    def downloading_on_disk(file_name):
        y.upload(file_name, "/" + file_name)
        bot.send_message(message.chat.id, success_message, parse_mode="html")
        os.remove(file_name)

    markup_0 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    upload = types.KeyboardButton("загрузить на диск")
    download = types.KeyboardButton("скачать с диска")
    delete = types.KeyboardButton("удалить с диска")
    markup_0.add(upload, download, delete)
    bot.send_message(message.chat.id, question_message_0, parse_mode="html", reply_markup=markup_0)
    bot.register_next_step_handler(message, determinant_0)
