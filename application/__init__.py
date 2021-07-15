import os
from flask import Flask


def get_app_base_path():
    return os.path.dirname(os.path.realpath(__file__))


app = Flask(__name__, instance_path=get_app_base_path(), instance_relative_config=True)


from .bin.hello.routes import hello_blueprint

app.register_blueprint(hello_blueprint)
