#!/usr/bin/python
# https://abyz.me.uk/rpi/pigpio/index.html
import pigpio
import time

trigger_pin = 4 # BCM numbering - change to what you actually connect
echo_pin = 24   # BCM numbering - change to what you actually connect

last_tick = 0

def callback_func(gpio, level, tick):
    global last_tick
    if level == 1:
        last_tick = tick
    else:
        if tick > last_tick:
            print (round((tick - last_tick) / 58.31), "cm")   # tick is in us

pi = pigpio.pi()

pi.set_mode(trigger_pin , pigpio.OUTPUT)
pi.set_mode(echo_pin, pigpio.INPUT)

echo_pin_callback = pi.callback (echo_pin, pigpio.EITHER_EDGE, callback_func)

# 10 Hz (100ms gap to prevent interference)
rtn = pi.set_PWM_frequency (trigger_pin, 10)   
print ("freq = ", rtn)
pi.set_PWM_range(trigger_pin, 10000)
pi.set_PWM_dutycycle (trigger_pin, 1)  # equivalent to 10us

try:
    while True:
        time.sleep (1)
except KeyboardInterrupt:
    pass

echo_pin_callback.cancel() # to cancel callback
print ("setting PWM off")
pi.set_PWM_dutycycle(trigger_pin, 0) # PWM off
pi.set_PWM_frequency(trigger_pin, 0) # PWM off
