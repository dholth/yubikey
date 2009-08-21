#!/usr/bin/env python
# Daniel Holth <dholth@fastmail.fm>, 2009
import sys
import k2u
import ctypes
from ctypes.util import find_library

# corresponds to the 16 keycodes produced for modhex:
yubikey_keycodes = [
        54, 56, 40, 26, 41, 42, 43, 31, 
        44, 45, 46, 57, 27, 28, 30, 55 ]

unicode_offset = 0x01000000

x11 = ctypes.cdll.LoadLibrary("libX11.so.6")
x11.XKeysymToString.restype = ctypes.c_char_p
x11.XKeycodeToKeysym.restype = ctypes.c_int32

def keycodesToKeysyms(layoutName=u""):
    """Return the unicode for the yubikey keycodes in the current keymap."""
    display = x11.XOpenDisplay(None)
    keysyms = list(x11.XKeycodeToKeysym(display, x, 0) 
            for x in yubikey_keycodes)
    chars = list((k2u.map.get(x, x) for x in keysyms))
    for i in range(len(chars)):
        if type(chars[i]) == int:
            try:
                chars[i] = unichr(chars[i] ^ unicode_offset)
            except Exception, e:
                error = u"%s '%s' %d:%s\n" % (unicode(e), layoutName, i, chars[i])
                sys.stderr.write(error)
                return None
    x11.XCloseDisplay(display)
    return u''.join(chars)

if __name__ == "__main__":
    alphabet = keycodesToKeysyms()
    if len(sys.argv) > 1:
        print sys.argv[1], ":", repr(alphabet)
    else:
        print repr(alphabet)
