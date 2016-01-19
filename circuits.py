import datetime
import requests
import time

import gpiozero as io

host = 'http://localhost:8080'
pir = io.MotionSensor(pin=18)


def loop():
    pir.wait_for_active()
    time.sleep(0.5)
    if pir.value != 1:
        return

    now = datetime.datetime.now()
    if 13 <= now.hour <= 23 or 0 <= now.hour <= 5:
        requests.get('{}/api/lights/on'.format(host))
        print('Lights activated')
        if now.weekday() <= 4 and 16 <= now.hour <= 21:
            requests.get('{}/api/desktop/on'.format(host))
            print('Magic packet sent to desktop')
    elif 7 <= now.hour <= 9:
        requests.get('{}/api/lights/off'.format(host))
        print('Lights deactivated')

    time.sleep(30)


if __name__ == '__main__':
    while True:
        loop()
