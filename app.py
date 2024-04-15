import os

import telebot
from flask import Flask, request
from telebot import TeleBot

from bot import states
from db import model
from db.ydb_settings import get_ydb_pool

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH")
YDB_ENDPOINT = os.getenv("YDB_ENDPOINT")
YDB_DATABASE = os.getenv("YDB_DATABASE")

pool = get_ydb_pool(YDB_ENDPOINT, YDB_DATABASE)
state_storage = states.StateYDBStorage(pool)
bot = TeleBot(BOT_TOKEN, state_storage=state_storage)
# bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.remove_webhook()
bot.set_webhook()


@bot.message_handler(commands=['start'])
def start_message(message):
    state = model.get_state(pool, message.from_user.id)
    if not state:
        bot.set_state(message.from_user.id, states.RegisterState.guest, message.chat.id)
    bot.send_message(message.chat.id, "Привет ✌️ ")


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "Помощь уже в пути! ")


@app.route("/", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return {
        "statusCode": 200,
        "body": "!",
    }


@app.route("/api/say", methods=['POST'])
def say():
    bot.send_message(
        request.args.get('id'),
        request.args.get('text')
    )
    return {
        "statusCode": 200,
        "body": "!",
    }


if __name__ == '__main__':
    app.run()
