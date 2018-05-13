import docker


class DockerUtils(object):

    def __init__(self):
        self.client = docker.from_env()

    def get_enabled_containers(self):
        enabled_containers = []
        labels = {'indexr.name', 'indexr.url', 'indexr.icon'}
        for container in self.client.containers.list(filters={'label': 'indexr.enable=true'}):
            if set(labels).issubset(container.labels):
                labels = container.labels
                enabled_containers.append(
                    {'name': labels['indexr.name'], 'url': labels['indexr.url'], 'icon': labels['indexr.icon']})
        return enabled_containers
