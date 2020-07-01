import BlynkLib
import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
throttle
# Initialize Blynk
blynk = BlynkLib.Blynk('dG2SwZBhNvt8dHp_miQq2UyQO4JxJK-o')

# Register Virtual Pins
@blynk.VIRTUAL_WRITE(throttle)
def my_write_handler(value):  
    v3 = value[0]
    os.system("pigs s 5 " + v3)
    print(value[0])
#@blynk.VIRTUAL_READ(2)
#   def my_read_handler():
#       # this widget will show some time in seconds..
#       blynk.virtual_write(2, int(time.time()))

#calibrate()
while True:
    blynk.run()  
