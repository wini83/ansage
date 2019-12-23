#!/usr/bin/env python
# -*- coding: utf-8 -*-
DELAY_AMPLIFIER = 2
DELAY_SPEAKERS = 1

try:
    import RPi.GPIO as GPIO
except ImportError:
    print("This is not RPi!")

import time

import playsnd
from gtts import gTTS


def downloadMP3(text, outputFile):
    try:
        tts = gTTS(text=text, lang='pl', slow=False)
        tts.save(outputFile)
        return True
    except Exception:
        return False


def play_announcement_simple(file_name):
    try:
        #playsnd.playsound("gong.wav")
        #time.sleep(1)
        playsnd.playsound(file_name)
        return True

    except KeyboardInterrupt:
        return False


def playAnnoucement(file_name):
    tab = [17, 27]
    try:
        GPIO.setmode(GPIO.BCM)  # (GPIO.BOARD)
        GPIO.setup(17, GPIO.OUT)
        time.sleep(DELAY_AMPLIFIER)
        GPIO.setup(27, GPIO.OUT)
        time.sleep(DELAY_SPEAKERS)
        playsnd.playsound("gong.wav")
        time.sleep(1)
        playsnd.playsound(file_name)
        GPIO.cleanup(27)
        time.sleep(DELAY_AMPLIFIER)
        GPIO.cleanup(tab)
        return True

    except KeyboardInterrupt:
        GPIO.cleanup(tab)
        return False
