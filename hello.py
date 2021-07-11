# Instructor's Challenge: info below.


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
            "<p>This is a paragraph.</p>" \
            "<img src='https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif' width=200>"

@app.route('/bye')
def bye():
    return "Bye"

@app.route('/username/<name>')
def greet_name(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)

