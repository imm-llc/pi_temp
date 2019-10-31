import Adafruit_DHT

from flask import current_app as app

SENSOR_NUMBER = app.config['DHT_SENSOR']
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = app.config['DHT_PIN']

def get_temp():

    try:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        
        if temperature is not None:
            farenheight = 9.0/5.0 * temperature + 32 + app.config['TEMP_OFFSET']
            print("Temperature reading is: %f" % farenheight)
            return farenheight
    except Exception as e:
        return str(e)
