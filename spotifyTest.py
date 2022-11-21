import spotipy
from spotipy.oauth2 import SpotifyOAuth

from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

from time import sleep


DEVICE_ID = "e2a25c343e92c413d53a049b0424db513b1e8376"
CLIENT_ID = '0de7a5b2dd2c42379211c6d1dceb25ec'
CLIENT_SECRET = 'e43cbf9c244f428187b85069a82f9554'

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri="http://localhost:8080",
                                                scope="user-read-playback-state,user-modify-playback-state"))

playlisturi = 'spotify:playlist:7DM159dKkjm0Mgu2gFARp0'


# Transfer playback to the Raspberry Pi if music is playing on a different device
sp.transfer_playback(device_id=DEVICE_ID, force_play=False)

# Play the spotify track at URI with ID 45vW6Apg3QwawKzBi03rgD (you can swap this for a diff song ID below)
sp.start_playback(device_id=DEVICE_ID, context_uri = playlisturi)

