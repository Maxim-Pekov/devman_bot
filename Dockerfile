FROM python:3
LABEL org.opencontainers.image.authors="Max.Pekov@gmail.com"
WORKDIR /devman_bot
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python3","main.py"]
