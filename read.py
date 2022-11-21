#!/usr/bin/env  python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

reader = SimpleMFRC522()
GPIO.setmode(GPIO.BOARD)

LED_PIN = 11
GPIO.setup(11, GPIO.OUT)

try:
	print('Waiting for scan')
	id = reader.read()[0]
	print("The ID for the card is: ", id)
	GPIO.output(11, GPIO.HIGH) 
	sleep(1)
	GPIO.output(11, GPIO.LOW)
	sleep(1)

finally:
	GPIO.cleanup()
