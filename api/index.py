from flask import Flask, request
import telebot
import os

API_TOKEN = '7704347220:AAHpo6jWysFvUc0Deahk7_HuPInJ3E0X2ns'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@app.route('/' + API_TOKEN, methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return 'ok', 200

@app.route('/')
def home():
    return 'Bot is running!', 200

def handler(req, res):
    return app
