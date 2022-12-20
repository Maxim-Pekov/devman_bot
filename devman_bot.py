import logging
import os
from dotenv import load_dotenv
from telegram import Bot
from telegram.utils.request import Request


logger = logging.getLogger(__name__)


def send_message(title, lesson_url, confirmation_attempt, TOKEN_TG, CHAT_ID):
    logger.info(f'Функция send_message с параметрами title={title},\n lesson_url={lesson_url}, confirmation_attempt={confirmation_attempt}')

    if not confirmation_attempt:
        bot_messege = f'Ваша работа "{title}" проверена!!\n\n Преподователю все понравилось можно приступить к ' \
                      f'следующему уроку\n\n {lesson_url}'
    else:
        bot_messege = f'Ваша работа "{title}" проверена!!\n\nК сожалению, в работе нашлись ошибки.\n\n {lesson_url}'

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
