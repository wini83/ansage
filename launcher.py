#!/usr/bin/env python
# -*- coding: utf-8 -*-

import engine
inputs =  "Pociąg osobowy do Grodziska Wielkopolskiego odjedzie z toru pierwszego przy peronie drugim"

files = "output.mp3"
stra  = inputs.decode("'UTF-8")
print "Pobieranie"
engine.downloadMP3(stra,files)
print "Odtwarzanie"
engine.playAnnoucement(files)