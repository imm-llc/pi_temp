import Adafruit_DHT

from flask import current_app as app


SENSOR_NUMBER = app.config['DHT_SENSOR']
DHT_SENSOR = Adafruit_DHT.SENSOR_NUMBER
DHT_PIN = app.config['DHT_PIN']


humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

def get_humidity():
    if humidity is not None:
        return humidity
