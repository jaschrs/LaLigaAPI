from flask import Flask

def config_local_service():
    """
    Configures the local Flask service.
    :return: Flask app instance with JSON sorting disabled
    """

    app = Flask(__name__)
    app.json.sort_keys = False
    return app