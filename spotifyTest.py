import spotipy
from spotipy.oauth2 import SpotifyOAuth

from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

from time import sleep

DEVICE_ID = 'e2a25c343e92c413d53a049b0424db513b1e8376'
CLIENT_ID = '0de7a5b2dd2c42379211c6d1dceb25ec'
CLIENT_SECRET = 'e43cbf9c244f428187b85069a82f9554'
GPIO.setmode(GPIO.BOARD)

LED_PIN = 11
GPIO.setup(11, GPIO.OUT)

def flash(PIN):
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
    143916729532: 'spotify:track:3CSpzkoL1XgDBZ1q9aDCUV',
    18424469880: 'spotify:track:6CQaVuICm1WVXyy3SZ5jEI',
    17132493258: 'spotify:track:4U45aEWtQhrm8A5mxPaFZ7',
    675386694123: 'spotify:track:5OkKOkdVTKFrYi6GWXkMzR',
    178226136137: 'spotify:track:0y60itmpH0aPKsFiGxmtnh',
    308836697265: 'spotify:track:4h8VwCb1MTGoLKueQ1WgbD',
    313181996221: 'spotify:track:0ikz6tENMONtK6qGkOrU3c',
    883036980299: 'spotify:track:05wIrZSwuaVWhcv5FfqeH0',
    629667398679: 'spotify:track:1Je1IMUlBXcx1Fz0WE7oPT',
    839902757970: 'spotify:track:3Dy4REq8O09IlgiwuHQ3sk',
    574387853583: 'spotify:track:3496rr5XSGD6n1Z1OKXovb',
    496858956994: 'spotify:track:2DYtBXueUkZyUZAHKJAAIs',
    943134284154: 'spotify:track:3Dnv944x31XU4FFMlkfnWN',
    358413435967: 'spotify:track:70jtZsS59vhmyZSsln0std',
    847177195351: 'spotify:track:2kNYcE79Yu778nqdOgBHEb',
    769522336903: 'spotify:track:7rGMKCgeYXpBecQ1FPb3oc',
    5354952969: 'spotify:track:2g2GkH3vZHk4lWzBjgQ6nY',
    240100443342: 'spotify:track:5rb9QrpfcKFHM1EUbSIurX',
    492548594154: 'spotify:track:1jyddn36UN4tVsJGtaJfem',
    148563952811: 'spotify:track:13mXFvyRyjfIjnag95Rnug',
    911559498206: 'spotify:track:3as6Wz3mwbTnusWhZjTUNr',
    159889955113: 'spotify:track:0qxYx4F3vm1AOnfux6dDxP',
    749474814233: 'spotify:track:6FT83pFXKhDlXDsNJFAHWz',
    743720294834: 'spotify:track:69Qa7czzqraPWZgxpQN405',
    53958613418: 'spotify:track:0293bTPojlkLvyr8ojc74y',
    1082678976325: 'spotify:track:3e09orWFdPkTN7JAxCVc7g',
    993095517377: 'spotify:track:714hERk9U1W8FMYkoC83CO',
    307764337113: 'spotify:track:3aSWQJcWnnqgwYbAgidvlV',
    842956211359: 'spotify:track:3XVBdLihbNbxUwZosxcGuJ',
    305063205238: 'spotify:track:3G2lWP5eg517FkJNt887cf',
    164284269689: 'spotify:track:3v9xlH6BpmRbqL7hgNJhfT',
    571451840958: 'spotify:track:3v9xlH6BpmRbqL7hgNJhfT',
    737544897548: 'spotify:track:23l1kVpqMVREiwU1YAlcr4',
    324348747617: 'spotify:track:4TjrIZw2QxJxbVjdc3XKsj',
    532243487137: 'spotify:track:1PEqh7awkpuepLBSq8ZwqD',
    776820360308: 'spotify:track:72Q0FQQo32KJloivv5xge2',
    957074768918: 'spotify:track:7nCfgsjUCQUogw3MY5tEeR',
    97763924451: 'spotify:track:1xsY8IFXUrxeet1Fcmk4oC',
    1016224423898: 'spotify:track:0GVvRmCoiLkhxJvlZy9bLk',
    265166985654: 'spotify:track:6RANU8AS5ICU5PEHh8BYtH',
    872249230530: 'spotify:track:3C5b21hX1FePgFAGdzk3Uc',
    542444099867: 'spotify:track:2xar08Fq5xra2KKZs5Bw9j',
    526957282517: 'spotify:track:2tUBqZG2AbRi7Q0BIrVrEj',
    926340290895: 'spotify:track:1BwhFXqoIsePt21WyWIttb',
    300045436039: 'spotify:track:6e40mgJiCid5HRAGrbpGA6',
    571702183046: 'spotify:track:5zF200It0lex62TAEflGTt',
    442820991316: 'spotify:track:3OrqExOwr13y6UCI1LGhA4',
    110764885197: 'spotify:track:7cv28LXcjAC3GsXbUvXKbX',
    629684241425: 'spotify:track:0PKmDncVOiNQLO6D1P6PXi',
    760313026974: 'spotify:track:69s4AlXEFyRax2ev96a42r',
    633761104899: 'spotify:track:2oTDOIAdsxPTE7yAp4YOcv',
    161415365807: 'spotify:track:2wSAWEYUHkt92X4SBAPqZE',
    825826673816: 'spotify:track:3XG7bMVcMWLIn2k9jLAaAt',
    89860474086: 'spotify:track:4HGIPyqDxSf863tPOwXiLJ',
    1082192306083: 'spotify:track:5y8zb3grlQonjdqd27K39T',
    1064146961453: 'spotify:track:40NRm1ZLvZpUSCUXAGGZ8J',
    170072409249: 'spotify:track:0uMMLry3hzWGn3q3loqMkm',
    956581421003: 'spotify:track:3sUOaOeKGEXee4AR6ri1CE',
    851596477598: 'spotify:track:1UH4viviUjZnS9aWgPGrk0',
    768431752262: 'spotify:track:7Kszjzps0xbQXyo1pO4KfE',
    118014024023: 'spotify:track:6NDaYWg85ZnJ3Ae0WkILWh',
    893691828722: 'spotify:track:3eMw0VMpuRA9plOkjQ54Kp',
    64711492609: 'spotify:track:7AL1pxI9IwHoXs98G0T8cC',
    959054546060: 'spotify:track:2IY559smG7SXYk229NA2Vl',
    439918467389: 'spotify:track:1CsOQTtxnequA05qBXKpJj',
    496221488357: 'spotify:track:3YhcVZIWyakQSTUJD1YMt4',
    386214599043: 'spotify:track:1MAIJFzQFIQ2Hkm3X5YtCW',
    677836036475: 'spotify:track:5Ts1DYOuouQLgzTaisxWYh',
    950860390163: 'spotify:track:7oHCN849Cytkh7OhOtJOBv',
    269074695302: 'spotify:track:1z6WtY7X4HQJvzxC4UgkSf',
    798530077771: 'spotify:track:6Cfy5wwz2S0TpF6KhE30er',
    1034065413165: 'spotify:track:5hnJCRSo4pxRsaEwT9YusG',
    993130387946: 'spotify:track:28285KFbyCq8sJofn58qlD',
    853141297491: 'spotify:track:6H3Wa6hWR9DRMzMSd4pZkT',
    514022048967: 'spotify:track:7jQBORjiir0pNSKGaHevq9',
    970630759425: 'spotify:track:0oUBuOO4g9P4lREqfqR5nq',
    50585011410: 'spotify:track:4EEjMyQub6tgFVshlM9j1M',
    911106578880: 'spotify:track:6UtfMFnVWLJjHsd3dPcGgB',
    441411574167: 'spotify:track:7oK9VyNzrYvRFo7nQEYkWN',
    820006295908: 'spotify:track:3zopUGxKy1Uz4cKtDGjZry',
    717355163406: 'spotify:track:745H5CctFr12Mo7cqa1BMH',
    1090000651306: 'spotify:track:4nYqRUNPIiPj48YNS1bGJQ',
    567391754665: 'spotify:track:6roSI9jonCiMhPeLZuEn4O',
    516152820810: 'spotify:track:6MdqqkQ8sSC0WB4i8PyRuQ',
    387488351357: 'spotify:track:6IwKcFdiRQZOWeYNhUiWIv',
    1005830674925: 'spotify:track:3X7uFMzJrEE0sxn62qd8Ch',
    368261596405: 'spotify:track:52HAHV1j93s5B8GoTNI7DJ',
    249245341957: 'spotify:track:2ZD42YPLXtzoGlRH51zViF',
    223004460225: 'spotify:track:4gehZ6WYqLOXZpmMEq3Em9',
    932043228356: 'spotify:track:0Oe49j06Bjrxs8PltuVeaW',
    494979974227: 'spotify:track:6naxalmIoLFWR0siv8dnQQ',
    986822154512: 'spotify:track:1EQn3Uc5AyUXoiPLeyCrrg',
    936405304515: 'spotify:track:3oQomOPRNQ5NVFUmLJHbAV',
    159453813036: 'spotify:track:2Ml0l8YWJLQhPrRDLpQaDM',
    964557407338: 'spotify:track:3E7dfMvvCLUddWissuqMwr',
    1080346943455: 'spotify:track:6gcd9amHfYlZrEpxrLYoU9',
    78988903529: 'spotify:track:5uuJruktM9fMdN9Va0DUMl',
    747862951057: 'spotify:track:5lA3pwMkBdd24StM90QrNR',
    537595418976: 'spotify:track:2374M0fQpWi3dLnB54qaLX',
    386902530406: 'spotify:track:4ccM2xBxicGigjLqt6A0YY',
    416816306500: 'spotify:track:0edWHlI2pjWLaetkzojpC3',
    533854099718: 'spotify:track:1V7mHn6zEEUpgysBYxiW9r',
    1031012025570: 'spotify:track:27mhCGdAA8gM7b33KIiB3k',
    83887850628: 'spotify:track:6WCeFNVAXUtNczb7lqLiZU',
    553968600165: 'spotify:track:5IVuqXILoxVWvWEPm82Jxr',
    918805939238: 'spotify:track:66TRwr5uJwPt15mfFkzhbi',
    514996443560: 'spotify:track:5pkd9ib1RgbkAd1R9bIOCa',
    370929239060: 'spotify:track:2ToW7zhGCrVrLU4fiKj9U1',
    402537448698: 'spotify:track:5FMXrphygZ4z3gVDHGWxgl',
    535934343552: 'spotify:track:0EMmVUYs9ZZRHtlADB88uz',
    79676769408: 'spotify:track:7tawDKBYV9059X92D6dr7R',
    788967064603: 'spotify:track:6VeZ970uI0Yi6sjBgyFBrp',
    458372023501: 'spotify:track:7vFoFDWqTX0mHzLfrF1Cfy',
    315648312360: 'spotify:track:3K7Q9PHUWPTaknlbFPThn2',
    392900517772: 'spotify:track:7rix9h010ISulNPU1dmA7o',
    889814975741: 'spotify:track:44AyOl4qVkzS48vBsbNXaC',
    634247578657: 'spotify:track:4r8lRYnoOGdEi6YyI5OC1o',
    49913922698: 'spotify:track:3XcuLPQb1LG13ZJEEa6wUI',
    355646380456: 'spotify:track:4myBMnNWZlgvVelYeTu55w',
    713150891186: 'spotify:track:6ztstiyZL6FXzh4aG46ZPD',
    903598972701: 'spotify:track:3KzgdYUlqV6TOG7JCmx2Wg',
    86706422843: 'spotify:track:78JAqmzSWW9SKUM6MchOrs',
    764589835432: 'spotify:track:2goLsvvODILDzeeiT4dAoR',
    318819206254: 'spotify:track:3MjUtNVVq3C8Fn0MP3zhXa',
    31477143909: 'spotify:track:1nd9moIZkGvWoHtReFqkRY',
    660302595130: 'spotify:track:5X0M16GjlZYN1WjPNzerb5',
    16191718616: 'spotify:track:6o5sSlAsvLcPdrK7HFxXp3',
    624476364634: 'spotify:track:6L2woktiAuW35BrcROmhW5',
    28204205193: 'spotify:track:6vyFAHVKIsp3pdyhlOKMAz',
    830592719252: 'spotify:track:3OeX4IyrnpwkElW5iS8leo',
    513653015792: 'spotify:track:22x73BTJpIkciL7605zZ66',
    727530281467: 'spotify:track:1LeWIs2hP2r5yOQnVuYoI5',
    992592200931: 'spotify:track:4y1LsJpmMti1PfRQV9AWWe',
    661679708579: 'spotify:track:0Qi29hMhf8tIzDpa2BH9MV',
    141787404555: 'spotify:track:3F6czr26ZwGU5O5CHY04Ma',
    705634698480: 'spotify:track:5YJtMNWKe55yr49cyJgxva',
    885923977661: 'spotify:track:39lnzOIUCSNaQmgBHoz7rt',
    485970609224: 'spotify:track:78VG6M1i7JQXBdygmWFwye',
    776921023566: 'spotify:track:5WTxbyWTpoqhdxEN2szOnl',
    599502029825: 'spotify:track:1JyaAeaXVFnVv5ikwWQVQ4',
    1041917150331: 'spotify:track:3N2nIBN3a9J40PIij4gW5F',
    635287766119: 'spotify:track:2hKdd3qO7cWr2Jo0Bcs0MA',
    976898629437: 'spotify:track:78MI7mu1LV1k4IA2HzKmHe',
    452820146481: 'spotify:track:0y03oYS73uWt3OIFGAGyDD',
    342592455829: 'spotify:track:4Z2PtqWOBXJOgQ7UCLO3py',
    535178183928: 'spotify:track:7HW5WIw7ZgZORCzUxv5gW5',
    4063173060: 'spotify:track:1udKn1oNKYQSQ9OmiIWCMu',
    559119271091: 'spotify:track:4356Typ82hUiFAynbLYbPn',
    945868970448: 'spotify:track:3H8Sn0mYsZMPPlMCbebOJ5',
    1084247513511: 'spotify:track:2ATDkfqprlNNe9mYWodgdc',
    640589431980: 'spotify:track:7AqISujIaWcY3h5zrOqt5v',
    247869675961: 'spotify:track:4kP69y3GKHi9tXckfgp4bK',
    1090873066526: 'spotify:track:3FQ26GroLnhQEja48FKYqT',
    343659323389: 'spotify:track:5P11rW6aJErF37MTfRZS31',
    30386559267: 'spotify:track:5kXDF4OmM5COyeo6z97nEk',
    335478981709: 'spotify:track:4fIWvT19w9PR0VVBuPYpWA',
    177219503221: 'spotify:track:5k3U0OGYBccHdKJJu3HrUN',
    4397401112: 'spotify:track:3sl4dcqSwxHVnLfqwF2jly',
    903347380013: 'spotify:track:7v8YDCoM60xCPuSbXerImD',
    643374384199: 'spotify:track:7zw0jBh5Khn08DkDP93yyh',
    628191069390: 'spotify:track:3ZFTkvIE7kyPt6Nu3PEa7V',
    298669769936: 'spotify:track:5iDfnRTdV2mrvMK886TLRg',
    76539364573: 'spotify:track:6Ac4NVYYl2U73QiTt11ZKd',
    86640695569: 'spotify:track:6EuudaFtwibd4tzcWjonb2',
    127459531143: 'spotify:track:7KEajVD9AUG68onXRSFZTv',
    1039987836105: 'spotify:track:6XcoXHCbeyhybWrqHLYWo0',
    458539795639: 'spotify:track:1H5tvpoApNDxvxDexoaAUo',
    609853506669: 'spotify:track:4ZtFanR9U6ndgddUvNcjcG',
    606447797409: 'spotify:track:4cnqxdE2opmhp7MwkvhkAJ',
    844818416745: 'spotify:track:49FYlytm3dAAraYgpoJZux',
    786601542797: 'spotify:track:5oO3drDxtziYU2H1X23ZIp',
    725599519815: 'spotify:track:3e9HZxeyfWwjeyPAMmWSSQ',
    918151627789: 'spotify:track:53KFMdxzi8IJDewiql1Qo3',
    475568669898: 'spotify:track:6UelLqGlWMcVH1E5c4H7lY',
    




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
        flash(LED_PIN)      
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
