from flask import Flask

def config_localservice():
    app = Flask(__name__)
    return app