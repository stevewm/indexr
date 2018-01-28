from flask import Flask, render_template, url_for
import docker

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('theme_basic/index.html', containers=get_enabled_containers()) 
  

@app.route('/monitor')
def monitor():
    return render_template('theme_basic/monitor.html', containers=get_enabled_containers()) 


def get_enabled_containers():
  client = docker.from_env()
  enabled_containers = []
  for c in client.containers.list(filters={'label': 'indexr.enable=true'}):
    l = c.labels
    icon = url_for('static', filename='icons/' + l['indexr.icon'])
    enabled_containers.append({'name': l['indexr.name'], 'url': l['indexr.url'], 'icon': icon})
  return enabled_containers
