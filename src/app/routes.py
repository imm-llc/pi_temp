from monitors import temp_monitor
from monitors import humidity_monitor
from app import app
from flask import jsonify
@app.route('/temp')
def temp():

    return jsonify({"temperature": temp_monitor.get_temp()})

@app.route('/humidity')
def humidity():
    
    return jsonify({"humidityss": humidity_monitor.get_humidity()})