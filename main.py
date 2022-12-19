import requests, os, logging
from dotenv import load_dotenv
from time import sleep

from devman_bot import send_message


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

DEVMAN_TOKEN = os.getenv('DEVMAN_TOKEN')
TOKEN_TG = os.getenv('TOKEN_TG')
TIMEOUT = 100
LONG_POLLING_URL = 'https://dvmn.org/api/long_polling/'

def main():
    load_dotenv()

    while True:
        try:
            params = {
                'timestamp': '',
            }
            long_polling_url = LONG_POLLING_URL
            response = requests.get(long_polling_url, headers={
                'Authorization': f'Token {DEVMAN_TOKEN}'
            }, timeout=TIMEOUT, params=params)
            response.raise_for_status()
            long_polling_response = response.json()
            if long_polling_response.get('status') == 'found':
                new_attempts = long_polling_response.get('new_attempts')
                for attempt in new_attempts:
                    params['timestamp'] = attempt.get('timestamp')
                    lesson_title = attempt.get('lesson_title')
                    lesson_url = attempt.get('lesson_url')
                    confirmation_attempt = attempt.get('is_negative')
            else:
                params['timestamp'] = long_polling_response.get('timestamp_to_request')
            send_message(lesson_title, lesson_url, confirmation_attempt)
        except requests.exceptions.ReadTimeout:
            logger.info('Сервер не отвечает')
        except requests.exceptions.ConnectionError:
            logger.info('Отсутствует интернет')
            sleep(TIMEOUT)


if __name__ == '__main__':
    main()



