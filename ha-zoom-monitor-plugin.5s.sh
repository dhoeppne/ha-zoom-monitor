#!/bin/bash

# <bitbar.title>Zoom Meeting Status</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>fanuch</bitbar.author>
# <bitbar.author.github>fanuch</bitbar.author.github>
# <bitbar.desc>Simply run a Python script to detect an active meeting</bitbar.desc>

pythonenv="/Users/dhoeppner/dev/me/ha-zoom-monitor"
script="main.py"

$pythonenv/venv/bin/python $pythonenv/$script