# Simple guessing number game where you guess an integer between 1-9 by adding it after the URL.

from flask import Flask
import random
app = Flask(__name__)

correct_number = random.randint(1, 9)


@app.route('/')
def greeting():
    return "<h1 style='text-align: center'>Guess a number between 0 and 9.</h1>" \
            "<img src='https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif' width=200>"

@app.route('/<number>')
def guess_number(number):
    try:
        if int(number) > correct_number and int(number) <= 9:
            return "<h1> TOO HIGH </h1>"
        if int(number) < correct_number:
            return "<h1> TOO LOW</h1>"
        if int(number) == correct_number:
            return "<h1>YAY THAT'S RIGHT</h1>"
        else:
            return "<h1>HUH. GUESS A NUMBER BETWEEN 1 and 9.</h1>"
    except ValueError:
        return "<h1>LIKE, THAT ISN'T AN INTEGER??</h1>"

if __name__ == "__main__":
    app.run()