
# Megaphone2MQTT 📢


This is a simple python project for making audio announcements on a Raspberry PI remotely via MQTT. It uses GoogleTTS as engine

## Getting started

### Installation:
```
# Clone Megaphone2mqtt repository
sudo git clone https://github.com/wini83/megaphone2mqtt.git /opt/megaphone2mqtt
sudo chown -R pi:pi /opt/megaphone2mqtt

# Install dependencies (as user "pi")
cd /opt/megaphone2mqtt
pip3 install --upgrade -r requirements.txt
```    

### Configuring:
Before we can start Megaphone2mqtt we need to create from template and edit the configuration.py file. This file contains the configuration which will be used by Megaphone2mqtt.

Create & open the configuration file:
```
cp config-example.py config.py
nano /opt/megaphone2mqtt/config.py
```
For a basic configuration, the default settings are probably good. The only thing we need to change is the MQTT server url and authentication (if applicable). This can be done by changing the section below in your configuration.yaml.

```python
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
```
Save the file and exit.

### Starting Megaphone2MQTT
Now that we have setup everything correctly we can start Megaphone2MQTT.
    cd /opt/megaphone2mqtt
    python3 main.py
When started successfully, you will see something like:
```
    pygame 2.0.1 (SDL 2.0.9, Python 3.7.3)
    Hello from the pygame community. https://www.pygame.org/contribute.html
    error = 0
```
Zigbee2MQTT can be stopped by pressing `CTRL + C.`

### (Optional) Running as a daemon with systemctl
tbd

### (For later) Update Megaphone2MQTT to the latest version
To update Zigbee2MQTT to the latest version, execute:
```
git pull
```
## MQTT topics and message structure
this section describes which MQTT topics are used by Megaphone2MQTT. Note that the base topic (by default `megaphone`) is configurable in the Megaphone2MQTT `config.py`

### megaphone/announce
Publishing messages to this topic allows you to making audio announcements via MQTT. Only accepts JSON messages. An example below
```
{
  "payload": "System started", // text to announce
  "chime": true, // (optional, default = true - plays chime before announcement (not yet implemented)
  "lang": "pl", // (optional) Language of the announcement (not yet implemented)
  "slow": true, // (optional)(not yet implemented)
}
```

### megaphone/state
Contains the state of the app, payloads are:

* `online`: published when the app is running (on startup)
* `offline`: published right app the bridge stops

### megaphone/mode (not yet implemented)
Contains the mode of the app, payloads are: 

* `idle`: tbd
* `Parsing Payload`: tbd
* `Downloading MP3 file`: tbd
* `Playing`: tbd


### megaphone/log
All Megaphone2MQTT logging is published to this topic in the form of `{"level": LEVEL, "message": MESSAGE}, example: {"level": "info", "message": "Download complete"}.` - tbd
