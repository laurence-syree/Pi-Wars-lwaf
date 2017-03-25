#!/usr/bin/python
import sys
import time
from evdev import InputDevice, list_devices, categorize, ecodes, RelEvent

print("Press Ctrl-C to quit")
time.sleep(1)

found = False;
devices = [InputDevice(fn) for fn in list_devices()]
for dev in devices:
    if dev.name == 'Wireless Controller':
        found = True;
        print("Found")
        break
if not(found):
  print('Device not found. Aborting ...')
  exit()

try:
    for event in dev.read_loop():

        if event.type == ecodes.EV_ABS:
            if event.code in ecodes.ABS:
                symbol = ecodes.ABS[event.code]
                if symbol == "ABS_RY":
                    pass
                    #print(event.value)

                if symbol == "ABS_X":
                    print(event.value)

                if symbol == "ABS_RZ":
                    print(event.value)

                print(symbol)

        if event.type == ecodes.EV_KEY:

            #print(event.code)

            if event.code == 311:
                pass
                #print("right")

            if event.code == 310:
                print("left")

            if event.value == 1:
                print("keydown")
            if event.value == 0:
                pass
                #print("keyup")

except KeyboardInterrupt:
    sys.exit()
