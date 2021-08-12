import pathlib

import blindinglights.playa as playa

try:
    import board
    import neopixel
except ImportError:
    import blindinglights.dummy.board as board
    import blindinglights.dummy.neopixel as neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 100) # Define the lightstrip, and how many LEDs to use on it.

def Rainbow(speed):
    color = [255, 0, 0]
    for x in range (0,254):
        pixels.fill((color[0], color[1], color[2])) # Set all pixels to the current color.
        color[1] = color[1] + 1
        time.sleep(1/speed)
    for x in range (0,254):
        pixels.fill((color[0], color[1], color[2])) # Set all pixels to the current color.
        color[0] = color[0] - 1
        time.sleep(1/speed)
    for x in range (0,254):
        pixels.fill((color[0], color[1], color[2])) # Set all pixels to the current color.
        color[2] = color[2] + 1
        time.sleep(1/speed)
    for x in range (0,254):
        pixels.fill((color[0], color[1], color[2])) # Set all pixels to the current color.
        color[1] = color[1] - 1
        time.sleep(1/speed)
    for x in range (0,200):
        pixels.fill((color[0], color[1], color[2])) # Set all pixels to the current color.
        color[0] = color[0] + 1
        time.sleep(1/speed)
    pixels.fill((255,255,255)) # Set all pixels to the current color.

def ColorFlash(color, delay=0.01):
    pixels.fill((color[0], color[1], color[2]))
    time.sleep(0.01)
    pixels.fill((0, 0, 0))

def ColorFallOff(color, length=25, delay=0.01, division=2):
    for x in range(0,length):
        pixels.fill((color[0], color[1], color[2]))
        color[0] = color[0] / division
        color[1] = color[1] / division
        color[2] = color[2] / division
        time.sleep(delay)


def do_colors ():
    # Initial Ambient Notes
    time.sleep(1.26)
    ColorFallOff([255,100,0],delay=0.02, division=1.05, length=150)

    ColorFallOff([255,255,0],delay=0.04, length=15)
    time.sleep(0.01)
    ColorFallOff([200,200,0],delay=0.02, length=15)
    time.sleep(0.06)
    ColorFallOff([150,150,0], length=5)
    time.sleep(0.08)
    ColorFallOff([100,100,0], length=5)
    time.sleep(0.08)
    ColorFallOff([50,50,0], length=5)
    time.sleep(0.18)
    ColorFallOff([25,25,0], length=20)
    time.sleep(0.08)
    ColorFallOff([15,15,0])


    # Initial Drum Sequence
    time.sleep(2.65)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.34)
    ColorFlash([0,0,255]) # Snare
    time.sleep(0.34)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.34)
    ColorFlash([0,0,255]) # Snare
    time.sleep(0.34)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.34)
    ColorFlash([0,0,255]) # Snare
    time.sleep(0.34)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.1)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.2)
    ColorFlash([0,0,255]) # Snare

    time.sleep(0.2)

    ColorFlash([255,0,0]) # Kick
    time.sleep(0.34)
    ColorFlash([0,0,255]) # Snare
    time.sleep(0.34)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.34)
    ColorFlash([0,0,255]) # Snare
    time.sleep(0.34)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.34)
    ColorFlash([0,0,255]) # Snare
    time.sleep(0.34)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.1)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.2)
    ColorFlash([0,0,255]) # Snare

    time.sleep(0.3)


    # Initial Note Sequence
    ColorFallOff([255,255,0])
    time.sleep(0.2)
    ColorFallOff([255,255,0])
    time.sleep(0.10)
    ColorFallOff([255,255,0], length=5)
    time.sleep(0.08)
    ColorFallOff([255,255,0], length=5)
    time.sleep(0.08)
    ColorFallOff([255,255,0], length=5)
    time.sleep(0.18)
    ColorFallOff([255,255,0], length=20)
    time.sleep(0.08)
    ColorFallOff([255,255,0])

    time.sleep(0.1)

    ColorFallOff([255,255,0])
    time.sleep(0.2)
    ColorFallOff([255,255,0])
    time.sleep(0.10)
    ColorFallOff([255,255,0], length=5)
    time.sleep(0.08)
    ColorFallOff([255,255,0], length=5)
    time.sleep(0.08)
    ColorFallOff([255,255,0], length=5)
    time.sleep(0.18)
    ColorFallOff([255,255,0], length=20)
    time.sleep(0.08)
    ColorFallOff([255,255,0])

    time.sleep(0.05)
    ColorFallOff([255,255,0], length=5)
    time.sleep(0.08)
    ColorFallOff([255,255,0], length=5)
    time.sleep(0.18)
    ColorFallOff([255,255,0], length=5)
    time.sleep(0.18)
    ColorFallOff([255,255,0], length=20)
    time.sleep(0.22)
    ColorFallOff([255,255,0], length=5)
    time.sleep(0.08)
    ColorFallOff([255,255,0], length=5)
    time.sleep(0.18)
    ColorFallOff([255,255,0], length=5)
    time.sleep(0.18)
    ColorFallOff([255,255,0], length=20)
    time.sleep(0.18)
    ColorFallOff([255,255,0], length=20)

    # Drum Sequence Finishing Initial Note Sequence
    time.sleep(0.05)
    ColorFlash([0,0,255]) # Snare
    time.sleep(0.34)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.34)
    ColorFlash([0,0,255]) # Snare
    time.sleep(0.34)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.34)
    ColorFlash([0,0,255]) # Snare
    time.sleep(0.34)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.1)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.2)
    ColorFlash([0,0,255]) # Snare

    time.sleep(0.2)


    # Initial Vocals Drum Sequence
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.34)
    ColorFlash([0,0,255]) # Snare
    time.sleep(0.34)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.34)
    ColorFlash([0,0,255]) # Snare
    time.sleep(0.34)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.34)
    ColorFlash([0,0,255]) # Snare
    time.sleep(0.34)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.1)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.2)
    ColorFlash([0,0,255]) # Snare

    time.sleep(0.25)

    ColorFlash([255,0,0]) # Kick
    time.sleep(0.35)
    ColorFlash([0,0,255]) # Snare
    time.sleep(0.35)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.35)
    ColorFlash([0,0,255]) # Snare
    time.sleep(0.35)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.34)
    ColorFlash([0,0,255]) # Snare
    time.sleep(0.34)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.1)
    ColorFlash([255,0,0]) # Kick
    time.sleep(0.2)
    ColorFlash([0,0,255]) # Snare


    time.sleep(0.1)
    pixels.fill((255, 255, 255))



    time.sleep(16.85)


    # Prechorus Bass Line

    pixels.fill((0, 255, 0))
    time.sleep(2.8)
    pixels.fill((255, 0, 255))
    time.sleep(2.8)
    pixels.fill((0, 255, 255))
    time.sleep(2.8)
    ColorFallOff([0, 255, 0], division=1.05, length=100)
    time.sleep(0.8)

    # Chorus
    Rainbow(100)

def do_light_show (music_file: pathlib.Path):
    with playa.Playa (music_file):
        do_colors ()
