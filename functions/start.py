
from config import bot


def start(message):
    message_to_user = f"<b>Привет {message.from_user.first_name}</b> <b>{message.from_user.last_name}!</b>"
    bot.send_message(message.chat.id, message_to_user, parse_mode="html")