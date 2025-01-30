# BLESuite README

## Overview


BLESuite is a python package to make Bluetooth Low Energy (BLE) device communication more user
friendly and enables rapid BLE device testing.
Version 2 of BLESuite removes the dependency on PyGattlib and BlueZ and instead uses a modified version
of PyBT (https://github.com/mikeryan/PyBT) to implement and manage our own BLE stack. This version increases
communication reliability, increases communication flexibility, improves device scanning, and enables device
fuzzing at the host layers of the Bluetooth stack.
The stack utilized by BLESuite intentionally allows malformed requests/responses to be sent to devices
in order to enable device testing.

Features:

* Includes 2 CLI tools to facilitate basic BLESuite operations: `blesuite` and `ble-replay`
* Support for the Central and Peripheral BLE roles
* Supports multiple HCI devices (such as a USB Bluetooth adapter)
* With a HCI device used for a central role, support for numerous simultaneous connections to peripherals (limited by the HCI controller's maximum number of connections)
* Scan for BLE devices
* Scan BLE devices for all GATT entities
* Quickly and easily send ATT requests to a peer peripheral device
* Construct and send carefully constructed (or intentionally malformed) L2CAP and ATT packets to a target devices
* Supports JustWorks LE Legacy pairing. Additional pairing methods will be available in a later version
* Quickly spin up a GATT server using an abstract object definition and numerous helper functions
* Support for GATT server import and export
* Support for Security Manager Long Term Key Database import and export
* Optionally, install a Python API-friendly version of BlueZ's BDADDR tool
(https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/tools/bdaddr.c) that enables a user to spoof the
BD_ADDR of their host's Bluetooth adapter (only supports some chipsets. This is a modified version of the
BlueZ's bdaddr.c)


**Note to the reader:**

In order to access Bluetooth Low Energy functionality, you must have access to a Bluetooth adapter that
supports it.


## Why BLESuite?


The goal of BLESuite is to provide a simplified method of quickly scripting communication with target
BLE devices for security assessments. Combined with the move from PyGattlib and BlueZ to PyBT, we now can
have more control over the BLE stack and use it to test various BLE stack layers of a target device.

Additionally, BLESuite is no longer restricted to just using the Central role. BLESuite now supports
the Peripheral role and allows users to quickly configure and stand-up a GATT server that can be used to test
Central role BLE devices (or dual role devices).

## Installation


The following are installation instruction for the BLESuite Python package.

### Prerequisites

**Supported Operating Systems:**

BLESuite was developed and tested against Ubuntu 24.04. The library may be supported
by other Linux distributions, however support is not currently guaranteed. 


**Required Software**

The following are requirements in order to use BLESuite:

You can mostly use pip to install all of it. 

* libbluetooth-dev
* libpython-dev
* gevent 
* Scapy 
* pycrypto
* pyshark 
* prettytable 

After installing libbluetooth-dev, libpython-dev, and python-sphinx, run the following to install the remaining Python dependencies:

```bash
pip install -r requirements.txt
```

### Documentation


From the docs folder, run:

```bash
make html
```

Then in docs/_build/html a full set of documentation and reference guides will be available.


### Installing Everything


Run the following command to install the python package:

```bash
python3 -m build
```
You'll get an error about not finding btaddr.h, so you have to go to (presumably you ran the command) _blesuite.egg-info_ folder, and at the end of the _SOURCES.txt_ file add:

```bash
tools/btaddr.h
tools/oui.h
```
Doing so, it is going to compile. Note that this is a temporary fix, I need to probably create a pyproject.toml instead of the outdated setup.py from Python 2.



If you do not want to install the BDADDR Python API or are having issues getting it to install,
comment out the following line in setup.py and re-run the command above:

```python
ext_modules = [c_ext],
```


## Future Plans (for now)


### Removing Legacy Code

Currently the main goal of this project is to remove legacy code and to run with newer versions of the dependencies.
