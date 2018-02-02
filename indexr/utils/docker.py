import docker


class DockerUtils(object):

    def __init__(self):
        self.client = docker.from_env()

    def get_enabled_containers(self):
      enabled_containers = []
      for c in self.client.containers.list(filters={'label': 'indexr.enable=true'}):
        l = c.labels
        enabled_containers.append({'name': l['indexr.name'], 'url': l['indexr.url'], 'icon': l['indexr.icon']})
      return enabled_containers
