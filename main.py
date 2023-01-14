from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Mr.Kamal, WELCOME TO APP ENGINE-V1'

