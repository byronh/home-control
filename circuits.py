import datetime
import requests
import time

import RPi.GPIO as io

bounce_time = 100
host = 'http://localhost:8080'
pir_pin = 18

io.setmode(io.BCM)
io.setup(pir_pin, io.IN, pull_up_down=io.PUD_DOWN)


def on_motion(channel):
    time.sleep(1)
    if not io.input(pir_pin):
        return
    io.remove_event_detect(pir_pin)

    now = datetime.datetime.now()
    if 16 <= now.hour <= 23 or 0 <= now.hour <= 5:
        requests.get('{}/api/lights/on'.format(host))
        if now.weekday() <= 4 and 16 <= now.hour <= 21:
            requests.get('{}/api/desktop/on'.format(host))
    elif 7 <= now.hour <= 9:
        requests.get('{}/api/lights/off'.format(host))

    time.sleep(2)
    io.add_event_detect(pir_pin, io.RISING, callback=on_motion, bouncetime=bounce_time)


io.add_event_detect(pir_pin, io.RISING, callback=on_motion, bouncetime=bounce_time)

while True:
    time.sleep(10)
