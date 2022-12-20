import requests, os, logging
from dotenv import load_dotenv
from time import sleep, time
import time
from devman_bot import send_message


logger = logging.getLogger(__name__)


def main():
    load_dotenv()
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%m-%Y %I:%M:%S %p',
                        level=logging.INFO)

    DEVMAN_TOKEN = os.getenv('DEVMAN_TOKEN')
    LONG_POLLING_URL = 'https://dvmn.org/api/long_polling/'
    TIMEOUT = 10
    TOKEN_TG = os.getenv('TOKEN_TG')
    CHAT_ID = os.getenv('CHAT_ID')

    while True:
        try:
            params = {
                'timestamp': time.time(),
            }
            long_polling_url = LONG_POLLING_URL
            response = requests.get(long_polling_url, headers={
                'Authorization': f'Token {DEVMAN_TOKEN}'
            }, timeout=TIMEOUT, params=params)
            response.raise_for_status()
            logger.info(response.json())
            json_response = response.json()
            if json_response.get('status') == 'found':
                params['timestamp'] = json_response.get('last_attempt_timestamp')
                new_attempts = json_response.get('new_attempts')
                for attempt in new_attempts:
                    lesson_title = attempt.get('lesson_title')
                    lesson_url = attempt.get('lesson_url')
                    confirmation_attempt = attempt.get('is_negative')
                    send_message(lesson_title, lesson_url, confirmation_attempt, TOKEN_TG, CHAT_ID)
            else:
                params['timestamp'] = json_response.get('timestamp_to_request')
        except requests.exceptions.ReadTimeout:
            logger.info('Сервер не отвечает.')
        except requests.exceptions.ConnectionError:
            logger.info('Отсутствует интернет.')
            sleep(TIMEOUT)


if __name__ == '__main__':
    main()



