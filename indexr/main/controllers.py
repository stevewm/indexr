import requests
from flask import Blueprint, render_template, Response
from indexr.utils.docker import DockerUtils

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def index():
    dockerutils = DockerUtils()
    enabled_containers = dockerutils.get_enabled_containers()
    return render_template('index.html', containers=enabled_containers)


@main.route('potd')
def potd():
    # TODO: Get Unsplash POTD instead of random
    r = requests.get('https://source.unsplash.com/random')
    return Response(r.content, mimetype=r.headers.get('content-type'))
