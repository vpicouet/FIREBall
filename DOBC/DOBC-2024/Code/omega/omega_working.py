#!/usr/bin/python

import signal
import serial
import os
import sys
import time
from datetime import datetime,timedelta


ser0 = serial.Serial(port='/dev/ttyS1', baudrate=9600, parity=serial.PARITY_ODD, stopbits=serial.STOPBITS_ONE,                             bytesize=serial.SEVENBITS)
 
def omega_cmd(ser, cmd):

    ser0.write('%s\r\n' % '*X01')
    time.sleep(0.2)
    rtd=ser0.read(10)
    rtd = rtd[3:9]
#ser0.close()

    return(rtd)
#def omega_cmd(ser, cmd):

 #   endchar='\r\n'

    # send command here
    #ser.write('%s\r\n' % cmd)
    #time.sleep(0.2)

    # setup a sigalarm timer, disabled only when reply received
    #signal.signal(signal.SIGALRM, sighandler)
    #signal.alarm(5)
  

    # poll status
    #reply=''
    #while True:
    #    while ser.inWaiting() > 0:      # read chars from device
    #       r=ser.read(2)
    #        reply+=r
    #    if endchar in reply:
    #        break

    #signal.alarm(0)                     # disarm timer

    #reply=reply.split(endchar)
    #print reply[0]
    #return

#---------------------------------------------------------------------------
# The main function starts here
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    try:

    # open the serial device

        ser0  = serial.Serial(port='/dev/ttyS1',
                              baudrate=9600,
                              parity=serial.PARITY_ODD,
                              stopbits=serial.STOPBITS_ONE,
                              bytesize=serial.SEVENBITS)

        temp = omega_cmd(ser0, sys.argv[1:])

        print temp

	time  = datetime.now().strftime("%D %T")
	dat   = [time, ",", temp, "\n"]     # put data in list

	fn    = "/home/fireball2/data/" + datetime.now().strftime("%y%m%d") + "/omega_temp.csv"
	dir   = os.path.dirname(fn) 

        if not os.path.exists(dir):# create data directory if needed
	    os.makedirs(dir)

	if not os.path.exists(fn): # write a header?
                writeheader = True
	else:
		writeheader = False

        fp = open(fn, 'a') # open file for append/write

        print temp

        if writeheader:
	    fp.write('time,temp[C]\n')# header
        fp.write('{0}, {1}\n'.format(time, temp))
	fp.close()

    finally:
        
        ser0.close()

