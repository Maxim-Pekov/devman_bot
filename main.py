import requests, os
from devman_bot import reply_message
from pprint import pprint
from dotenv import load_dotenv
from time import sleep
from telegram import Bot


load_dotenv()
DEVMAN_TOKEN = os.getenv('DEVMAN_TOKEN')
TOKEN_TG = os.getenv('TOKEN_TG')
TIMEOUT = 10


def main():
    while True:
        try:
            params = {
                'timestamp': '',
            }
            long_polling = 'https://dvmn.org/api/long_polling/'
            response = requests.get(long_polling, headers={
                'Authorization': f'Token {DEVMAN_TOKEN}'
            }, timeout=TIMEOUT, params=params)
            params['timestamp'] = response.json().get('new_attempts')[0].get('timestamp')
            lesson_title = response.json().get('new_attempts')[0].get('lesson_title')
            pprint(params['timestamp'])
            pprint(response.json())
            reply_message(lesson_title)
        except requests.exceptions.ReadTimeout:
            print(111)
            pass
        except requests.exceptions.ConnectionError:
            print(222)
            sleep(TIMEOUT)
            pass


if __name__ == '__main__':
    main()



