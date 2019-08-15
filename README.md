# Flirc Home Assistant
This is a small set of scripts that can be used with Flirc to control your Home Assistant's lighting (and other things, in the future). Mainly running it on Windows, but it could easily be adapted into an OSX or Linux solution.

### The flow is as follows:
- Flirc toggles a keyboard shortcut when a particular remote button signal is sensed
- AutoHotKey detects this shortcut and runs a batch file
- The batch file runs the python script with the proper lighting parameters. Why a batch file? Because it allows the script to run minimized (open to suggestions on better ways to run this lol)
- The python script uses Home Assistant's API to issue the lighting instruction for the desired group of lights

### List of Keystrokes
Ctrl + Alt + ...
U => 25% brightness
I => 50% brightness
O => 75% brightness
P => 100% brightness

## Prerequisites
- Python's `requests` library needs to be available, install it by running: `pip install requests`
- AutoHotKey, to reliably detect the keyboard shortcuts
- A Home Assistant instance & corresponding API key to access it

## Installation/Usage
- Double click on the AutoHotKey script to begin detecting for keystrokes (useful to configure it to start on boot as well)
- Bind your remote buttons in Flirc to the keystrokes listed above
- Duplicate `config.py.sample` to `config.py`
- Fill in the values
  - Home Assistant's URL (ex: http://localhost:8123)
  - Light entity name
  - Bearer Token value
