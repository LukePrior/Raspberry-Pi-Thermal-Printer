#!/bin/sh
# installer.sh will install HOP-H58 drivers, python code & libraries

#Install Packages
PACKAGES="cups paps"
apt-get update
apt-get upgrade -y
apt-get install $PACKAGES -y

#Configure CUPS
usermod -a -G lpadmin pi

#Install python packages
pip3 install pyowm
pip3 install tweepy
pip3 install requests

#Install HOP-H58 Drivers
git clone https://github.com/OkkarMin/HOP-H58-RaspberryPi-Driver
cd HOP-H58-RaspberryPi-Driver
chmod +x ./install_H58_driver.sh
./install_H58_driver.sh

echo "Install complete, rebooting."
reboot
