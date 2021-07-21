import logging
import os
import sys
from icecream import ic
import colorama
from telegram import chat
import toml
import telegram
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
from flask import Flask, request, Response

logger = logging.getLogger()
logger.setLevel(logging.INFO)
log_format = (
    colorama.Fore.MAGENTA
    + "[%(asctime)s %(name)s %(levelname)s] "
    + colorama.Fore.WHITE
    + "%(message)s"
)
logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%I:%M:%S")
logger.info("Starting bot...")

# Load Configurations
fname = "config.toml"
logging.info("Loading Config from %s" % fname)
with open(fname, "r") as f:
    config = toml.load(f)
ic(config)

# Automatically set proxies
os.environ["HTTPS_PROXY"] = config["http_proxy"]
os.environ["HTTP_PROXY"] = config["https_proxy"]

# Telegram settings
TOKEN = config["token"]
CHAT_ID = config["chat_id"]
FLASK_TOKEN = config["flask_token"]

bot = telegram.Bot(token=TOKEN)
bot_identity = bot.get_me()
logging.info(
    "Starting Bot %s @%s..." % (bot_identity["first_name"], bot_identity["username"])
)


# Flask app initialization
app = Flask(__name__)


@app.route("/notify", methods=["GET", "POST"])
def notify():
    if request.args.get("uuid") == FLASK_TOKEN:
        if "text" in request.args.keys():
            text = request.args.get("text")
            logging.info('Sending "%s"...' % text)
            bot.send_message(text=request.args.get("text"), chat_id=CHAT_ID)
        else:
            bot.send_message(text="お兄ちゃん、どうしたの？", chat_id=CHAT_ID)
        return Response(response="Data Sent!", status=200)
    else:
        return Response(response="Wrong UUID!", status=400)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
    # Load configurations
