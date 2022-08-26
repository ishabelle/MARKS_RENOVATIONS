from flask import Flask, render_template
import os

app = Flask(__name__)
app.secret_key = (os.urandom(16))


@app.route("/")
def index_page():
    return render_template("main_page.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(
        host='localhost',
        port=5000,
        debug=True,
    )