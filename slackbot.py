import os
import random
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

motivationalquotes = [
    "> \"You're filled with DETERMINATION.\"",
    "> \"You're not the first one who found out such an annoying bug.\"",
    "> \"Think about the cake.\"",
]


boostquotes = [
    "> \"It's not a bug, it is a feature.\"",
    "> \"First you have to solve the problem, then you write the code.\"",
    "> \"The idea is half of the project. So is the name.\"",
]

# 3. Film / Popcultuur quote
focusquotes = [
    "> \"The best way to focus is pausing for five minutes.\"",
    "> \"Quality > Quantity\"",
    "> \"I grinded Stardance, you can grind this too.\"",
]

@app.command("/cat-quote")
def send_motivational_quote(message, say):
    say(random.choice(motivationalquotes))

@app.command("/cat-focus")
def send_focus_quote(message, say):
    say(random.choice(focusquotes))


@app.command("/cat-boost")
def send_boost_quote(message, say):
    say(random.choice(boostquotes))

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN"))
    handler.start()