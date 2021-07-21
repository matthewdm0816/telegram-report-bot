import logging
import os
import sys
from icecream import ic
import colorama
import toml
from telegram.ext import (
    CommandHandler,
    Dispatcher,
    Filters,
    MessageHandler,
    Updater,
    InlineQueryHandler,
)
from telegram import (
    InlineQueryResultArticle,
    InputTextMessageContent,
)

# Automatically set proxies
os.environ["HTTPS_PROXY"] = "https://localhost:10809"
os.environ["HTTP_PROXY"] = "http://localhost:10809"
TOKEN = r"1904652985:AAFtfDRXYvj--mNd_QkuRd62uleVWKfkr2o"


from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    ic(request.json)
    ic(request.args)
    return Response(response="Hello!", status=200)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)



