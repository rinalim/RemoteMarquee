## install.sh
# Install      :
# cd /home/pi
# git clone https://github.com/rinalim/RemoteMarquee.git
# cd RemoteMarquee
# chmod 755 install.sh
# sudo ./install.sh
#
# Reference    :
# https://github.com/ipromiseyou/RetroPie-AutoSet.git
# https://github.com/zzeromin/RetroPie-OLED.git

sudo sed -i '/rom_name/d' /opt/retropie/configs/all/runcommand-onstart.sh 
echo 'rom_name=$3' >> /opt/retropie/configs/all/runcommand-onstart.sh 
echo 'rom_name="${rom_name##*/}"' >> /opt/retropie/configs/all/runcommand-onstart.sh 
echo 'rom_name="${rom_name%.*}"' >> /opt/retropie/configs/all/runcommand-onstart.sh 
echo 'echo "$1 $rom_name" > /tmp/remotemarquee.log' >> /opt/retropie/configs/all/runcommand-onstart.sh

sudo sed -i '/remotemarquee/d' /opt/retropie/configs/all/runcommand-onend.sh
echo 'echo "maintitle" > /tmp/remotemarquee.log' >> /opt/retropie/configs/all/runcommand-onend.sh

sudo sed -i '/RemoteMarquee/d' /opt/retropie/configs/all/autostart.sh 
sed -i '1i\\/bin/sh /home/pi/RemoteMarquee/stream.sh' /opt/retropie/configs/all/autostart.sh
sed -i '1i\\/usr/bin/python /home/pi/RemoteMarquee/RemoteMarquee.py &' /opt/retropie/configs/all/autostart.sh

apt-get install -y imagemagick sysstat libjpeg8-dev

cd /home/pi/RemoteMarquee/
mkdir watching
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental
make
make install

chgrp -R -v pi /home/pi/RemoteMarquee
chown -R -v pi /home/pi/RemoteMarquee

echo "Setup Completed. Reboot after 3 Seconds."
sleep 3
reboot
