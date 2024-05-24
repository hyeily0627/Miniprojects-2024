# 2024 05 21 
# Red LED등 점등 

import RPi.GPIO as GPIO
import time

# RGB LED의 핀 번호 설정 
red_pin = 4
green_pin = 6
blue_pin = 5 

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD) 두가지 방법 중 이건 잘 안씀! 

GPIO.setup(red_pin, GPIO.OUT) # 4번핀으로 출력하겠다. 
GPIO.setup(green_pin, GPIO.OUT) # 6번핀으로 출력하겠다. 
GPIO.setup(blue_pin, GPIO.OUT) # 5번핀으로 출력하겠다. 


while(True):
    GPIO.output(red_pin, True)
    GPIO.output(green_pin, False)
    GPIO.output(blue_pin, False)
    time.sleep(0.5) # 0.5초 동안 딜레이
    
    GPIO.output(red_pin, False)
    GPIO.output(green_pin, True)
    GPIO.output(blue_pin, False)
    time.sleep(0.5) # 0.5초 동안 딜레이

    GPIO.output(red_pin, False)
    GPIO.output(green_pin, False)
    GPIO.output(green_pin, True)
    time.sleep(0.5) # 0.5초 동안 딜레이

    # GPIO.output(red_pin, True)
    # GPIO.output(green_pin, True)
    # GPIO.output(green_pin, True)
    # time.sleep(0.5) # 0.5초 동안 딜레이

