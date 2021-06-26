from adafruit_hid.keycode import Keycode

class KeyboardLayoutUSDVO:
    """Map ASCII characters to appropriate keypresses on a standard US PC keyboard.
    Non-ASCII characters and most control characters will raise an exception.
    """

    # The ASCII_TO_KEYCODE bytes object is used as a table to maps ASCII 0-127
    # to the corresponding # keycode on a US 104-key keyboard.
    # The user should not normally need to use this table,
    # but it is not marked as private.
    #
    # Because the table only goes to 127, we use the top bit of each byte (ox80) to indicate
    # that the shift key should be pressed. So any values 0x{8,9,a,b}* are shifted characters.
    #
    # The Python compiler will concatenate all these bytes literals into a single bytes object.
    # Micropython/CircuitPython will store the resulting bytes constant in flash memory
    # if it's in a .mpy file, so it doesn't use up valuable RAM.
    #
    # \x00 entries have no keyboard key and so won't be sent.
    SHIFT_FLAG = 0x80
    ASCII_TO_KEYCODE = (
        b"\x00"  # NUL
        b"\x00"  # SOH
        b"\x00"  # STX
        b"\x00"  # ETX
        b"\x00"  # EOT
        b"\x00"  # ENQ
        b"\x00"  # ACK
        b"\x00"  # BEL \a
        b"\x2a"  # BS BACKSPACE \b (called DELETE in the usb.org document)
        b"\x2b"  # TAB \t
        b"\x28"  # LF \n (called Return or ENTER in the usb.org document)
        b"\x00"  # VT \v
        b"\x00"  # FF \f
        b"\x00"  # CR \r
        b"\x00"  # SO
        b"\x00"  # SI
        b"\x00"  # DLE
        b"\x00"  # DC1
        b"\x00"  # DC2
        b"\x00"  # DC3
        b"\x00"  # DC4
        b"\x00"  # NAK
        b"\x00"  # SYN
        b"\x00"  # ETB
        b"\x00"  # CAN
        b"\x00"  # EM
        b"\x00"  # SUB
        b"\x29"  # ESC
        b"\x00"  # FS
        b"\x00"  # GS
        b"\x00"  # RS
        b"\x00"  # US
        b"\x2c"  # SPACE
        b"\x9e"  # ! x1e|SHIFT_FLAG (shift 1)
        b"\x94"  # Q" x14|SHIFT_FLAG
        b"\xa0"  # # x20|SHIFT_FLAG (shift 3)
        b"\xa1"  # $ x21|SHIFT_FLAG (shift 4)
        b"\xa2"  # % x22|SHIFT_FLAG (shift 5)
        b"\xa4"  # & x24|SHIFT_FLAG (shift 7)
        b"\x14"  # q'
        b"\xa6"  # ( x26|SHIFT_FLAG (shift 9)
        b"\xa7"  # ) x27|SHIFT_FLAG (shift 0)
        b"\xa5"  # * x25|SHIFT_FLAG (shift 8)
        b"\xb0"  # }+ x30|SHIFT_FLAG (shift ])
        b"\x1a"  # w,
        b"\x34"  # '-
        b"\x08"  # e.
        b"\x2f"  # [/
        b"\x27"  # 0
        b"\x1e"  # 1
        b"\x1f"  # 2
        b"\x20"  # 3
        b"\x21"  # 4
        b"\x22"  # 5
        b"\x23"  # 6
        b"\x24"  # 7
        b"\x25"  # 8
        b"\x26"  # 9
        b"\x9d"  # Z: x1d|SHIFT_FLAG
        b"\x1d"  # z;
        b"\x9a"  # W< x1a|SHIFT_FLAG
        b"\x30"  # ]=
        b"\x88"  # E> x08|SHIFT_FLAG
        b"\xaf"  # {? x2f|SHIFT_FLAG (shift [)
        b"\x9f"  # @ x1f|SHIFT_FLAG (shift 2)
        b"\x84"  # AA x04|SHIFT_FLAG (shift a)
        b"\x91"  # NB x11|SHIFT_FLAG
        b"\x8c"  # IC x0c|SHIFT_FLAG
        b"\x8b"  # HD x0b|SHIFT_FLAG
        b"\x87"  # DE x07|SHIFT_FLAG
        b"\x9c"  # YF x1c|SHIFT_FLAG
        b"\x98"  # UG x18|SHIFT_FLAG
        b"\x8d"  # JH x0d|SHIFT_FLAG
        b"\x8a"  # GI x0a|SHIFT_FLAG
        b"\x86"  # CJ x06|SHIFT_FLAG
        b"\x99"  # VK x19|SHIFT_FLAG
        b"\x93"  # PL x13|SHIFT_FLAG
        b"\x90"  # MM x10|SHIFT_FLAG
        b"\x8f"  # LN x0f|SHIFT_FLAG
        b"\x96"  # SO x16|SHIFT_FLAG
        b"\x95"  # RP x15|SHIFT_FLAG
        b"\x92"  # OR x12|SHIFT_FLAG
        b"\x9b"  # XQ x1b|SHIFT_FLAG
        b"\xb3"  # :S x33|SHIFT_FLAG (shift ;)
        b"\x8e"  # KT x0e|SHIFT_FLAG
        b"\x89"  # FU x09|SHIFT_FLAG
        b"\xb7"  # >V x37|SHIFT_FLAG (shift .)
        b"\xb6"  # <W x36|SHIFT_FLAG (shift ,)
        b"\x85"  # BX x05|SHIFT_FLAG (etc.)
        b"\x97"  # TY x17|SHIFT_FLAG
        b"\xb8"  # ?Z x38|SHIFT_FLAG (shift /)
        b"\x2d"  # -[
        b"\x31"  # \ backslash
        b"\x2e"  # =]
        b"\xa3"  # ^ x23|SHIFT_FLAG (shift 6)
        b"\xb4"  # "_ x34|SHIFT_FLAG (shift ')
        b"\x35"  # `
        b"\x04"  # aa
        b"\x11"  # nb
        b"\x0c"  # ic
        b"\x0b"  # hd
        b"\x07"  # de
        b"\x1c"  # yf
        b"\x18"  # ug
        b"\x0d"  # jh
        b"\x0a"  # gi
        b"\x06"  # cj
        b"\x19"  # vk
        b"\x13"  # pl
        b"\x10"  # mm
        b"\x0f"  # ln
        b"\x16"  # so
        b"\x15"  # rp
        b"\x1b"  # xq
        b"\x12"  # or
        b"\x33"  # ;s
        b"\x0e"  # kt
        b"\x09"  # fu
        b"\x37"  # .v
        b"\x36"  # ,w
        b"\x05"  # bx
        b"\x17"  # ty
        b"\x38"  # /z
        b"\xad"  # _{ x2d|SHIFT_FLAG (shift -)
        b"\xb1"  # | x31|SHIFT_FLAG (shift \)
        b"\xae"  # +} x2e|SHIFT_FLAG (shift =)
        b"\xb5"  # ~ x35|SHIFT_FLAG (shift `)
        b"\x4c"  # DEL DELETE (called Forward Delete in usb.org document)
    )

    def __init__(self, keyboard):
        """Specify the layout for the given keyboard.
        :param keyboard: a Keyboard object. Write characters to this keyboard when requested.
        Example::
            kbd = Keyboard(usb_hid.devices)
            layout = KeyboardLayoutUS(kbd)
        """

        self.keyboard = keyboard

    def write(self, string):
        """Type the string by pressing and releasing keys on my keyboard.
        :param string: A string of ASCII characters.
        :raises ValueError: if any of the characters are not ASCII or have no keycode
            (such as some control characters).
        Example::
            # Write abc followed by Enter to the keyboard
            layout.write('abc\\n')
        """
        for char in string:
            keycode = self._char_to_keycode(char)
            # If this is a shifted char, clear the SHIFT flag and press the SHIFT key.
            if keycode & self.SHIFT_FLAG:
                keycode &= ~self.SHIFT_FLAG
                self.keyboard.press(Keycode.SHIFT)
            self.keyboard.press(keycode)
            self.keyboard.release_all()

    def keycodes(self, char):
        """Return a tuple of keycodes needed to type the given character.
        :param char: A single ASCII character in a string.
        :type char: str of length one.
        :returns: tuple of Keycode keycodes.
        :raises ValueError: if ``char`` is not ASCII or there is no keycode for it.
        Examples::
            # Returns (Keycode.TAB,)
            keycodes('\t')
            # Returns (Keycode.A,)
            keycode('a')
            # Returns (Keycode.SHIFT, Keycode.A)
            keycode('A')
            # Raises ValueError because it's a accented e and is not ASCII
            keycode('é')
        """
        keycode = self._char_to_keycode(char)
        if keycode & self.SHIFT_FLAG:
            return (Keycode.SHIFT, keycode & ~self.SHIFT_FLAG)

        return (keycode,)

    def _char_to_keycode(self, char):
        """Return the HID keycode for the given ASCII character, with the SHIFT_FLAG possibly set.
        If the character requires pressing the Shift key, the SHIFT_FLAG bit is set.
        You must clear this bit before passing the keycode in a USB report.
        """
        char_val = ord(char)
        if char_val > 128:
            raise ValueError("Not an ASCII character.")
        keycode = self.ASCII_TO_KEYCODE[char_val]
        if keycode == 0:
            raise ValueError("No keycode available for character.")
        return keycode