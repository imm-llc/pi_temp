from app import app
from app.monitors import temp_monitor, humidity_monitor
from flask import jsonify

@app.route('/temp')
def temp():

    return jsonify(temp_monitor.get_temp())

@app.route('/humidity')
def humidity():
    
    return jsonify(humidity_monitor.get_humidity())