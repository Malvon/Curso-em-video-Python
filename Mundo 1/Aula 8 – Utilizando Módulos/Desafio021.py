'''Faça um programa em Python que abra e reproduza um arquivo mp3'''
import time

from pygame import mixer
mixer.init()
mixer.music.load('Desafio021.mp3')
mixer.music.play()
from time import sleep
sleep(360)
