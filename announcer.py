#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import config
from gtts import gTTS, gTTSError
from pygame import mixer

from pygame import time as gtime

try:
    import RPi.GPIO as GPIO
except ImportError:
    print("This is not RPi!")


def play_sound(sound):
    mixer.init()
    mixer.music.load(sound)
    mixer.music.play()
    while mixer.music.get_busy():
        gtime.Clock().tick(10)
    mixer.music.unload()


class Announcer:

    def __init__(self, simple=True):
        self.simple = simple
        self.mp3_filename = config.mp3_filename
        self.chime_filename = config.mp3_filename
        self.on_status_change = None

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

    def say(self, payload, chime=False, lang="pl"):

        result = self.download_mp3(payload, lang)
        if result:
            self.on_status_change("Announcing...")
            if self.simple:
                self._play_announcement_simple(chime)
            else:
                self._play_announcement(chime)
            self.on_status_change("Announce completed")
            os.remove(self.mp3_filename)
            return True
        else:
            return False

    def _play_announcement_simple(self, chime=True):
        try:
            if chime:
                play_sound(config.chime_filename)
                time.sleep(1)
            play_sound(self.chime_filename)
            return True
        except KeyboardInterrupt:
            return False

    def _play_announcement(self, chime=True):
        tab = [config.gpio_amplifier, config.delay_speakers]
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(config.gpio_amplifier, GPIO.OUT)
            time.sleep(config.delay_amplifier)
            GPIO.setup(config.gpio_speakers, GPIO.OUT)
            time.sleep(config.delay_speakers)
            if chime:
                play_sound(self.chime_filename)
                time.sleep(1)
            play_sound(self.mp3_filename_name)
            GPIO.cleanup(27)
            time.sleep(config.delay_amplifier)
            GPIO.cleanup(tab)
            return True
        except KeyboardInterrupt:
            GPIO.cleanup(tab)
            return False
