dd if=/dev/zero of=/dev/fb1
mplayer -vo fbdev2:/dev/fb1 -zoom -xy 480 -demuxer lavf -framedrop http://127.0.0.1:8080/?action=stream </dev/null >/dev/null 2>&1
