from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def receive_data():
    if request.method == "POST":
        username = request.form['user_name']
        password = request.form.get('user_password')
        return render_template("login.html", username=username, password=password)






if __name__ == "__main__":
    app.run(debug=True)
