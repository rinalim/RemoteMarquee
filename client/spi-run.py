#!/usr/bin/python

import os
from subprocess import *

def run_cmd(cmd):
# runs whatever in the cmd variable
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
return output

run_cmd("dd if=/dev/zero of=/dev/fb1")
run_cmd("mplayer -vo fbdev2:/dev/fb1 -zoom -xy 480 -demuxer lavf -framedrop http://127.0.0.1:8080/?action=stream </dev/null >/dev/null 2>&1")
