How to use charles-proxy-helper
=============================================

This is a simple script intended to allow you to quickly update a PAC file for use with
http://www.charlesproxy.com/ on a mobile device.

**NOTE:** There is no need to remove the configuration from Dropbox or the mobile device when not is use because it fails gracefully if the proxy isn't available.

Usage
-----
1. Place the update_pac.py script in a Publicly accessible location (like on Dropbox) and run it. It will create/update proxy.pac
2. Get the public URL for the proxy.pac file. (Use Dropbox you can right click the file.)
3. For convenience I suggest creating a j.mp aka: bit.ly custom URL [like http://j.mp/rbro_pac](http://j.mp/rbro_pac)
4. Make sure the mobile device is on the same WiFi network as the computer
5. Anytime you start a new testing session, rerun the script incase your IP address has changed.

iOS Setup
---------
![iOS screenshot](http://i.imgur.com/MgtOEdO.png)

In Settings > Wifi, click tap the name your the network you want to modify, scroll to the bottom, and enter the shortened URL to your hosted PAC file

Android Setup
-------------
![Android screenshot 1](http://i.imgur.com/PHrMiTC.png)

Long tap on the name of the network you want to modify, and select "Modify network"

![Android screenshot 2](http://i.imgur.com/7GDgyVZ.png)

Enter the shortened URL to your hosted PAC file

