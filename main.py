import requests, os

from pprint import pprint
from dotenv import load_dotenv
from time import sleep


load_dotenv()
DEVMAN_TOKEN = os.getenv('DEVMAN_TOKEN')
TIMEOUT = 10


def main():
    while True:
        try:
            params = {
                'timestamp': '',
            }
            url = 'https://dvmn.org/api/user_reviews/'
            long_polling = 'https://dvmn.org/api/long_polling/'
            # response = requests.get(url, headers={
            #     'Authorization': f'Token {DEVMAN_TOKEN}'
            # })
            response = requests.get(long_polling, headers={
                'Authorization': f'Token {DEVMAN_TOKEN}'
            }, timeout=TIMEOUT, params=params)
            params['timestamp'] = response.json().get('new_attempts')[0].get('timestamp')
            pprint(params['timestamp'])
            # pprint(response.text)
        except requests.exceptions.ReadTimeout:
            print(111)
            pass
        except requests.exceptions.ConnectionError:
            print(222)
            sleep(TIMEOUT)
            pass


if __name__ == '__main__':
    main()



