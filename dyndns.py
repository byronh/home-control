import json
import requests
import time

url = 'https://{username}:{password}@domains.google.com/nic/update?hostname={hostname}&myip={ip}'

with open('config.json', 'r') as f:
    config = json.load(f)['dynamic_dns']


def update_dynamic_dns():
    result = requests.get('http://checkip.amazonaws.com')
    ip = result.text.strip()
    result = requests.post(url.format(username=config['username'],
                                      password=config['password'],
                                      hostname=config['hostname'],
                                      ip=ip))
    print(result, result.text)


if __name__ == '__main__':
    time.sleep(10)
    while True:
        update_dynamic_dns()
        time.sleep(600)
