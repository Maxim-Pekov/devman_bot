import requests, os
from devman_bot import reply_message
from pprint import pprint
from dotenv import load_dotenv
from time import sleep


DEVMAN_TOKEN = os.getenv('DEVMAN_TOKEN')
TOKEN_TG = os.getenv('TOKEN_TG')
TIMEOUT = 10


def main():
    load_dotenv()

    while True:
        try:
            params = {
                'timestamp': '',
            }
            long_polling_url = 'https://dvmn.org/api/long_polling/'
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
            pprint(params['timestamp'])
            pprint(response.json())
            reply_message(lesson_title, lesson_url, confirmation_attempt)
        except requests.exceptions.ReadTimeout:
            print(111)
            pass
        except requests.exceptions.ConnectionError:
            print(222)
            sleep(TIMEOUT)
            pass


if __name__ == '__main__':
    main()



