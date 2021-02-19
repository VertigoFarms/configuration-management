#!./env/bin/python3

import paho.mqtt.client as mqtt
from id import ID
import yaml


class MqttClient:
    #  PRIVATE
    def __init__(self):
        self.__id = ID()
        self.__client = mqtt.Client()
        self.__client.on_connect = self.__on_connect
        self.__client.on_message = self.__on_message
        self.__client.will_set(f"devices/{self.__id.get()}/status", "offline")
        self.__subscribed = {}

    def __on_connect(self, client, userdata, flags, rc):
        for topic, (cb, qos) in self.__subscribed.items():
            self.__client.subscribe(topic, qos)
        self.__client.publish(f"devices/{self.__id.get()}/status", "online")

    def __on_message(self, client, userdata, message):
        if message.topic in self.__subscribed:
            (cb, qos) = self.__subscribed[message.topic]
            if cb:
                cb(message.topic, message.payload.decode('utf-8'))

    #  PUBLIC
    def id(self):
        return self.__id.get()

    def start(self, host, port, keepalive):
        self.__client.loop_start()
        self.__client.connect(
            host,
            port,
            keepalive
        )

    def stop(self):
        self.__client.loop_stop()

    def publish(self, topic, payload=None, qos=0, retain=False):
        self.__client.publish(topic, payload, qos, retain)

    def subscribe(self, topic, callback, qos=0):
        assert (None != topic)
        assert (None != callback)
        self.__subscribed[topic] = (callback, qos)
        self.__client.subscribe(topic, qos)
