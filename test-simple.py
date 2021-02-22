#!/usr/bin/env python
# -*- coding: utf-8 -*-

from announcer import Announcer

inputs = "Pociąg osobowy do Grodziska Wielkopolskiego odjedzie z toru pierwszego przy peronie drugim"

inp2 = "Uzbrajanie systemu"

def status_change(message):
    print(message)

pa = Announcer()
pa.on_status_change = status_change
pa.say(inp2, chime=True)
