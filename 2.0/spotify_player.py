#!/usr/bin/env python
import datetime
import os
import sys
import time
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
import traceback
import logging as log
from songMap import songMap

datetimenow = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
log.basicConfig(level=log.INFO,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%d-%b-%y %H:%M:%S',
                handlers=[log.FileHandler("./logs/debug-" + datetimenow + ".log"), log.StreamHandler(sys.stdout)])

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

rpi="5b95d37ad488736f2ec255666715b71c6c07eadf"
iphone="b5b0b22eeb0edf9258d9ae86b2827bf0154f3b21"
mac="0ccfdb463ff9bf478f07095da1b431b9f869c642"

DEVICE_ID=rpi                         
CLIENT_ID="b8b7f917323244aeadfcdd32eaabbf70"
CLIENT_SECRET="7ca91ad2fc014060bf58b69c406f9725"

CHANGE_DESTINATION_CARD = 703174690857
PLAY_PAUSE_CARD = 155382919085
NEXT_CARD = 346868157546
PREV_CARD = 426989849494
SHUFFLE_CARD = 494766394154

SPECIAL_CARDS = [
    CHANGE_DESTINATION_CARD,
    PLAY_PAUSE_CARD,
    NEXT_CARD,
    PREV_CARD,
    SHUFFLE_CARD,
]

IS_PLAYING = False
IS_SHUFFLE = False
IS_REPEAT = False
CURRENT_SONG = ""
CURRENT_CONTEXT_URI = None
CURRENT_PROGRESS = 0
AVAILABLE_DEVICES = []

def play_accept():
    os.system("mpg123 accept.mp3 >/dev/null 2>&1")

def play_error():
    os.system("mpg123 error.mp3 >/dev/null 2>&1")

def play_connect_device():
    os.system("mpg123 connect_device.mp3 >/dev/null 2>&1")

def play_shuffle_on():
    os.system("mpg123 shuffle_on.mp3 >/dev/null 2>&1")

def play_shuffle_off():
    os.system("mpg123 shuffle_off.mp3 >/dev/null 2>&1")

def play_startup():
    os.system("mpg123 startup.mp3 >/dev/null 2>&1")

  

