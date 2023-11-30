# pi_stem
playing stem with Raspberry Pi (distance sensor, OLED, camera driven by servo motors etc)

# The first python added to this repository is distance_detect.py
I am using the ultrasonic distance sensor HC-SR04. Most of the python programs found on internet is using the RPi.GPIO library to do software timed PWM on the trigger PIN and then software polling to measure the time of the signal PIN.  This consumes the main loop and is not *very* accurate.

I use the [pigpio library](https://abyz.me.uk/rpi/pigpio/index.html).  It supports hardware timed PWM as well as hardware based PWM.  But since there are only two hardware based PWM PINs and I have used them to drive the two servo motors, I used hardware timed PWM for the ultrasonic sensor.

I set the trigger PIN to make periodic PWM and therefore I do not need to bother to turn it on/off by software.  For the echo PIN, I used a callback function to sense the ON/OFF in the background.  The main loop is now a simply while-sleep to incorporate other logic.
