#!/usr/bin/python

import os
from subprocess import *
from time import *
from datetime import datetime

USER = 'MyName@RaspigamerCafe'
INTERVAL = 1
FONT1_SIZE = 14
FONT2_SIZE = 14

def run_cmd(cmd):
# runs whatever in the cmd variable
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

def get_ip_address(cmd, cmdeth):
    # ip & date information
    ipaddr = run_cmd(cmd)

    # selection of wlan or eth address
    count = len(ipaddr)
    if count == 0 :
        ipaddr = run_cmd(cmdeth)
    return ipaddr

def get_cpu_temp():
    tempFile = open("/sys/class/thermal/thermal_zone0/temp")
    cpu_temp = tempFile.read()
    tempFile.close()
    return "{0:.2f}".format(float(cpu_temp)/1000)

def main():

    #get ip address of eth0 connection
    cmdeth = "ip addr show eth0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1"
    #get ip address of wlan0 connection
    cmd = "ip addr show wlan0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1"

    delay = INTERVAL
    if FONT2_SIZE != 0:
        delay = delay - 1

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

        run_cmd("cp '/home/pi/RemoteMarquee/marquee/" + romfile + ".jpg' /tmp/result.jpg")

        if FONT1_SIZE > 0:
            date =  datetime.now().strftime( "%b %d %H:%M" )
            log1 =  USER + '    ' + date
            run_cmd("convert -background black -fill white -font FreeSans -pointsize " + str(FONT1_SIZE) + " label:'" + log1 + "' /tmp/log1.png")
            run_cmd("composite -gravity North /tmp/log1.png '/tmp/result.jpg' /tmp/result.jpg")
        if FONT2_SIZE > 0:
            ipaddr = get_ip_address(cmd, cmdeth)
            ipaddr = ipaddr.replace("\n","")
            lines = run_cmd('iostat -c 1 2').split('\n')
            words = lines[6].split()
            cpu_load = "{0:.2f}".format(100 - float(words[5]))
            log2 = 'IP: ' + ipaddr + '    CPU: ' + cpu_load + '%/' + get_cpu_temp() + u"\u2103"
            run_cmd("convert -background black -fill white -font FreeSans -pointsize " + str(FONT2_SIZE) + " label:'" + log2 + "' /tmp/log2.png")
            run_cmd("composite -gravity South /tmp/log2.png '/tmp/result.jpg' /tmp/result.jpg")
        
        run_cmd("cp /tmp/result.jpg /home/pi/RemoteMarquee/watching/result.jpg")
        if delay != 0:
            sleep(delay)

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
	