while True:
    try:
        reader=SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))
        

        def get_state():
            global IS_PLAYING
            global IS_SHUFFLE
            global IS_REPEAT
            global CURRENT_CONTEXT_URI
            global CURRENT_PROGRESS
            global CURRENT_SONG
            global AVAILABLE_DEVICES
            data = sp.current_playback()
            if data is None:
                # play_error()
                return
            IS_PLAYING =data['is_playing']
            IS_SHUFFLE = data['shuffle_state']
            IS_REPEAT = False if data['repeat_state'] == 'off' else True
            CURRENT_CONTEXT_URI = data['context']['uri'] if data['context'] is not None else None
            CURRENT_SONG = data['item']['uri']
            update_device_list()
            CURRENT_PROGRESS = data['progress_ms'] if data['progress_ms'] is not None else 0

        def update_device_list():
            global AVAILABLE_DEVICES
            try:
                AVAILABLE_DEVICES = sp.devices()['devices']
            except Exception as e:
                log.error(e)
                AVAILABLE_DEVICES = []


        def play_song(song):    
            if CURRENT_CONTEXT_URI is not None and CURRENT_SONG == song:
                sp.start_playback(device_id=DEVICE_ID, context_uri=CURRENT_CONTEXT_URI, offset={"position": CURRENT_SONG}, position_ms=CURRENT_PROGRESS)
            else:
                sp.start_playback(device_id=DEVICE_ID, uris=song, position_ms=CURRENT_PROGRESS)
            
        def play_album(album):
            sp.start_playback(device_id=DEVICE_ID, context_uri=album)

        def next_track():
            log.info("Next Track")
            sp.next_track(device_id=DEVICE_ID)
        
        def prev_track():
            log.info("Previous Track")
            sp.previous_track(device_id=DEVICE_ID)

        def play_pause():
            if IS_PLAYING:
                log.info("Pausing Playback")
                sp.pause_playback(device_id=DEVICE_ID)
            else:
                log.info("Resuming Playback")
                play_song([CURRENT_SONG])

        def shuffle():
            if IS_SHUFFLE:
                log.info("Shuffle Off")
                play_shuffle_off()
                sp.shuffle(device_id=DEVICE_ID, state=False)
            else :
                log.info("Shuffle On")
                play_shuffle_on()
                sp.shuffle(device_id=DEVICE_ID, state=True)

        def repeat():
            if IS_REPEAT:
                log.info("Repeat Off")
                sp.repeat(device_id=DEVICE_ID, state=False)
            else:
                log.info("Repeat On")
                sp.repeat(device_id=DEVICE_ID, state=True)
        

        def next_player():
            for i in range(1, 4):
                try:
                    global DEVICE_ID
                    ids = list(map(lambda d: d['id'], AVAILABLE_DEVICES))
                    if len(AVAILABLE_DEVICES) > 1 and DEVICE_ID is not None:
                        current_index = ids.index(DEVICE_ID)
                        next_index = (current_index + i) % len(ids)
                        log.info("now playing on " + AVAILABLE_DEVICES[next_index]['name'])
                        DEVICE_ID = AVAILABLE_DEVICES[next_index]['id']
                    else:
                        wait_for_device()
                    sp.transfer_playback(device_id=DEVICE_ID, force_play=True)
                    return
                except:
                    log.error(e)
                    log.error("Error while transferring playback, Retyring...", exc_info=True)
                    play_error()
                    pass
            else:
                log.error("Failed to transfer playback", exc_info=True)
                play_error()

        def wait_for_device():
            i = 0
            while True:
                try:
                    global DEVICE_ID
                    update_device_list() 
                    if len(AVAILABLE_DEVICES) > 0:
                        ids = list(map(lambda d: d['id'], AVAILABLE_DEVICES))
                    else:
                        ids = None 
                    if ids is not None and len(ids) > 0:
                        if DEVICE_ID is not None and DEVICE_ID in ids:
                            return
                        elif i < 4:
                            i += 1
                            sleep(0.5)
                            continue
                        elif rpi in ids:
                            DEVICE_ID = rpi
                        else :
                            DEVICE_ID = ids[0]
                    else :
                        log.warn("No devices found. Please open spotify and select a device")
                        play_connect_device()
                        time.sleep(1)
                except e:
                    log.error(e)
                    log.error("Error while waiting for device, Retyring...")
                    play_connect_device()
                    sleep(3)
                    pass
        
        def handle_special(id):
            get_state()
            if id == CHANGE_DESTINATION_CARD: 
                next_player()
            elif id == PLAY_PAUSE_CARD:
                play_pause()
            elif id == SHUFFLE_CARD:
                shuffle()
            elif id == NEXT_CARD:  
                next_track() 
            elif id == PREV_CARD:  
                prev_track()

        # create an infinite while loop that will always be waiting for a new scan
        while True:
            try:
                get_state()
                wait_for_device()
                sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
                break
            except Exception as e:
                sleep(2)
                pass

        play_startup()
        while True:
            
            log.info("Waiting for record scan...")
            id= reader.read()[0]
            if id in SPECIAL_CARDS:
                play_accept()
                handle_special(id)
                sleep(1)
                continue
            if id in songMap:
                play_accept()
                if songMap[id]["type"] == "song":
                    log.info("Playing Song: " + songMap[id]["name"])
                    CURRENT_PROGRESS=0
                    CURRENT_CONTEXT_URI = None
                    play_song([songMap[id]["sid"]])
                elif songMap[id]["type"] == "album":
                    log.info("Playing Album: " + songMap[id]["name"])
                    play_album(songMap[id]["sid"])
                elif songMap[id]["type"] == "playlist":
                    log.info("Playing Playlist: " + songMap[id]["name"])
                    play_album(songMap[id]["sid"])
                elif songMap[id]["type"] == "artist":
                    log.info("Playing Artist: " + songMap[id]["name"])
                    play_album(songMap[id]["sid"])
            else :
                log.warn("RFID card not registered. Ignoring")
                log.warn("Card Value is:",id)
                play_error()
            sleep(1)

    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        play_error()
        log.error(e, exc_info=True)

        sleep(1)
        pass

    finally:
        sleep(1)
        log.error("Cleaning  up...")
        GPIO.cleanup()
