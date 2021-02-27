# noinspection PyUnresolvedReferences
from ext_amp_conf import ExternalAmplifierConfig

# MQTT Server connection
mqtt_server_ip = "192.168.2.100"
mqtt_server_port = 1883
mqtt_user = "wini"
mqtt_pass = "dupa"

# mqtt topic

base_topic = "megaphone"

# control external Amplifier with GPIO

ext_amplifier = None

# ext_amplifier = ExternalAmplifierConfig(gpio_amplifier=17,gpio_speakers=27,delay_amplifier=2, delay_speakers=1)


# Chimes
mp3_filename = "output.mp3"

chime_filename = "gong.wav"
