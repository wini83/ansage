import paho.mqtt.client as mqtt
import json
import time
import sys
from announcer import Announcer
import config

import signal


class Worker(object):

    def __init__(self):
        self.client = mqtt.Client()
        signal.signal(signal.SIGINT, self.signal_handler)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
        self.client.username_pw_set(config.mqtt_user, password=config.mqtt_pass)
        self.announcer = Announcer()
        self.announcer.on_status_change = self.status_change

    def signal_handler(self, signal, frame):
        print('You pressed Ctrl+C - or killed me with -2')
        print("disconnect handler")
        self.client.publish("{}/state".format(config.base_topic), payload='offline')
        self.client.disconnect()
        sys.exit(0)

    def status_change(self, message):
        print(message)
        self.client.publish("{}/log".format(config.base_topic), payload=message)


    def on_connect(self, client, userdata, flags, rc):
        print("error = " + str(rc))
        self.client.publish("{}/state".format(config.base_topic), payload='online')
        self.client.subscribe("{}/announce".format(config.base_topic))

    def on_disconnect(self, userdata, flags, rc):
        print("disconnect on")
        self.client.publish("{}/state".format(config.base_topic), payload='offline')

    def on_message(self, client, userdata, msg):
        my_json = msg.payload.decode('utf8')
        try:
            data = json.loads(my_json)
            print(data)
            payload = data['payload']
            text = '{"payload": "' + payload + '"}'
            self.client.publish("{}/log".format(config.base_topic), payload=payload)
            self.announcer.say(payload)
        except:
            e = sys.exc_info()[0]
            print(e)
            self.client.publish("{}/log".format(config.base_topic), payload='wrong announce structure')

    def run(self):
        self.client.connect(config.mqtt_server_ip, config.mqtt_server_port, 60)
        self.client.loop_start()
        while True:
            time.sleep(10)
