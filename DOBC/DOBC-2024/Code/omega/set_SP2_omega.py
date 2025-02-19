#!/usr/bin/python

import signal
import serial
import os
import sys
import time
from datetime import datetime,timedelta

 
def omega_cmd(ser, cmd):

    fullcmd = '*W02' + str(cmd)

    ser0.write('%s\r\n' % fullcmd)
    time.sleep(0.2)
    ser0.write('%s\r\n' % '*Z02')  #after sending a write command, a hard reset if required to load changes into volatile memory
    time.sleep(0.2)

    return()

def convert_temp(temp):

    temp = ", ".join(temp)
    temp = str(temp)
        
    temp_SP2 = ''

    if temp[0] == '-':

        temp_SP2 = 'A'
        temp = temp[1:]

    else:

        temp_SP2 = '2'
        temp = temp[0:]

    tempDec = int(temp)*10
    tempBin = bin(tempDec)
    tempHex = hex(int(tempBin,2))
    
    if len(tempHex[2:]) == 3:
       temp_SP2 = temp_SP2 + '00' + tempHex[2:].upper()

    elif len(tempHex[2:]) < 2:
       temp_SP2 = temp_SP2 + '0000' + tempHex[2:].upper()

    elif len(tempHex[2:]) < 3:
       temp_SP2 = temp_SP2 + '000' + tempHex[2:].upper()

	
    return(temp_SP2)

#---------------------------------------------------------------------------
# The main function starts here
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    try:

    # open the serial device

        ser0  = serial.Serial(port='/dev/omega',
                              baudrate=9600,
                              parity=serial.PARITY_ODD,
                              stopbits=serial.STOPBITS_ONE,
                              bytesize=serial.SEVENBITS)

	cmd = convert_temp(sys.argv[1:])
        omega_cmd(ser0, cmd)

	
    finally:
        
        time.sleep(1)
        ser0.close()

