#bootstrap for project remoteCam on RPi3
import os,sys
import subprocess

if not os.geteuid() == 0:
    sys.exit("\nOnly root can run this script\n")


subprocess.call("sudo apt-get install autossh python-picamera pi-bluetooth subversion")
subprocess.call("sudo apt-get install python-zbar")

#wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.40.tar.xz
#tar xvf bluez-5.40.tar.xz
#cd bluez-5.40
#./configure --disable-systemd
#make


print("Ready.")