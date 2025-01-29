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

You can mostly use pip to install all of it. I still need to do a better TODO xD 

* libbluetooth-dev
* libpython-dev
* python-sphinx
* gevent 
* Scapy 
* pycrypto
* pyshark 
* prettytable 
* sphinx_rtd_theme 

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
You'll get an error about not finding btaddr.h, so you have to go to (presumably you ran the command) _dists_ folder, and at the end of the _SOURCES.txt_ file add:

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


## Future Plans


### Full pairing support


As of now, BLESuite can only support LE Legacy JustWorks pairing. The Security Manager has mostly outlined, but the
remaining cryptographic programming for LESC and the alternate association models still need to be implemented.

### Signed write support

The ATT signed write operation is currently not supported by BLESuite. This is not a commonly used operation,
however in order to support security mode 2, it should be supported.

### Further support for private addresses

BLESuite currently only supports Public and Random (static) addresses. However, Random addresses can be of two
sub-types: Static or Private. A Random Private address can also be broken down into two sub-types not
supported currently by BLESuite: Non-resolvable Private address and Resolvable Private address (resolved using
IRK exchanged during pairing).

As such, functionality to set these types of addresses to the host adapter is not currently exposed by BLESuite.
Also, the ability to resolve Random resolvable addresses of a peer based on an exchanged IRK is not yet
implemented.

### Additional Tooling Built Using BLESuite

With the library built, the next step is to build security assessment tooling that utilizes this library.

Once such example that we have included with this library is `ble-replay`, which can take in a BLE packet
capture and replay the GATT traffic to a target device. `ble-replay` can quickly help
identify application layer security flaws related to replay attacks.

These sorts of tools decrease the time spent manually
analyzing packet captures and manually scripting BLE communication test cases.

### Removing Legacy Code

Since the code is fairly old, it was mostly with outdated functions and packaging. Refactoring to newer PEP's might be needed.
