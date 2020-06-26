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

def manual_drive(): #You will use this function to program your ESC if required
    inp = raw_input()
    pi.set_servo_pulsewidth(ESC,inp)
        
def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
    pi.set_servo_pulsewidth(ESC, 0)
    pi.stop()

#Main program.
calibrate()
while True:
    print os.environ.get("v3")
    #manual_drive()
#inp = raw_input()
#if inp == "manual":
#    manual_drive()
#elif inp == "stop":
#    stop()
#else:
#    print("Thank You for not following the things I'm saying... now you gotta restart the program STUPID!!")

