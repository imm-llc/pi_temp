import temp_monitor
import humidity_monitor
from app import app
from flask import jsonify
@app.route('/temp')
def temp():

    return jsonify({"temperature": temp_monitor.get_temp()})

@app.route('/humidity')
def humidity():
    
    return jsonify({"humidity": humidity_monitor.get_humidity()})