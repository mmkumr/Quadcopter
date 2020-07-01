#!/usr/bin/python
"""
Released under the MIT License
Copyright 2015 MrTijn/Tijndagamer
"""

# Import the MPU6050 class from the MPU6050.py file
from MPU6050 import MPU6050
import time

# Create a new instance of the MPU6050 class
sensor = MPU6050(0x68)
Total_angle = {
        "x" : 0,
        "y": 0,
        }
kp=3.55
ki=0.005
kd=2.05
throttle = 1500
desired_angle = 0.0
elapsedTime = timePrev = float()
timeNow = time.time()*1000.0

while True:

    timePrev = timeNow
    timeNow = time.time()*1000.0
    elapsedTime = (timeNow - timePrev) / 1000

    accel_data = sensor.get_accel_data()
    gyro_data = sensor.get_gyro_data()
    temp = sensor.get_temp()

    print("Accelerometer data")
    print("x: " + str(accel_data['x']))
    print("y: " + str(accel_data['y']))
    print("z: " + str(accel_data['z']))

    print("Gyroscope data")
    print("x: " + str(gyro_data['x']))
    print("y: " + str(gyro_data['y']))
    print("z: " + str(gyro_data['z']))

    print("Temp: " + str(temp) + " C") 

    Total_angle["x"] = 0.98 *(Total_angle["x"] + gyro_data['x']*elapsedTime) + 0.02*accel_data['x']
    Total_angle["y"] = 0.98 *(Total_angle["y"] + gyro_data['y']*elapsedTime) + 0.02*accel_data['y']
    print("Total Angle data")
    print("x: " + str(Total_angle["x"]))
    print("y: " + str(Total_angle["y"])) 
#    error = Total_angle[1] - desired_angle;
#    print("Error: " + str(error))
    

