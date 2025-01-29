# -*- coding: utf-8 -*-


"""setup.py: distutils.core setup control."""

#import re
from setuptools import setup, Extension


#with open("README.md", "rb") as f:
 #  long_descr = f.read().decode("utf-8")

#grab version from blesuite/blesuite.py
#version = re.search(
 #   '^__version__\s*=\s*"(.*)"',
  #  open('blesuite/__init__.py').read(),
   # re.M
    #).group(1)
#useless there ain't no other versions lol
version = 1

c_ext = Extension("bdaddr", include_dirs=["tools/"], sources=["tools/bdaddr.c", "tools/oui.c"], libraries=["bluetooth"])

setup(
    name = "blesuite",

    packages = ['blesuite', 'blesuite.entities', 'blesuite.utils', 
                'blesuite.cli', 'blesuite.pybt', 'blesuite.replay',
                'blesuite.replay.btsnoop', 'blesuite.replay.btsnoop.btsnoop', 
                'blesuite.replay.btsnoop.android','blesuite.replay.btsnoop.bt'],
    ext_modules = [c_ext],
    scripts = ["bin/blesuite", "bin/ble-replay"],
    version = version,
    description = "A Python 2 library converted to Python 3 for communicating with and testing Bluetooth LE devices.",
    authors = "Taylor Trabun, Marlon Lüdtke",
    author_email = "taylor.trabun@nccgroup.trust",
    )