#!/usr/bin/python
# -----------------------------------------------------------------------------
# @file      get_omega_lks.py
# @brief     read temperatures from omega and lakeshore
# @author    Gillian Kyne <gkyne@caltech.edu>
# @date      2016-10-14
#
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
def get_temps(ser0, channels):

    endchar='\r\n'

    retval = {}

    for ch in channels:

        # send command here
        ser0.write('CRDG? %s\r\n' % ch)
        time.sleep(0.2)

        # setup a sigalarm timer, disabled only when home complete
        signal.signal(signal.SIGALRM, sighandler)
        signal.alarm(5)

        # poll status, wait for motion to stop
        temp=''
        while True:
            while ser0.inWaiting() > 0:      # read chars from device
                r=ser0.read(1)
                temp+=r
            if endchar in temp:
                break

        signal.alarm(0)                     # disarm timer

        temp=temp.split(endchar)
        retval[ch] = float( temp[0] )

    return retval


def omega_cmd(ser2, omegacmd):

    ser2.write('%s\r\n' % omegacmd)
    time.sleep(1)

    reply = ''

    while ser2.inWaiting() > 0:
        rtd=ser2.read(1)
        reply+=rtd
        if rtd == '\n':
           break

    return(reply[3:-1])

# -----------------------------------------------------------------------------
# @fn     main
# @brief  the main function starts here
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    try:

        # open the serial devices to Lesker 354 Ion Gauge

        ser0  = serial.Serial(port='/dev/lakeshore',
                              baudrate=9600,
                              parity=serial.PARITY_EVEN,
                              stopbits=serial.STOPBITS_ONE,
                              bytesize=serial.SEVENBITS)
 
        ser2  = serial.Serial(port='/dev/omega',
                              baudrate=9600,
                              parity=serial.PARITY_ODD,
                              stopbits=serial.STOPBITS_ONE,
                              bytesize=serial.SEVENBITS)

        #Lakeshore temperatures
        lkstemp = get_temps(ser0, ['1','2','3','5','6'])
        #Omega temperature
        omegacmd = '*X01'
        omegatemp = omega_cmd(ser2, omegacmd)
        
        time  = datetime.now().strftime("%D %T")
        dat   = [time, ",", [lkstemp, omegatemp], "\n"]     # put data in convenient list

        fn    = "/home/fireball2/data/" + datetime.now().strftime("%y%m%d") + "/omega_lks.csv"
        dir   = os.path.dirname(fn)          # fully qualified path

        if not os.path.exists(dir):          # create data directory if needed
            os.makedirs(dir)

        if not os.path.exists(fn):           # write a header?
            writeheader = True
        else:
            writeheader = False

        fp = open(fn, 'a')                   # open file for append/write

        if writeheader:
            fp.write('time,CuClamp1[C],Getter[C],CuClamp2[C],sidetank[C],toptank[C],EMCCDBack[C]\n')         # header

        fp.write('{0},{1: <8},{2: <8},{3: <8},{4: <8},{5: <8},{6: <8}\n'.format(time, lkstemp['3'], lkstemp['1'], lkstemp['2'], lkstemp['5'], lkstemp['6'],omegatemp))
        fp.close()


    finally:
        ser0.close()
        ser2.close()

