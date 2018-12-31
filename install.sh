## install.sh
# Install      :
# cd /home/pi
# git clone https://github.com/rinalim/RemoteMarquee.git
# cd /home/pi/RemoteMarquee/
# chmod 755 install.sh
# sudo ./install.sh
#
# Reference    :
# https://github.com/ipromiseyou/RetroPie-AutoSet.git
# https://github.com/zzeromin/RetroPie-OLED.git

cd /home/pi/RemoteMarquee/
cp runcommand-onstart.sh /opt/retropie/configs/all/
cp runcommand-onend.sh /opt/retropie/configs/all/
#sed -i '1i\\/usr/bin/python /home/pi/RemoteMarquee/RemoteMarquee.py &' /opt/retropie/configs/all/autostart.sh
apt-get install -y imagemagick sysstat libjpeg8-dev
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental
make
make install
chgrp -R -v pi /home/pi/RemoteMarquee
chown -R -v pi /home/pi/RemoteMarquee
chgrp -R -v pi /opt/retropie/configs/all
chown -R -v pi /opt/retropie/configs/all
echo "Setup Completed. Reboot after 3 Seconds."
sleep 3
reboot
