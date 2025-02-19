#!/usr/bin/python
# -----------------------------------------------------------------------------
# @file      get_all_temps.py
# @brief     read temperature sensors from ruggeduino shield
# @author    Gillian Kyne <gkyne@caltech.edu>
# @date      2017-04-18
# -----------------------------------------------------------------------------

import numpy as np
import signal
import serial
import os
import sys
import time
from datetime import datetime,timedelta

# -----------------------------------------------------------------------------
# @fn     sighandler
# @brief  signal handler
# -----------------------------------------------------------------------------
def sighandler(signum, frame):
    print "sighandler got signal", signum
    raise IOError("SIGALRM timeout")

#---------------------------------------------------------------------------
def get_arduino(ser0):

    #using serial read() instead of readline(), readline() stopped working properly.

    temp = []
    rtd = ''
    i = 0

    while True:
         if ser0.inWaiting() > 0:  #if incoming bytes are waiting to be read from the serial input buffer
            r=ser0.read(1) #reads whole line as it's printed from the arduino
            rtd += r
            if r == '\n':
                temp.append(rtd)
                rtd = ''
                i = i+1
                continue
            if i == 4:
                break
    return temp

# -----------------------------------------------------------------------------
# @fn     main
# @brief  the main function starts here
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    try:

        # open the serial devices
        ser0  = serial.Serial(port='/dev/sparearduino',baudrate=115200,timeout=5,xonxoff=False,rtscts=False,dsrdtr=False)

        #arduino temperatures
        ard = get_arduino(ser0)
        #print ard
        ard0 = str(ard[0]).replace("\r\n","")
        print ard0
        ard1 = str(ard[1]).replace("\r\n","")
        print ard1
        ard2 = str(ard[2]).replace("\r\n","")
        print ard2
        ard3 = str(ard[3]).replace("\r\n","")
        print ard3
        
        time  = datetime.now().strftime("%D %T")
        dat   = [time, ",", [ard2], "\n"]     # put data in convenient list

        fn    = "/home/fireball2/data/" + datetime.now().strftime("%y%m%d") + "/ruggeduino_test.csv"
        dir   = os.path.dirname(fn)          # fully qualified path

        if not os.path.exists(dir):          # create data directory if needed
            os.makedirs(dir)

        if not os.path.exists(fn):           # write a header?
            writeheader = True
        else:
            writeheader = False

        fp = open(fn, 'a')                   # open file for append/write

        if writeheader:
            fp.write('time,Flange DOBC[C]\n')         # header

        fp.write('{0},{1: <8}\n'.format(time,ard2))
        fp.close()

        
    finally:
        ser0.close()
