from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",  # Replace with your MySQL password
        database="quantams"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/bots')
def bots():
    return render_template('bots.html')

@app.route('/docs')
def docs():
    return render_template('doc.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm')

        if password != confirm:
            return "Passwords do not match"

        try:
            con = get_connection()
            cur = con.cursor()
            cur.execute("INSERT INTO users (fullname, email, password) VALUES (%s, %s, %s)",
                        (fullname, email, password))
            con.commit()
        except mysql.connector.Error as err:
            print(f"[ERROR] Signup: {err}")
            return "Email may already exist or database error occurred."
        finally:
            cur.close()
            con.close()

        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        try:
            con = get_connection()
            cur = con.cursor()
            cur.execute("SELECT * FROM users WHERE email=%s AND password=%s", (username, password))
            user = cur.fetchone()
        finally:
            cur.close()
            con.close()

        if user:
            print(f"[LOGIN] Success: {username}")
            return redirect(url_for('index'))
        else:
            return "Invalid credentials"

    return render_template('login.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        experience = request.form.get('experience')
        comments = request.form.get('comments')

        try:
            con = get_connection()
            cur = con.cursor()
            cur.execute("INSERT INTO feedback (name, email, experience, comments) VALUES (%s, %s, %s, %s)",
                        (name, email, experience, comments))
            con.commit()
        finally:
            cur.close()
            con.close()

        return redirect(url_for('index'))

    return render_template('feedback.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        try:
            con = get_connection()
            cur = con.cursor()
            cur.execute("INSERT INTO contact (name, email, message) VALUES (%s, %s, %s)",
                        (name, email, message))
            con.commit()
        finally:
            cur.close()
            con.close()

        return redirect(url_for('index'))

    return render_template('contact.html')

@app.route('/buy_bot', methods=['POST'])
def buy_bot():
    user_email = request.form.get('email')
    bot_name = request.form.get('bot')

    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("INSERT INTO bot_orders (user_email, bot_name) VALUES (%s, %s)", (user_email, bot_name))
        con.commit()
    finally:
        cur.close()
        con.close()

    return "Bot purchased successfully!"

if __name__ == '__main__':
    app.run(debug=True)



