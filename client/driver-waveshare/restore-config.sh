sudo sed -i '/dtparam=i2c_arm/d' config.txt 
sudo sed -i '/dtparam=spi/d' config.txt 
sudo sed -i '/enable_uart/d' config.txt 
echo 'dtparam=i2c_arm=on' >> config.txt 
echo 'dtparam=spi=on' >> config.txt
echo 'enable_uart=1' >> config.txt
sudo sed -i '/dtoverlay=waveshare/d' config.txt 
cat /boot/config.txt | grep dtoverlay=waveshare >> config.txt 

cp config.txt /boot/config.txt

sudo sed -i '/con2fbmap/d' /opt/retropie/configs/all/autostart.sh
sudo sed -i '1icon2fbmap 1 0' /opt/retropie/configs/all/autostart.sh
