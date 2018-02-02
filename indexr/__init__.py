from flask import Flask
from indexr.main.controllers import main
from indexr.admin.controllers import admin
from indexr.utils import *

app = Flask(__name__,
            template_folder='templates')

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
