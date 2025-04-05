import telebot
from flask import Flask, request

API_TOKEN = 'توکن_ربات_شما'
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "سلام! من ربات تلگرام شما هستم!")

@app.route('/' + API_TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
