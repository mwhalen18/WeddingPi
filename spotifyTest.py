import spotipy
from spotipy.oauth2 import SpotifyOAuth

from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

from time import sleep


DEVICE_ID = "e2a25c343e92c413d53a049b0424db513b1e8376"
CLIENT_ID = '0de7a5b2dd2c42379211c6d1dceb25ec'
CLIENT_SECRET = 'e43cbf9c244f428187b85069a82f9554'
GPIO.setmode(GPIO.BOARD)

LED_PIN = 11
GPIO.setup(11, GPIO.OUT)


scope = 'user-read-private user-read-playback-state user-modify-playback-state playlist-read-private user-read-currently-playing playlist-modify-private playlist-modify-public'

cards = {
    417000990306: 'spotify:track:0V3wPSX9ygBnCm8psDIegu',
    716918890464: 'spotify:track:2rTbSf6sLfFIXI3MKBB6vO',
    208576054462: 'spotify:track:5jkFvD4UJrmdoezzT1FRoP',
    526470743280: 'spotify:track:0PpamSdfQzIAvj5OB9Bz54',
    699294226757: 'spotify:track:7s25THrKz86DM225dOYwnr',
    415221023955: 'spotify:track:5hqOXjG2iZeVeWzAibynl8',
    380441920723: 'spotify:track:3gdewACMIVMEWVbyb8O9sY',
    935599932433: 'spotify:track:5L95vS64rG1YMIFm1hLjyZ',
    122225039710: 'spotify:track:6TXnGAr6DLVYshIrMeP0lZ',
    926020207699: 'spotify:track:5nNmj1cLH3r4aA4XDJ2bgY',
    361550775397: 'spotify:track:2Lv9mFjcIFPn8zyWF89EAe',
    183913546982: 'spotify:track:5619Ojc6t9evEEs3B7Drhe',
    439162176569: 'spotify:track:2ZBNclC5wm4GtiWaeh0DMx'
}

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri='http://google.com',
                                                scope=scope))

playlisturi = 'spotify:playlist:7DM159dKkjm0Mgu2gFARp0'

reader = SimpleMFRC522()

# Transfer playback to the Raspberry Pi if music is playing on a different device
sp.transfer_playback(device_id=DEVICE_ID, force_play=False)

# Play the spotify track at URI with ID 45vW6Apg3QwawKzBi03rgD (you can swap this for a diff song ID below)
sp.start_playback(device_id=DEVICE_ID, context_uri = playlisturi)
tracks = []

while True:
    print('Waiting for RFID scan . . . ')
    id = reader.read()[0]
    print("Card Value is")
    songURI = cards.get(id)
    if songURI in tracks:
        GPIO.output(LED_PIN, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(LED_PIN, GPIO.LOW)
        sleep(0.2)
        GPIO.output(LED_PIN, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(LED_PIN, GPIO.LOW)
        sleep(0.2)
        GPIO.output(LED_PIN, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(LED_PIN, GPIO.LOW)
        sleep(0.2)        
    elif songURI == 'exit':
        sp.pause_playback(device_id = DEVICE_ID)
        break
    else:
        GPIO.output(LED_PIN, GPIO.HIGH)
        sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        sleep(1)
        sp.add_to_queue(songURI, device_id = DEVICE_ID)
        sp.user_playlist_add_tracks(user = 'mwhalen18', playlist_id = playlisturi, tracks = [songURI])
        tracks.append(songURI)
        

GPIO.cleanup()
