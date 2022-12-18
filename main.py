from pprint import pprint

import requests


def print_hi(name):
    token = {'Authorization': 'Token 33811728b3925fac31e3f92d7b9fc820679551a8'}
    url = 'https://dvmn.org/api/user_reviews/'
    long_polling = 'https://dvmn.org/api/long_polling/'
    # response = requests.get(url, headers=token)
    response = requests.get(long_polling, headers=token)

    pprint(response.text)


if __name__ == '__main__':
    print_hi('PyCharm')


