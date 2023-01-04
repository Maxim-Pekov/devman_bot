import time
from time import sleep
from telegram import Bot
import requests, os, logging
from dotenv import load_dotenv


LONG_POLLING_URL = 'https://dvmn.org/api/long_polling/'

logger = logging.getLogger(__name__)


def create_message(title, lesson_url, confirmation_attempt):
    if not confirmation_attempt:
        bot_message = f'Ваша работа "{title}" проверена!!\n\n Преподователю все понравилось можно приступить к ' \
                      f'следующему уроку\n\n {lesson_url}'
    else:
        bot_message = f'Ваша работа "{title}" проверена!!\n\nК сожалению, в работе нашлись ошибки.\n\n {lesson_url}'
    return bot_message


def main():
    load_dotenv()
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%m-%Y %I:%M:%S %p',
                        level=logging.WARNING)

    timeout = 100
    devman_token = os.getenv('DEVMAN_TOKEN')
    tg_token = os.getenv('TOKEN_TG')
    chat_id = os.getenv('CHAT_ID')

    bot = Bot(token=tg_token)

    while True:
        try:
            params = {
                'timestamp': time.time(),
            }
            long_polling_url = LONG_POLLING_URL
            response = requests.get(long_polling_url, headers={
                'Authorization': f'Token {devman_token}'
            }, timeout=timeout, params=params)
            response.raise_for_status()
            logger.info(f'Данные словаря из response {response.json()}')
            json_response = response.json()
            if json_response.get('status') == 'found':
                params['timestamp'] = json_response.get('last_attempt_timestamp')
                new_attempts = json_response.get('new_attempts')
                for attempt in new_attempts:
                    lesson_title = attempt.get('lesson_title')
                    lesson_url = attempt.get('lesson_url')
                    confirmation_attempt = attempt.get('is_negative')
                    message = create_message(lesson_title, lesson_url, confirmation_attempt)
                    bot.send_message(
                        chat_id=chat_id,
                        text=message,
                    )
            else:
                params['timestamp'] = json_response.get('timestamp_to_request')
        except requests.exceptions.ReadTimeout:
            server_not_answer_message = logger.warning('Сервер не отвечает.')
            bot.send_message(
                chat_id=chat_id,
                text=server_not_answer_message,
            )
        except requests.exceptions.ConnectionError:
            connection_error_message = logger.warning('Отсутствует интернет.')
            bot.send_message(
                chat_id=chat_id,
                text=connection_error_message,
            )
            sleep(timeout)


if __name__ == '__main__':
    main()



