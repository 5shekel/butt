#!/usr/bin/python
from flask import Flask
from flask import request
from subprocess import Popen,PIPE
app = Flask(__name__)
from functools import wraps
from flask import request, Response

import time, sys, signal, atexit
import pyupm_mpu9150 as sensorObj

# Instantiate an MPU60X0 on I2C bus 0
sensor = sensorObj.MPU60X0()

## Exit handlers ##
# This function stops python from printing a stacktrace when you hit control-C
def SIGINTHandler(signum, frame):
        raise SystemExit

# This function lets you run code on exit
def exitHandler():
        print "Exiting"
        sys.exit(0)

# Register exit handlers
atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)

sensor.init()

x = sensorObj.new_floatp()
y = sensorObj.new_floatp()
z = sensorObj.new_floatp()
    
    
def get_sernsor_data():
        sensor.update()
        sensor.getAccelerometer(x, y, z)
        """
        print "Accelerometer: AX: ", sensorObj.floatp_value(x), 
        print " AY: ", sensorObj.floatp_value(y),
        print " AZ: ", sensorObj.floatp_value(z)

        sensor.getGyroscope(x, y, z)
        print "Gyroscope:     GX: ", sensorObj.floatp_value(x), 
        print " GY: ", sensorObj.floatp_value(y),
        print " GZ: ", sensorObj.floatp_value(z)

        print "Temperature:  ", sensor.getTemperature()
        print

        #time.sleep(.5)
        """
        return sensorObj.floatp_value(x), sensorObj.floatp_value(y), sensorObj.floatp_value(z)


@app.route("/",methods=['GET', 'POST'])
def switch():
    data = get_sernsor_data()
    return str(data[0]) + " " + str(data[1]) + " " + str(data[2])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

