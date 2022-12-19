# dewman_bot

Этот проект нужен для оповещения о проверенных работах на учебном сервисе [https://dvmn.org](https://dvmn.org). 

Проект содержит два скрипта:
* `main.py` - Скрипт проверяет изменения в статусе проверки работ по средством API и отправляет данные в функцию телеграмм бота.
* `devman_bot.py` - Скрипт принемает результат о проверки работ и отправляет его через телеграм бота ученику.
## Пример сообщения телеграмм бота.

<img src="static/111.jpg" width="300">

## Как он работает:

1. `main.py`
   Вы запускаете скрипт командой ниже, и он посылает запрос к API. Сервер ответит не сразу, 
   а только когда изменится статус проверки работ. В этом случает скрипт достанет из ответа, данные о проверке: 
   название, время изменения статуса, статус проверки, ссылку на урок и передаст данные через телеграмм бота в чат 
   ученика.

```python
python3 main.py
```

## Установка

Используйте данную инструкцию по установке этого скрипта

1. Установить

```python
git clone https://github.com/Maxim-Pekov/dewman_bot.git
```

2. Создайте виртуальное окружение:

```python
python -m venv venv
```

3. Активируйте виртуальное окружение:
```python
.\venv\Scripts\activate`    # for Windows
```
```python
source ./.venv/bin/activate    # for Linux
```

4. Перейдите в `dewman_bot` директорию.

3. Установите зависимости командой ниже:
```python
pip install -r requirements.txt
```

4. Создайте файл с названием `.env`

5. Запишите в данном файле, ваш API токен с сайта DEVMAN, телеграмм токен вашего бота и номер вашего чата с ботом в формате 
   как в примере ниже.
```python
DEVMAN_TOKEN='33222728d3925fc31t3e955555wj8206k95h1l8'
TOKEN_TG='559475638:AQweRTZdfKiJnm0AitjQ196u_n6GHjSDFG0'
CHAT_ID='741414141'
```
---

## About me

[<img align="left" alt="maxim-pekov | LinkedIn" width="30px" src="https://img.icons8.com/color/48/000000/linkedin-circled--v3.png" />https://www.linkedin.com/in/maxim-pekov/](https://www.linkedin.com/in/maxim-pekov/)
</br>

[<img align="left" alt="maxim-pekov" width="28px" src="https://upload.wikimedia.org/wikipedia/commons/5/5c/Telegram_Messenger.png" />https://t.me/MaxPekov/](https://t.me/MaxPekov/)
</br>

[//]: # (Карточка профиля: )
![](https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Maxim-Pekov&theme=solarized_dark)

[//]: # (Статистика языков в коммитах:)

[//]: # (Статистика языков в репозиториях:)
![](https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=Maxim-Pekov&theme=solarized_dark)
![](https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Maxim-Pekov&theme=solarized_dark)


[//]: # (Статистика профиля:)

[//]: # (Данные по коммитам за сутки:)
![](https://github-profile-summary-cards.vercel.app/api/cards/stats?username=Maxim-Pekov&theme=solarized_dark)
![](https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=Maxim-Pekov&theme=solarized_dark)

[//]: # ([![trophy]&#40;https://github-profile-trophy.vercel.app/?username=Maxim-Pekov&#41;]&#40;https://github.com/ryo-ma/github-profile-trophy&#41;)

