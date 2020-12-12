import pygame
from pygame import mixer  # Load the required library

from platform import system

class PlaysoundException(Exception):
    pass


def _playsoundWin(sound, block = True):
    mixer.init()
    mixer.music.load(sound)
    mixer.music.play()
    while mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    mixer.music.unload()

def _playsoundNix(sound, block = True):
    import os
    os.system("mplayer  -ao alsa -really-quiet -noconsolecontrols "+sound)


system = system()

if system == 'Windows':
    playsound = _playsoundWin
else:
    playsound = _playsoundNix

del system