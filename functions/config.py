import telebot
import yadisk

success_message = "Файл был удачно установлен в хранилище Яндекс Диска"
question_message = "Отправите файл и укажите его название(document, photo, video, audio)"
question_message_2 = "Укажите полное название вашего файла"
question_message_4 = f"Укажите полное название вашего файла и тип файла через запятую(типы:video, document, photo, " \
                     f"audio) "
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
question_message_0 = f"<b>Что вы желаете сделать?</b>"
pic_list = [".png", ".jpg"]
vid_list = [".mp4"]
doc_list = [".doc", ".txt", ".html", ".Odt", ".Rtf"]
audio_list = [".mp3"]
types_list = ["photo", "video", "document", "audio"]
y = yadisk.YaDisk(token=token_me)
