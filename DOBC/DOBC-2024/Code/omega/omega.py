#!/usr/bin/python
# -----------------------------------------------------------------------------
# @file      omega.py
# @brief     send commands to the Omega temperature controller
# @author    David Hale <dhale@caltech.edu>
# @date      2014-09-26
# @modified  2015-10-30 Gillian Kyne <gkyne@caltech.edu>
# -----------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------
# @fn     omega_cmd
# @brief  send command to lakeshore
# @param  ser  serial object
# @param  cmd  command string
# -----------------------------------------------------------------------------
def omega_cmd(ser, cmd):

    endchar='\r\n'

    # send command here
    ser.write('%s\r\n' % cmd)
    time.sleep(0.2)

    # setup a sigalarm timer, disabled only when reply received
    signal.signal(signal.SIGALRM, sighandler)
    signal.alarm(5)

    # poll status
    reply=''
    while True:
        while ser.inWaiting() > 0:      # read chars from device
            r=ser.read(1)
            reply+=r
        if endchar in reply:
            break

    signal.alarm(0)                     # disarm timer

    reply=reply.split(endchar)
    print reply[0]
    return

# -----------------------------------------------------------------------------
# @fn     main
# @brief  the main function starts here
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    try:

        # open the serial device

	ser0  = serial.Serial(port='/dev/omega',
                              baudrate=9600,
                              parity=serial.PARITY_ODD,
                              stopbits=serial.STOPBITS_ONE,
                              bytesize=serial.SEVENBITS)
 
        # send the command specified as an argument

	# converting setpoint 1 value from string to hex

	#setpoint = hex conversion of sys.argv[1:] 
	#hex command for setpoint + converted number-to-hex inserted below before
	#where is says sys.argv[1:]. sys.argv[1:] is replaced by setpoint above.

        omega_cmd(ser0, " ".join(sys.argv[1:]))

    finally:
        ser0.close()
