# macropad_keycheck_boot.py
# disable CIRCUITPY drive by default, enable if Macropad bottom-right (KEY11) key is pressed
# Make this file "boot.py" and reset 
# 13 Oct 2021 - @todbot

import time
import board
import keypad
import storage

key_order = list(range(12))
key_pins = [getattr(board, "KEY%d" % (num + 1)) for num in key_order]
keys = keypad.Keys(key_pins, value_when_pressed=False, pull=True)

should_enable = False

for i in range(10):  # wait for 1 second total
    event = keys.events.get()
    if event and event.pressed and event.key_number == 11:  # bottom-right key on macropad
        should_enable = True
    time.sleep(0.1)

if should_enable:
    print("CIRCUITPY drive enabled")
else:
    print("CIRCUITPY drive disabled")
    storage.disable_usb_drive()  # disable CIRCUITPY