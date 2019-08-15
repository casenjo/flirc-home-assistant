import config
import requests
import sys

# Get the command-line params
action = sys.argv[1]
brightness_percentage = sys.argv[2]

# Establish constants
HA_URL_PATH = "/api/services/homeassistant/turn_" + action

# Build the full URL
url = config.HA_BASE_URL + HA_URL_PATH

# Create some payloads
on_payload = '{"entity_id": "' + config.HA_LIGHTS_GROUP + '", "transition": 1.5, "brightness_pct": ' + brightness_percentage + '}'
off_payload = '{"entity_id": "' + config.HA_LIGHTS_GROUP + '", "transition": 1.5}'

# Choose which payload to use
if action == 'on':
    payload = on_payload

if action == 'off':
    payload = off_payload

# Build HTTP headers
headers = {
    'Authorization': 'Bearer ' + config.BEARER_TOKEN,
    'content-type': 'application/json'
}

# Send over the request to Home Assistant
response = requests.request("POST", url, data=payload, headers=headers)
