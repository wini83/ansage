import config
from worker import Worker

worker1 = Worker(mqtt_server_ip=config.mqtt_server_ip, mqtt_server_port=config.mqtt_server_port,
                 mqtt_user=config.mqtt_user, mqtt_pass=config.mqtt_pass, mqtt_base_topic=config.base_topic,
                 mp3_filename=config.mp3_filename, ext_amp_conf=config.ext_amplifier)

worker1.run()
