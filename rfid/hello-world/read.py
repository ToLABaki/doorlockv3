#!/usr/bin/env python

import RPi.GPIO as GPIO
import MFRC522
import signal
from subprocess import call
import time


continue_reading = True
# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
rfid = MFRC522.MFRC522()

i=0
while continue_reading:
    # Talk to the module
    (status,TagType) = rfid.MFRC522_Request(rfid.PICC_REQIDL)
    if status == rfid.MI_OK:
        # Try to read
        (status,uid) = rfid.MFRC522_Anticoll()
        if status == rfid.MI_OK:
            # Print the uid of the scanned card
            print uid
            print i
            i=i+1
            time.sleep(1)
