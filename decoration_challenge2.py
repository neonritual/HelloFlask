## CHALLENGE: User Python decorators to add HTML to strings in Flask.

from flask import Flask
app = Flask(__name__)

def bold(function):
    def decorate():
        return f"<b>{function()}</b>"
    return decorate

def emphasis(function):
    def decorate():
        return f"<em>{function()}</em>"
    return decorate

def underlined(function):
    def decorate():
        return f"<ul>{function()}</ul>"
    return decorate



@app.route('/')
@bold
@emphasis
@underlined
def hello_world():
    return "Some text."


if __name__ == "__main__":
    app.run(debug=True)



