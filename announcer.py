#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import string
import time
from gtts import gTTS, gTTSError
from pygame import mixer
from pygame import time as gtime
from ext_amp_conf import ExternalAmplifierConfig

try:
    # noinspection PyUnresolvedReferences
    import RPi.GPIO as GPIO
except ImportError:
    print("This is not RPi!")


def play_file(filename, volume: float = 1.0):
    mixer.init()
    mixer.music.load(filename)
    mixer.music.set_volume(volume)
    print(volume)
    mixer.music.play()
    while mixer.music.get_busy():
        gtime.Clock().tick(10)
    mixer.music.unload()


class Announcer:

    def __init__(self, mp3_filename: string = "output.mp3",
                 ext_amp_conf: ExternalAmplifierConfig = None):
        self.mp3_filename = mp3_filename
        self.on_status_change = None
        self.ext_amp_conf = ext_amp_conf

    def download_mp3(self, text, lang="pl", slow=False):
        try:
            self.on_status_change("Downloading..")
            tts = gTTS(text=text, lang=lang, slow=slow)
            tts.save(self.mp3_filename)
            self.on_status_change("Download succeed")
            return True
        except gTTSError:
            self.on_status_change("Error! Problem with downloading")
            return False

    def announce(self, payload, play_chime="gong", lang="pl", volume: float = 1.0):

        result = self.download_mp3(payload, lang)
        if result:
            self.on_status_change("Announcing...")
            if self.ext_amp_conf is None:
                self._play_announcement(play_chime, volume)
            else:
                self._play_announcement_ext_amp(play_chime, volume)
            self.on_status_change("Announce completed")
            os.remove(self.mp3_filename)
            return True
        else:
            return False

    def _play_announcement(self, play_chime="gong", volume: float = 1.0):
        try:
            self._play_chime(play_chime,volume)
            play_file(self.mp3_filename, volume)
            return True
        except KeyboardInterrupt:
            return False

    # noinspection PyMethodMayBeStatic
    def _play_chime(self, chime="gong", volume: float = 1.0):
        if chime == "gong":
            play_file(f'{chime}.wav', volume)
            time.sleep(1)
        elif chime == "none":
            time.sleep(0.001)
        else:
            play_file(f'gong.wav', volume)
            time.sleep(1)

    def _play_announcement_ext_amp(self, play_chime="gong", volume: float = 1.0):
        if self.ext_amp_conf is None:
            return False
        tab = [self.ext_amp_conf.gpio_amplifier, self.ext_amp_conf.delay_speakers]
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.ext_amp_conf.gpio_amplifier, GPIO.OUT)
            time.sleep(self.ext_amp_conf.delay_amplifier)
            GPIO.setup(self.ext_amp_conf.gpio_speakers, GPIO.OUT)
            time.sleep(self.ext_amp_conf.delay_speakers)
            self._play_chime(play_chime, volume)
            play_file(self.mp3_filename, volume)
            GPIO.cleanup(27)
            time.sleep(self.ext_amp_conf.delay_amplifier)
            GPIO.cleanup(tab)
            return True
        except KeyboardInterrupt:
            GPIO.cleanup(tab)
            return False
