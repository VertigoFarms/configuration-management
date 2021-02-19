#!./venv/bin/python3

import yaml



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
    # run_mqtt(configuration)
    # run_webserver(configuration)

    from db import DB
    db = DB()


if __name__ == '__main__':
    run()
