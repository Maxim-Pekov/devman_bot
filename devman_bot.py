import logging
import os

from dotenv import load_dotenv
from telegram import Bot
from telegram.utils.request import Request

load_dotenv()
TOKEN_TG = os.getenv('TOKEN_TG')
CHAT_ID = os.getenv('CHAT_ID')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def send_message(title, lesson_url, confirmation_attempt):
    logger.info(f'Функция send_message с параметрами title={title}, lesson_url={lesson_url}, confirmation_attempt={confirmation_attempt}')

    if not confirmation_attempt:
        bot_messege = f'Ваша работа "{title}" проверена!!\n\n Преподователю все понравилось можно приступить к ' \
                      f'следующему уроку\n {lesson_url} '
    else:
        bot_messege = f'Ваша работа "{title}" проверена!!\n\nК сожалению, в работе нашлись ошибки.'

    request = Request(
        connect_timeout=0.5,
        read_timeout=1.0,
    )
    bot = Bot(
        request=request,
        token=TOKEN_TG,
    )
    bot.send_message(
        chat_id=CHAT_ID,
        text=bot_messege,
    )
