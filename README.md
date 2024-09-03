# ArcGIS_Map_Copy
**Please note: This project has only been tested on Debian 12 and Windows 11.**
## Prerequisites
Before you begin, ensure you have met the following requirements:
* If you are on **Windows 11** machine, make sure the following packages are installed:
    * `python` version ranging from 3.9.x to 3.11.x
    * [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170) installed for `ujson` library
* If you are on **Debian 12** or similar distros, make sure the following packages are installed:
    * `python3` version ranging from 3.9.x to 3.11.x
    * `python3-pip`
    * `libkrb5-dev`
    * You can install them using the following command:
   ```bash
   sudo apt-get install python3 python3-pip libkrb5-dev
   ```

## Setup

**To setup without using git**
* Download the source code as `.zip` file
* Then unzip the file and go inside the folder
* Finally, open the terminal and do `pip install -r requirements.txt`

<br>

**To setup with git, open the terminal and perform the following the commands:**

```bash
git clone https://github.com/KPCOFGS/ARC_GIS_Map_Copy.git
cd ARC_GIS_Map_Copy
pip install -r requirements.txt
```

## Usage
[Instructions on how to use the script](usage/usage.md)

**Note:** After successfully cloning one map to another. Make sure to go to ArcGIS Online > Content > My Organization, find the cloned map and edit it. Then, do nothing but save it using "Save As", This ensures the map is successfully cloned with the right ownership and permissions

## Acknowledgement

We would like to thank the following projects for their great work:

   * This work is built upon the [ArcGIS API for Python](https://developers.arcgis.com/python/)

## License
This project is licensed under the Unlicense

See the [LICENSE](LICENSE) file for details.
