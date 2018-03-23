import RPi.GPIO as GPIO
import time 
import sendmail 
import os 

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)

count = 0
while True:
	input_state = GPIO.input(18)
	if input_state == True: 
		os.system("sudo service motion start")
		sendmail.send_email("____email____", "Motion Detetcted" + str(count), ":8081")
		count += 1
		time.sleep(60)
	else: 
		os.system("sudo service motion stop")
		time.sleep(15)

