import logging
import random
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request

app = App()
logging.basicConfig(level=logging.DEBUG)

@app.middleware
def log_request(logger, body, next):
    logger.debug(body)
    return next()

@app.event("app_mention")
def say_lyrics(body, say, logger):
    logger.info(body)
    lyric = random.choice(list(open('fleetwoodmac.txt')))
    while lyric.isspace():
        lyric = random.choice(list(open('fleetwoodmac.txt')))
    say(lyric)

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)
