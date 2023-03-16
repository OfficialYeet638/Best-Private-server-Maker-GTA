import vlc
import pytube
import os
import ctypes
from ctypes import cast, POINTER, windll
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc

#Set max volume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()
volume.GetVolumeRange()
volume.SetMasterVolumeLevel(0, None)

#max screen brightness
sbc.set_brightness(100)

# Download video
url = 'https://youtu.be/dQw4w9WgXcQ'
youtube = pytube.YouTube(url)
video = youtube.streams.filter(progressive=True, file_extension='mp4').first()
filename = video.default_filename
video.download()

# Create VLC media player
instance = vlc.Instance('--no-xlib')
player = instance.media_player_new()

# Set volume and brightness to maximum
player.audio_set_volume(100)

# Play video in full screen
media = instance.media_new(os.path.abspath(filename))
media.get_mrl()
player.set_fullscreen(True)
player.set_media(media)
player.play()

# Wait for video to finish
while True:
    state = player.get_state()
    if state == vlc.State.Ended or state == vlc.State.Error:
        break
    sbc.set_brightness(100)
    volume.SetMute(0, None)
    volume.SetMasterVolumeLevel(0, None)

