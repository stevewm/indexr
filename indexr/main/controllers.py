from flask import Blueprint, render_template
from indexr.utils.docker import DockerUtils

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def index():
    dockerutils = DockerUtils()
    enabled_containers = dockerutils.get_enabled_containers()
    return render_template('index.html', containers=enabled_containers)
