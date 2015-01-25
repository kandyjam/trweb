## What is trweb

Trweb is a simple transmission speed control tool, is is configed at router and can easily watch the download speed and toggle transmission to "Alternate limits".

This is created for guests and they can quickly toggle download limit.


## How to use

1\. Modify server configs such as host/port in server.py, transmission's rpc username/password/port in speed.sh/toggle.sh

2\. Move speed.sh and toggle.sh to /root/bin/ or some place accessable(modify script path in control.py)

3\. Run python server.py and check if everything is OK, you may need supervisor  or screen for running in backgroud.

4\. Use your desktop/phone's browser access http://\<server ip\>:\<port\> to see if everything is ok. There are only a process bar with speed(div auto refrushed) and a switch button for limiting speed. :)

## Dependence

1\. On router, python and flask is required. For example, my devices is wndr4300 installed openwrt.

2\. Transmission configed "Alternate limits".

## Sugesstion

1\. Mount a usb swapfile, transmission use a lot of memory if you have hundreds of torrent.

## Screenshot

![Alt text](/../screenshots/sc1.jpg?raw=true "Limited download")
![Alt text](/../screenshots/sc2.jpg?raw=true "Unlimited download")

