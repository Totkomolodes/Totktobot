from config import bot, cs_path, tundra_path, ets_path


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
