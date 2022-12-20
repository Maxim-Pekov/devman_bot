import logging
from telegram import Bot
from telegram.utils.request import Request


logger = logging.getLogger(__file__)


def send_message(message, tg_token, chat_id):
    logger.info(
        f'Функция send_message с параметрами:\n    TOKEN_TG={tg_token},\n    CHAT_ID={chat_id}')

    request = Request(
        connect_timeout=0.5,
        read_timeout=1.0,
    )
    bot = Bot(
        request=request,
        token=tg_token,
    )
    bot.send_message(
        chat_id=chat_id,
        text=message,
    )
