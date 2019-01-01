#!/bin/sh

cd /home/pi/RemoteMarquee/mjpg-streamer/mjpg-streamer-experimental/
export LD_LIBRARY_PATH="$(pwd)" 
./mjpg_streamer -i "input_file.so -f /home/pi/RemoteMarquee/watching -d 0" -o "output_http.so -w www" &
