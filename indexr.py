from flask import Flask, render_template, url_for
import docker

app = Flask(__name__)


@app.route('/')
def index():
  client = docker.from_env()
  urls = [] 
  for c in client.containers.list(filters={'label': 'indexr.enable=true'}):
      l = c.labels
      icon = url_for('static', filename='icons/' + l['indexr.icon'])
      urls.append({'name': l['indexr.name'], 'url': l['indexr.url'], 'icon': icon})
  return render_template('index.html', containers=urls) 
