#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
from announcer import Announcer

inputs = "Pociąg osobowy do Grodziska Wielkopolskiego odjedzie z toru pierwszego przy peronie drugim"

inp2 = "Uzbrajanie systemu"


def status_change(message):
    print(message)


pa = Announcer(mp3_filename=config.mp3_filename,
               ext_amp_conf=config.ext_amplifier)
pa.on_status_change = status_change
pa.say(inp2, play_chime="gong")
