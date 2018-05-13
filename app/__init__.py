from flask import Flask
from indexr.main.controllers import main
from indexr.utils import *

app = Flask(__name__,
            template_folder='templates')

app.register_blueprint(main, url_prefix='/')
