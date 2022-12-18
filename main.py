import requests, os

from pprint import pprint
from dotenv import load_dotenv
from time import sleep


load_dotenv()
DEVMAN_TOKEN = os.getenv('DEVMAN_TOKEN')


def main():
    while True:
        try:
            url = 'https://dvmn.org/api/user_reviews/'
            long_polling = 'https://dvmn.org/api/long_polling/'
            # response = requests.get(url, headers={
            #     'Authorization': f'Token {DEVMAN_TOKEN}'
            # })
            response = requests.get(long_polling, headers={
                'Authorization': f'Token {DEVMAN_TOKEN}'
            }, timeout=10)

            pprint(response.text)
        except requests.exceptions.ReadTimeout:
            print(111)
            pass
        except requests.exceptions.ConnectionError:
            print(222)
            sleep(10)
            pass


if __name__ == '__main__':
    main()



