from smbus2 import SMBus
import time

Acc_rawX = Acc_rawY = Acc_rawZ = Gyr_rawX = Gyr_rawY = Gyr_rawZ = int()
Acceleration_angle = Gyro_angle = Total_angle = [0, 0]
elapsedTime = time = timePrev = float()
kp=3.55
ki=0.005
kd=2.05
throttle = 1000
desired_angle = 0.0
bus = SMBus(1)

# Write a byte to address 80, offset 0, data
time = time.time()*1000.0
os.system("pigs s 5" + " " + 1000)
os.system("pigs s 6" + " " + 1000)
time.sleep(7)

def pid():
    global time ,elapsedTime, timePrev
    timePrev = time
    time = time.time()*1000.0
    elapsedTime = (time - timePrev) / 1000



