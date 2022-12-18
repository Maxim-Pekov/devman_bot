import logging
import os
from telegram import Bot
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, CallbackContext
from telegram.utils.request import Request
from telegram import ReplyKeyboardRemove, ParseMode, Update
from dotenv import load_dotenv


load_dotenv()
TOKEN_TG = os.getenv('TOKEN_TG')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# def start(update, context):
#     context.bot.send_message(
#         chat_id=update.message.chat_id,
#         text=f'HiHI {update.message.chat.username}')


def reply_message(title):
    request = Request(
        connect_timeout=0.5,
        read_timeout=1.0,
    )
    bot = Bot(
        request=request,
        token=TOKEN_TG,
    )
    bot.send_message(
        chat_id=741289598,
        text=f'ваша работа "{title}" проверена!!'
    )
# reply_message()

# if TOKEN_TG == "":
#     print("Please write TOKEN into file")
# else:
#     request = Request(
#         connect_timeout=0.5,
#         read_timeout=1.0,
#     )
#     bot = Bot(
#         request=request,
#         token=TOKEN_TG,
#     )
#     updater = Updater(TOKEN_TG, use_context=True)
#     dispatcher = updater.dispatcher
#
#     dispatcher.add_handler(CommandHandler("start", start))
#     # dispatcher.add_handler(CommandHandler("calendar", calendar_handler))
#     # dispatcher.add_handler(CallbackQueryHandler(inline_handler))
#
#     updater.start_polling()
#     updater.idle()