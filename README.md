# pi_temp

## Overview

A very, very simple Flask API to pull temperature and humidity readings from a DHT22 on a Raspberry Pi.

There are two API endpoints:

`/temp` returns the temperature reading in Fahrenheit (PR welcome to fix spelling).

`/humidity` returns the percentage of humidity. 

If they receive a reading that is not None, both endpoints will return the following JSON: `{"humidity": <humidity>, "error": "no"}` and ``{"temperature": <temperature>, "error": "no"}`

If an endpoint receives a reading of None, you'll receive the following JSON: `{"humidity": None, "error": "yes"}` and `{"temperature": None, "error": "yes"}`

If an exception is raised while checking, an additional K/V pair will be added to the JSON: `"err_string": "str(e)"` where `str(e)` is the string of the raised exception.

We're pulling this into Zabbix and using dependent items to check the JSON itself.

## Limitations

Only works with an ADAFruit DHT22. You could modify `src/app/monitors/humidity_monitor.py` and `src/app/monitors/humidity_monitor.py` to use e.g. DHT11

Runs as root for out-of-the-box access to DHT

No logging

## Configuration

The RPM installs the app config to `/etc/sysconfig/pi-temp`. You can modify the GPIO PIN (`DHT_PIN`) and the temperature offset (`TEMO_OFFSET`)

The systemd service is installed at `/usr/lib/systemd/system/pi-temp.service`.

## Extending

It should be fairly easy to poll additional sensors. For simplicity's sake, I would add additional modules in `src/app/monitors/` and give them each a route off of `/temp` (e.g. `/temp/serverroom`, `/temp/breakroom`)