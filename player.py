#!/usr/bin/env python
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID="YOUR_DEVICE_ID"
CLIENT_ID="YOUR_CLIENT_ID"
CLIENT_SECRET="YOUR_CLIENT_SECRET"

while True:
    try:
        reader=SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))
        
        # create an infinite while loop that will always be waiting for a new scan
        while True:
            print("Waiting for record scan...")
            id= reader.read()[0]
            print("Card Value is:",id)
            sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
            
            # DONT include the quotation marks around the card's ID value, just paste the number
            #1
            if (id==357052844410):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:7IneQ0ViJjz9UR0lisWJzJ')
                sleep(2)
            #2    
            elif (id==289742653758):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:3C2MFZ2iHotUQOSBzdSvM7')
                sleep(2)
            #3    
            elif (id==769738869121):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:31qVWUdRrlb8thMvts0yYL')
                sleep(2)
            #4    
            elif (id==427668212218):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:79dL7FLiJFOO0EoehUHQBv')
                sleep(2)
            #5    
            elif (id==219916011786):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6mlRdEExXqk8Git4nghBSL')
                sleep(2)
            #6    
            elif (id==222467066340):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0ODLCdHBFVvKwJGeSfd1jy')
                sleep(2)
            #7    
            elif (id==1045943159151):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:5xG9gJcs9ut3qDWezHUlsX')
                sleep(2)
            #8    
            elif (id==1047704701211):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:5BRhg6NSEZOj0BR6Iz56fR')
                sleep(2)
            #9    
            elif (id==359503301119):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6QC8G4HVk9lkbpxugU7ZgF')
                sleep(2)
            #10    
            elif (id==82058479888):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:06ZMpecsvvoHGWJHlc2St7')
                sleep(2)            
            #11    
            elif (id==978498619689):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:4xcjwu5Lyyu0uYTknhuK7X')
                sleep(2)
            #12    
            elif (id==632200104376):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6KT8x5oqZJl9CcnM66hddo')
                sleep(2)
            #13    
            elif (id==85598341627):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6kf46HbnYCZzP6rjvQHYzg')
                sleep(2)
            #14    
            elif (id==357859002631):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6IGpQUt0KNi5rBUXZZOFI6')
                sleep(2)
            #15    
            elif (id==704342002010):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6y9LbrjY2TpaLvtbE7FTkc')
                sleep(2)
            #16    
            elif (id==837922195932):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:7f6xPqyaolTiziKf5R5Z0c')
                sleep(2) 
            #17    
            elif (id==494006110576):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:7xV2TzoaVc0ycW7fwBwAml')
                sleep(2)
            #18    
            elif (id==701221505505):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:5r36AJ6VOJtp00oxSkBZ5h')
                sleep(2)
            #19    
            elif (id==910232062267):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:1FZKIm3JVDCxTchXDo5jOV')
                sleep(2)
            #20    
            elif (id==288619497833):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:7zeCZY6rQRufc8IHGKyXGX')
                sleep(2)  
            #21    
            elif (id==428793137580):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6uSnHSIBGKUiW1uKQLYZ7w')
                sleep(2)
            #22    
            elif (id==356886055251):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:7kjLKy9JLbwM9F7eDQEnd2')
                sleep(2)
            #23    
            elif (id==977978591567):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6jTUmLtY779ZNYsyugOq2q')
                sleep(2)
            #24    
            elif (id==566685141354):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:64Ky1tqKPfwxhJs6msphWd')
                sleep(2)                 
            #25    
            elif (id==908655200600):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:64yIGFoYJVg66fRXIxIYJr')
                sleep(2)
            #26    
            elif (id==76082574990):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:4un3pLJoCw3WCaSwsTyBXh')
                sleep(2)
            #27    
            elif (id==485882852984):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6rbqqMTScIBxRBlM7DayP1')
                sleep(2)
                
            #28    
            elif (id==970106795543):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:67smHJOf5YlFwad6dAlppm')
                sleep(2)
            #29    
            elif (id==838793693574):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:5c2AzoNyr46fCQM5d8mxE0')
                sleep(2)
            #30    
            elif (id==352168310404):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:h3euz4vS7ezKGnNSwgyvKcd')
                sleep(2)
            #31    
            elif (id==143291971158):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:3tx8gQqWbGwqIGZHqDNrGe')
                sleep(2)
            #32    
            elif (id==348561208925):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0o5xjCboti8vXhdoUG9LYi')
                sleep(2)
            #33    
            elif (id==144046880386):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0mkOUedmYlOzCC4tOm2v0c')
                sleep(2)                
             #34    
            elif (id==761683310284):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6PWXKiakqhI17mTYM4y6oY')
                sleep(2)
            #35    
            elif (id==213554820772):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:1gMxiQQSg5zeu4htBosASY')
                sleep(2)                 
 
# if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
        GPIO.cleanup()
