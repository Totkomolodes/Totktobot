import help
import library
import meme
import start
import start_keeping
from config import bot

bot.message_handler(commands=["start"])(start.start)
bot.message_handler(commands=["help"])(help.help_command)
bot.message_handler(commands=["library"])(library.library_which_i_used)
bot.message_handler(content_types=["text"], commands=["meme"])(meme.my_videos)
bot.message_handler(commands=["start_keeping"], content_types=["text"])(start_keeping.keeper_of_files_on_yadisk)

bot.polling(none_stop=True)
