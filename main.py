import time
from time import sleep
from telegram import Bot
import requests, os, logging
from dotenv import load_dotenv


LONG_POLLING_URL = 'https://dvmn.org/api/long_polling/'

logger = logging.getLogger(__name__)
exception_logger = logging.getLogger('get_all_exception')


class TelegramLogsHandler(logging.Handler):

    def __init__(self, tg_token, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.tg_bot = Bot(token=tg_token)

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)


def main():
    load_dotenv()
    devman_token = os.getenv('DEVMAN_TOKEN')
    tg_token = os.getenv('TOKEN_TG')
    chat_id = os.getenv('TG_CHAT_ID')
    timeout = 120

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%m-%Y %I:%M:%S %p',
                        level=logging.INFO)

    exception_logger.setLevel(logging.ERROR)
    exception_logger.addHandler(TelegramLogsHandler(tg_token, chat_id))

    logger.setLevel(logging.WARNING)
    logger.addHandler(TelegramLogsHandler(tg_token, chat_id))

    while True:
        try:
            bot = Bot(token=tg_token)
            logging.info('Бот запущен')
            params = {
                'timestamp': time.time(),
            }
            response = requests.get(LONG_POLLING_URL, headers={
                'Authorization': f'Token {devman_token}'
            }, timeout=timeout, params=params)
            response.raise_for_status()
            logging.info(f'Данные словаря из response {response.json()}')
            info_review = response.json()
            if info_review.get('status') == 'found':
                params['timestamp'] = info_review.get('last_attempt_timestamp')
                new_attempts = info_review.get('new_attempts')
                for attempt in new_attempts:
                    lesson_title = attempt.get('lesson_title')
                    lesson_url = attempt.get('lesson_url')
                    confirmation_attempt = attempt.get('is_negative')
                    if not confirmation_attempt:
                        bot_message = f'Ваша работа "{lesson_title}" проверена!!\n\n Преподователю все понравилось можно приступить к ' \
                                      f'следующему уроку\n\n {lesson_url}'
                    else:
                        bot_message = f'Ваша работа "{lesson_title}" проверена!!\n\nК сожалению, в работе нашлись ошибки.\n\n {lesson_url}'
                    bot.send_message(
                        chat_id=chat_id,
                        text=bot_message,
                    )
            else:
                params['timestamp'] = info_review.get('timestamp_to_request')
        except requests.exceptions.ReadTimeout:
            logger.warning('Сервер не отвечает.')
            sleep(timeout)
        except requests.exceptions.ConnectionError:
            logger.warning('Отсутствует интернет.')
            sleep(timeout)
        except Exception:
            exception_logger.exception("Бот упал с ошибкой")
            sleep(timeout)


if __name__ == '__main__':
    main()