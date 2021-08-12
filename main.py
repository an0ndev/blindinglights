import pathlib

from blindinglights.blindinglights import do_light_show

import sys

if len (sys.argv) < 2:
    print (f"Usage: {sys.argv [0]} <path to sound file>")
    sys.exit (1)

do_light_show (pathlib.Path (sys.argv [1]))