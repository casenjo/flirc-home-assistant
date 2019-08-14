import requests
import sys
from pprint import pprint

action = sys.argv[1]
brightness_percentage = sys.argv[2]

HA_BASE_URL = ""
HA_URL_PATH = "/api/services/homeassistant/turn_" + action
BEARER_TOKEN = ""

url = HA_BASE_URL + HA_URL_PATH

on_payload = '{"entity_id": "group.living_room_lights", "transition": 1.5, "brightness_pct": ' + brightness_percentage + '}'
off_payload = '{"entity_id": "group.living_room_lights", "transition": 1.5}'

headers = {
    'Authorization': 'Bearer ' + BEARER_TOKEN,
    'content-type': 'application/json'
}
if action == 'on':
    payload = on_payload

if action == 'off':
    payload = off_payload

response = requests.request("POST", url, data=payload, headers=headers)


# the filename
#print(sys.argv[0])
# the first after the filename: on/off
#print(sys.argv[1])
# the second after the filename: transition value
#print(sys.argv[2])
# the third after the filename: percentage brightness
#print(sys.argv[3])

# the Nth after the filename
# print(sys.argv[N])



