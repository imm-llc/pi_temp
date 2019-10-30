# pi_temp

## Overview

A very, very simple Flask API to pull temperature and humidity readings from a DHT22 on a Raspberry Pi.

## Limitations

Only works with an ADAFruit DHT22. You could modify `src/app/monitors/humidity_monitor.py` and `src/app/monitors/humidity_monitor.py` to use e.g. DHT11

Runs as root for out-of-the-box access to DHT

No logging

## Configuration

The RPM installs the app config to `/etc/sysconfig/pi-temp`. You can modify the GPIO PIN (`DHT_PIN`) and the temperature offset (`TEMO_OFFSET`)

The systemd service is installed at `/usr/lib/systemd/system/pi-temp.service`.