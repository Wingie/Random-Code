import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)
import subprocess

while 1:
    i = ser.readline()
    print i
    cmd = "xbacklight -set " + str(100-int(i[0:-2]))
    print cmd
    subprocess.call(cmd, shell=True)
    
    

