sudo apt-get install -y mplayer

sudo sed -i '/spi-run/d' /opt/retropie/configs/all/autostart.sh 
sudo sed -i '1i\\/usr/bin/python /home/pi/RemoteMarquee/client/spi-run.py &' /opt/retropie/configs/all/autostart.sh

echo "Reboot after 3 Seconds."
sleep 3
reboot
