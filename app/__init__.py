from flask import Flask

app = Flask(__name__)

@app.route('/')
def login_screen():
    return 'Login Screen'

if __name__ == '__main__':
    app.run()


