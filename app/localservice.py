from flask import Flask

def config_localservice():
    app = Flask(__name__)
    app.json.sort_keys = False
    return Flask(__name__)