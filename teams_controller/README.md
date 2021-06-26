Purpose
-------

The primary purpose of this is to really just get to know both circuit python as well as the BYO keyboard and see what works for me.

To make it practical, there was a need for a teams remote controller. It's what we've been having to deal with over the past months and with all sorts of extra noises and just jumping from one screen to another, it's been a messy experience. This little keyboard will hopefully make it all a little less messy by providing a few simple remote control features.

Installation
------------

As a user of both Qwerty and a Dvorak layout, keycodes move around a bit and the keyboard_layout_us_dvo has been copied from the adafruit_hid project site: https://github.com/adafruit/Adafruit_CircuitPython_HID
Installation of the keyboard_layout_us_dvo.py file is to copy it to the lib/adafruit_hid directory.
The work.py has to be copied to the main filesystem and it should be running!

Usage
-----

Designed for a 6 button keyboard, 2 rows of 3 buttons.
The left two buttons are mode-switching buttons bottom is Mod1, top is Mod2. For safety, we don't want to accidentally enter a password, so we have to press Mod1 and then Mod2 in that order. The second and third column represent a password each, the top row in the Dvorak layout, the bottom row in the Qwerty layout.

The without any of the modifers, the keys are as follows:
 * Top-Middle: control-shift-m, toggle mute self in teams,
 * Bottom-Middle: mute speakers,
 * Top-Right: control-shift-o, toggle video in teams,
 * Bottom-Right: control-shift-k, toggle raise-hand in teams.

There's a special Mod2 then Top-Middle to only be un-muted while the button is pressed. This is always handy for meetings where there's mostly listening and only limited input expected. Or when the kids/construction workers are especially noisy.
