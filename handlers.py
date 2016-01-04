import json
import requests
import tornado.web
from wakeonlan import wol

with open('config.json', 'r') as f:
    config = json.load(f)


class DesktopOnHandler(tornado.web.RequestHandler):
    def get(self):
        mac_address = config['desktop_mac_address']
        print('Sending magic packet to %s'.format(mac_address))
        wol.send_magic_packet(mac_address)
        return self.finish({'success': True})


def set_light_state(data):
    for group in config['groups']:
        for index in group['indices']:
            url = '{}/api/{}/lights/{}/state'.format(config['bridge_url'], config['bridge_username'], index)
            response = requests.put(url, json=data)
            response.raise_for_status()
            result = response.json()[0]
            if 'error' in result:
                print(result)


class LightsOnHandler(tornado.web.RequestHandler):
    def get(self):
        print('Turning lights on')
        set_light_state({'on': True, 'bri': 254})
        return self.finish({'success': True})


class LightsDimHandler(tornado.web.RequestHandler):
    def get(self):
        print('Dimming lights')
        set_light_state({'on': True, 'bri': 140})
        return self.finish({'success': True})


class LightsOffHandler(tornado.web.RequestHandler):
    def get(self):
        print('Turning lights off')
        set_light_state({'on': False})
        return self.finish({'success': True})
