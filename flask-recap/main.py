from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home():
    return '<h2>Ram Ram on Home Page!</h2>'

@app.route('/about')
def about():
    return '<h3>You are at about page</h3>'

if __name__ == '__main__':
    app.run('0.0.0.0',5005,debug=True)


