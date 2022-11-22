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
    439162176569: 'spotify:track:2ZBNclC5wm4GtiWaeh0DMx',
    356953818192: 'spotify:track:4RQgqR09VmHn345vRhKQ6T',
    270903477299: 'spotify:track:5MMZJtHOiH1RmQSSe3DJdg',
    919142799840: 'spotify:track:1PFBQ9GzRhX1txT7eHWGf2',
    510012294359: 'spotify:track:5pMmWfuL0FTGshYt7HVJ8P',
    126587181394: 'spotify:track:1q8E1FfFuhd12c5JcJwPxQ',
    56366407614: 'spotify:track:7vUzRjokJu0HTFASRGz6yG',
    1005342885094: 'spotify:track:5ubvP9oKmxLUVq506fgLhk',
    438635143144: 'spotify:track:3SdTKo2uVsxFblQjpScoHy',
    899881305163: 'spotify:track:78J9MBkAoqfvyeEpQKJDzD',
    811716969564: 'spotify:track:1xkLLbpo3y4KNy64EFVB9C',
    449916306615: 'spotify:track:0ctgmKdlPY8xx41wY339Da',
    353952078098: 'spotify:track:0zGLlXbHlrAyBN1x6sY0rb',
    316973647002: 'spotify:track:3pf96IFggfQuT6Gafqx2rt',
    590693991454: 'spotify:track:0iYebKFUSfF72fUu2OW6ZT',
    268705662129: 'spotify:track:0wz1LjDb9ZNEYwOmDJ3Q4b',
    755546850395: 'spotify:track:6l7tK5SsMlN8a9ccgeIkpS',
    1027589473457: 'spotify:track:6cUCckpdlqHJ5Ascf2uH2A',
    650672538871: 'spotify:track:2WfaOiMkCvy7F5fcp2zZ8L',
    210455168046: 'spotify:track:61LtVmmkGr8P9I2tSPvdpf',
    323718153227: 'spotify:track:1qiQduM84A0VeH8Y2uAbqi',
    1060422419470: 'spotify:track:0K2WjMLZYr09LKwurGRYRE',
    547308110862: 'spotify:track:0HPD5WQqrq7wPWR7P7Dw1i',
    601582404738: 'spotify:track:1Mb8WgET5ozEtG0zlibyUy',
    471291861472: 'spotify:track:6MFQeWtk7kxWGydnJB2y36',
    8626510135: 'spotify:track:443sErTxKXGiISwjsEBA9u',
    321286642096: 'spotify:track:6Qm9MaditCcx5V62rVHYqu',
    286673994979: 'spotify:track:4WFeJTXNHIS2wURtwlAkhu',
    494090781798: 'spotify:track:013AWvizllIUEC2FOBzOnh',
    630254601266: 'spotify:track:5ZBeML7Lf3FMEVviTyvi8l',
    852680056815: 'spotify:track:2aQxJc9qixdnYwPpWuyF8Y',
    314188694641: 'spotify:track:1B75hgRqe7A4fwee3g3Wmu',
    717732387213: 'spotify:track:65jrjEhWfAvysKfnojk1i0',
    912893616116: 'spotify:track:648TTtYB0bH0P8Hfy0FmkL',
    69108504878: 'spotify:track:0Hw6SCrtU9pFCjgAONpnGZ',
    


    419251758720: 'exit'
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
