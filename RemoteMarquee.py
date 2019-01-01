#!/usr/bin/python

import os
from subprocess import *
from time import *

FONT_SIZE = 10

def run_cmd(cmd):
# runs whatever in the cmd variable
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output


def get_cpu_temp():
    tempFile = open("/sys/class/thermal/thermal_zone0/temp")
    cpu_temp = tempFile.read()
    tempFile.close()
    return "{0:.2f}".format(float(cpu_temp)/1000)


def main():
    run_cmd('echo "maintitle" > /tmp/remotemarquee.log')
    while True:
        romfile = "maintitle"
        try:
            f = open('/tmp/remotemarquee.log', 'r')
            # except FileNotFoundError:
        except IOError:
		print "IOError"
        else:
            line = f.readline()
            words = line.split()
            f.close()
            if words[0] == "maintitle":
                romfile = "maintitle"
            else:
                system = words[0]
                romfile = words[1]
                if os.path.isfile("/home/pi/RemoteMarquee/marquee/" + romfile  + ".jpg") == False:
                    png_path1 = "/home/pi/RetroPie/roms/arcade/marquee/" + romfile  + ".png"
                    png_path2 = "/home/pi/RetroPie/roms/" + system + "/marquee/" + romfile  + ".png"
                    if os.path.isfile(png_path1) == True:
                        run_cmd("convert -resize 400x225 -quality 100 '" + png_path1 + "' '/tmp/" + romfile + ".png'")
                        run_cmd("composite -gravity center '/tmp/" + romfile + ".png' /home/pi/RemoteMarquee/background.jpg '/home/pi/RemoteMarquee/marquee/" + romfile + ".jpg'")
                    elif os.path.isfile(png_path2) == True:
                        run_cmd("convert -resize 400x225 -quality 100 '" + png_path2 + "' '/tmp/" + romfile + ".png'")
                        run_cmd("composite -gravity center '/tmp/" + romfile + ".png' /home/pi/RemoteMarquee/background.jpg '/home/pi/RemoteMarquee/marquee/" + romfile + ".jpg'")
                    else:
                        romfile = "maintitle"

        if FONT_SIZE == 0:
            run_cmd("cp '/home/pi/RemoteMarquee/marquee/" + romfile + ".jpg' /home/pi/RemoteMarquee/watching/result.jpg")
            sleep(1)
        else:
            lines = run_cmd('iostat -c 1 2').split('\n')
            words = lines[6].split()
            cpu_load = "{0:.2f}".format(100 - float(words[5]))
            log = 'CPU load = ' + cpu_load + ' Temperature = ' + get_cpu_temp() + ' '
            run_cmd("convert -background black -fill white -pointsize " + str(FONT_SIZE) + " label:'" + log + "' /tmp/log.png")
            run_cmd("composite -gravity Southeast /tmp/log.png '/home/pi/RemoteMarquee/marquee/" + romfile + ".jpg' /home/pi/RemoteMarquee/watching/result.jpg")
            #sleep(0)

if __name__ == "__main__":
    import sys

    try:
        main()

    # Catch all other non-exit errors
    except Exception as e:
        sys.stderr.write("Unexpected exception: %s" % e)
        sys.exit(1)

    # Catch the remaining exit errors
    except:
        sys.exit(0)

