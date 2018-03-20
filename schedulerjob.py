LIGHT_PIN1=18
LIGHT_PIN2=24
LIGHT_PIN3=23
LIGHT_PIN4=25
LIGHT_PIN5=20
LIGHT_PIN6=21


import schedule
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LIGHT_PIN1,GPIO.OUT)
GPIO.setup(LIGHT_PIN2,GPIO.OUT)
GPIO.setup(LIGHT_PIN3,GPIO.OUT)
GPIO.setup(LIGHT_PIN4,GPIO.OUT)
GPIO.setup(LIGHT_PIN5,GPIO.OUT)
GPIO.setup(LIGHT_PIN6,GPIO.OUT)

def job():
    print "i'm working"
    GPIO.output(LIGHT_PIN1,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LIGHT_PIN2,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LIGHT_PIN3,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LIGHT_PIN4,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LIGHT_PIN5,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LIGHT_PIN6,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LIGHT_PIN1,GPIO.LOW)
    time.sleep(1)
    GPIO.output(LIGHT_PIN2,GPIO.LOW)
    time.sleep(1)
    GPIO.output(LIGHT_PIN3,GPIO.LOW)
    time.sleep(1)
    GPIO.output(LIGHT_PIN4,GPIO.LOW)
    time.sleep(1)
    GPIO.output(LIGHT_PIN5,GPIO.LOW)
    time.sleep(1)
    GPIO.output(LIGHT_PIN6,GPIO.LOW)
    
    

schedule.every(6).seconds.do(job)
schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    #time.sleep(6)
