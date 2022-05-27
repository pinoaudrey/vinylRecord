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
            if (id=='RFID-CARDVALUE-1'):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #2    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #3    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #4    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #5    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #6    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #7    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #8    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #9    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #10    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)            
            #11    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #12    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #13    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #14    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #15    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #16    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2) 
            #13    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #14    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #15    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #16    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)                 
            #17    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #18    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #19    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #20    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)  
            #21    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #22    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #23    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #24    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)                 
            #25    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #26    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #27    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
                
            #28    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #29    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #30    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #31    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #32    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #33    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)                
             #34    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #35    
            elif (id=='RFID-CARDVALUE-2'):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)                 
 
# if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
        GPIO.cleanup()
