import requests
from flask import Blueprint, render_template, Response
from app.utils.docker import DockerUtils
from app.main import bp

main = Blueprint('main', __name__)


@bp.route('/')
def index():
    dockerutils = DockerUtils()
    enabled_containers = dockerutils.get_enabled_containers()
    return render_template('index.html', containers=enabled_containers)


@bp.route('/potd')
def potd():
    # TODO: Get Unsplash POTD instead of random
    r = requests.get('https://source.unsplash.com/random')
    return Response(r.content, mimetype=r.headers.get('content-type'))
