from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'TechnoJihad !'

@app.route('/aboutLife/')
def about():
    return 'We Die - sadface !'

if __name__ == '__main__':
    app.run(debug = True)
    