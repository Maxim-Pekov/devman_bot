import logging
import os
from telegram import Bot
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, CallbackContext
from telegram.utils.request import Request
from telegram import ReplyKeyboardRemove, ParseMode, Update
from dotenv import load_dotenv


load_dotenv()
TOKEN_TG = os.getenv('TOKEN_TG')
CHAT_ID = os.getenv('CHAT_ID')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def reply_message(title, lesson_url, confirmation_attempt):
    request = Request(
        connect_timeout=0.5,
        read_timeout=1.0,
    )
    bot = Bot(
        request=request,
        token=TOKEN_TG,
    )
    if not confirmation_attempt:
        bot.send_message(
            chat_id=CHAT_ID,
            text=f'Ваша работа "{title}" проверена!!\n\n Преподователю все понравилось можно приступить к следующему уроку'
                 f'\n {lesson_url}'
        )
    else:
        bot.send_message(
            chat_id=CHAT_ID,
            text=f'Ваша работа "{title}" проверена!!\n\nК сожалению, в работе нашлись ошибки.'
        )

