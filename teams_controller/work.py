import time
import board
import digitalio
import adafruit_matrixkeypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keyboard_layout_us_dvo import KeyboardLayoutUSDVO
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
control_key = Keycode.SHIFT
cc = ConsumerControl(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)
kbd_us = KeyboardLayoutUS(keyboard)
kbd_dv = KeyboardLayoutUSDVO(keyboard)

MOD_1 = 3
MOD_2 = 0
KEY_1 = 1
KEY_2 = 2
KEY_3 = 4
KEY_4 = 5

PASSWORD_1="Testing"
PASSWORD_2="Oldtest"

# Actions
def sendpwd(key):
    if key == KEY_1:
        kbd_us.write(PASSWORD_1)
    elif key == KEY_2:
        kbd_us.write(PASSWORD_2)
    elif key == KEY_3:
        kbd_dv.write(PASSWORD_1)
    elif key == KEY_4:
        kbd_dv.write(PASSWORD_2)

# Uncomment the following code for 6 Key (V2.5)
cols = [digitalio.DigitalInOut(x) for x in (board.D11, board.D12, board.D13)]
rows = [digitalio.DigitalInOut(x) for x in (board.D9, board.D10)]
keys = (
    (MOD_2, KEY_1, KEY_2),
    (MOD_1, KEY_3, KEY_4),
)
key_amount = 6

KEY_UP_EVENT = "up"
KEY_DOWN_EVENT = "down"

STATE_NOMOD = "nomod"
STATE_MOD1 = "mod1"
STATE_MOD2 = "mod2"
STATE_MOD21 = "mod21"
STATE_MOD12 = "mod12"

# Uncomment the following code for 9 Key (V2.6)
# cols = [digitalio.DigitalInOut(x) for x in (board.D11, board.D12, board.D13)]
# rows = [digitalio.DigitalInOut(x) for x in (board.D7, board.D9, board.D10)]
# keys = (
#     (6,7,8),
#     (3,4,5),
#     (0,1,2),
# )

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

ison = []

def sendtmpon_dv(key, ev):
    print("Sending: " + str(key))
    if key == KEY_1:
        # Mute self on/off
        keyboard.press(Keycode.CONTROL, Keycode.SHIFT, kbd_dv.keycodes('m')[0])
        time.sleep(0.1)
        keyboard.release_all()
        if ev == KEY_DOWN_EVENT:
            ison.append(key)
        elif ev == KEY_UP_EVENT and key in ison:
            ison.remove(key)


def sendtogl_dv(key):
    print("Sending: " + str(key))
    if key == KEY_1:
        # Mute self on/off
        keyboard.press(Keycode.CONTROL, Keycode.SHIFT, kbd_dv.keycodes('m')[0])
        time.sleep(0.1)
        keyboard.release_all()
    elif key == KEY_2:
        # Camera on/off
        keyboard.press(Keycode.CONTROL, Keycode.SHIFT, kbd_dv.keycodes('o')[0])
        time.sleep(0.1)
        keyboard.release_all()
    elif key == KEY_3:
        # Mute all
        cc.send(ConsumerControlCode.MUTE)
    elif key == KEY_4:
        # Raise hand
        keyboard.press(Keycode.CONTROL, Keycode.SHIFT, kbd_dv.keycodes('k')[0])
        time.sleep(0.1)
        keyboard.release_all()

def sendtogl_us(key):
    print("Sending: " + str(key))
    if key == KEY_1:
        # Mute self on/off
        keyboard.press(Keycode.CONTROL, Keycode.SHIFT, kbd_us.keycodes('m')[0])
        time.sleep(0.1)
        keyboard.release_all()
    elif key == KEY_2:
        # Camera on/off
        keyboard.press(Keycode.CONTROL, Keycode.SHIFT, kbd_us.keycodes('o')[0])
        time.sleep(0.1)
        keyboard.release_all()
    elif key == KEY_3:
        # Mute all
        cc.send(ConsumerControlCode.MUTE)
    elif key == KEY_4:
        # Raise hand
        keyboard.press(Keycode.CONTROL, Keycode.SHIFT, kbd_us.keycodes('k')[0])
        time.sleep(0.1)
        keyboard.release_all()

def empty_state():
    result = []
    for i in range(key_amount):
        result.append(False)
    return result

def scankbd(keys):
    result = empty_state()
    if keys:
        for key in keys:
            result[key] = True
    return result

def scanevents(currstate, prevstate):
    result = []
    for i in range(key_amount):
        if currstate[i] and not prevstate[i]:
            result.append((i, KEY_DOWN_EVENT))
        elif not currstate[i] and prevstate[i]:
            result.append((i, KEY_UP_EVENT))
    return result

previous = empty_state()
state = STATE_NOMOD

while True:
    keys = keypad.pressed_keys
    kstate = scankbd(keys)
    events = scanevents(kstate, previous)
    for (key, ev) in events:
        if key == MOD_1:
            if ev == KEY_UP_EVENT:
                if state == STATE_MOD1:
                    state = STATE_NOMOD
                if state == STATE_MOD12 or state == STATE_MOD21:
                    state = STATE_MOD2
            elif ev == KEY_DOWN_EVENT:
                if state == STATE_NOMOD:
                    state = STATE_MOD1
                elif state == STATE_MOD2:
                    state = STATE_MOD21
        elif key == MOD_2:
            if ev == KEY_UP_EVENT:
                if state == STATE_MOD2:
                    state = STATE_NOMOD
                if state == STATE_MOD12 or state == STATE_MOD21:
                    state = STATE_MOD1
            elif ev == KEY_DOWN_EVENT:
                if state == STATE_NOMOD:
                    state = STATE_MOD2
                elif state == STATE_MOD1:
                    state = STATE_MOD12
        else:
            if state == STATE_MOD12 and ev == KEY_UP_EVENT:
                sendpwd(key)
            elif state == STATE_NOMOD and ev == KEY_DOWN_EVENT:
                sendtogl_dv(key)
            elif state == STATE_MOD2:
                sendtmpon_dv(key, ev)
            #elif state == STATE_MOD2 and ev == KEY_DOWN_EVENT:
            #    sendtogl_us(key)
            if state != STATE_MOD2 and ison:
                for k in ison:
                    sendtmpon_dv(k, KEY_UP_EVENT)
    previous = kstate
    time.sleep(0.025)
