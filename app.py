from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Привет, это ваше Flask-приложение на Render!"

if __name__ == '__main__':
    app.run()
