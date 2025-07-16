from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/bots')
def bots():
    return render_template('bots.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/contact')
def contact():
    return render_template('contact us page.html')

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/docs')
def docs():
    return render_template('DOC.html')

if __name__ == '__main__':
    app.run(debug=True)
