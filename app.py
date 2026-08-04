from flask import Flask, render_template, request, redirect
import sqlite3
import random
import string

app = Flask(__name__)

# Generate random code
def generate_code(length=6):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


@app.route('/', methods=['GET','POST'])
def home():

    short_url = ""

    if request.method == "POST":

        original = request.form['url']

        code = generate_code()

        conn = sqlite3.connect("urls.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO urls(original, short) VALUES(?,?)",
            (original, code)
        )

        conn.commit()
        conn.close()

        short_url = request.host_url + code

    return render_template("index.html", short_url=short_url)


@app.route('/<code>')
def redirect_url(code):

    conn = sqlite3.connect("urls.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT original FROM urls WHERE short=?",
        (code,)
    )

    data = cursor.fetchone()

    conn.close()

    if data:
        return redirect(data[0])

    return "URL Not Found"


if __name__ == '__main__':
    app.run(debug=True)