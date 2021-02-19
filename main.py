#!./venv/bin/python3

import yaml

class FileDB:

    __FILENAME__ = "data.fdb"

    def __init__(self):
        try:
            with open(FileDB.__FILENAME__, 'r') as f:
                self.db = yaml.Load(f, Loader=yaml.Loader)
        except e:
            with open(FileDB.__FILENAME__, "w+") as f:
                self.db = yaml.Load(f, Loader=yaml.Loader)

    def save(self):
        to_save = self.db
        with open(FileDB.__FILENAME__, "w") as f:
            yaml.dumb(to_save, f)

    def has(self, device):
        return device in self.db

    def get(self, device):
        if device in self.db:
            return self.db[device]
        else:
            return None

    def write_configuration(self, device, configuration):
        self.db[device]['configuration'] = configuration

    def write_status(self, device, status):
        self.db[device]['status'] = status

    def write_type(self, device, type):
        self.db[device]['type'] = type

def read_configuration(filename):
    with open(filename, 'r') as f:
        return yaml.load(f, Loader=yaml.Loader)


def callback_device_configuration(topic, message):
    pass


def callback_device_type(topic, message):
    pass


def callback_device_status(topic, message):
    pass


def run_mqtt(configuration):
    from mqtt import MqttClient
    mqttc = MqttClient()
    mqttc.subscribe("devices/+/configuration", callback_device_configuration)
    mqttc.subscribe("devices/+/type", callback_device_type)
    mqttc.subscribe("devices/+/status", callback_device_status)

    mqttc.start(
        configuration['mqtt']['host'],
        configuration['mqtt']['port'],
        configuration['mqtt']['keepalive']
    )


def run_webserver(configuration):
    from webserver import WebServer
    server = WebServer()
    server.start(
        configuration['webserver']['port']
    )


def run():
    configuration = read_configuration("configuration.yaml")
    print("hello world!")
    run_mqtt(configuration)
    # run_webserver(configuration)


if __name__ == '__main__':
    run()
