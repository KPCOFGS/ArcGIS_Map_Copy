# ARCGIS_Map_Copy

**Please note: This project has only been tested on Linux Mint 21.3 and Windows 11.**

## Prerequisites

Before you begin, ensure you have met the following requirements:
* On **Linux 21.3** or similar distros, make sure the following packages are installed:
    * `python3`
    * `python3-pip`
    * `libkrb5-dev`
You can install them using the following command:
```bash
sudo apt-get install python3 python3-pip libkrb5-dev
```
Then, install the required Python package
```bash
python3 -m pip install arcgis
```
\
You can get the script by ```git clone https://github.com/KPCOFGS/ARC_GIS_Map_Copy.git```
\
\
\
In the script, replace  ```SOURCE_ACCOUNT``` and ```SOURCE_PASSWORD``` to your source account and password\
Do the same for the ```DESTINATION_ACCOUNT``` and ```DESTINATION_PASSWORD``` as well.
\
\
\
To get the map ID, first log into your account. Find and click ```Content``` tab. Then click on the map you want to copy, and then click ```view details```.\
On the right hand side, under ```Details``` section, There is the ```ID```. If you do not see ```Details``` section, you may want to scroll down a bit.
