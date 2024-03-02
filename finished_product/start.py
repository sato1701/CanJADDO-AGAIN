﻿# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

st_pin=24
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(st_pin, GPIO.IN)

def awaiting():
    while(True):
        value= GPIO.input(st_pin)
        print(value)
        if(value==0):
            print("program start")
            break
        time.sleep(1.0)
    time.sleep(30)#パラシュート展開後待機時間
    return