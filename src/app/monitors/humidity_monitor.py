import Adafruit_DHT

from flask import current_app as app


SENSOR_NUMBER = app.config['DHT_SENSOR']
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = app.config['DHT_PIN']

def get_humidity():

    try:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        
        if humidity is not None:
            print("Humidity reading is: %f" % humidity)
            return humidity
    except Exception as e:
        return str(e)
    
