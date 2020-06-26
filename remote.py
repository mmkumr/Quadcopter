import BlynkLib
import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library

#######################################Starting of ESC section####################################################
ESC=5 #Connect the ESC in this GPIO pin 
pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0) 

max_value = 2000 #change this if your ESC's max value is different or leave it be
min_value = 1000  #change this if your ESC's min value is different or leave it be

def calibrate():   #This is the auto calibration procedure of a normal ESC
    pi.set_servo_pulsewidth(ESC, 0)
    time.sleep(3)
    #print("Disconnect the battery and press Enter")
    #inp = raw_input()
    #if inp == '':
    pi.set_servo_pulsewidth(ESC, min_value)
    print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
    inp = raw_input()
    if inp == '':            
        pi.set_servo_pulsewidth(ESC, min_value)
        print("Wierd eh! Special tone")
        time.sleep(7)
        print("Wait for it ....")
        time.sleep (5)
        print("Im working on it, DONT WORRY JUST WAIT.....")
        pi.set_servo_pulsewidth(ESC, 0)
        time.sleep(2)
        print("Arming ESC now...")
        pi.set_servo_pulsewidth(ESC, min_value)
        time.sleep(1)
        print("See.... uhhhhh")  

# Initialize Blynk
blynk = BlynkLib.Blynk('dG2SwZBhNvt8dHp_miQq2UyQO4JxJK-o')

# Register Virtual Pins
@blynk.VIRTUAL_WRITE(3)
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
