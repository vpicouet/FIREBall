#!/usr/bin/python

import os.path
import os, sys
# import numpy as np
import subprocess
import sys
import time
from datetime import datetime,timedelta

def expose(exptime,emgain):

    command1 = './cam exptime='+str(exptime)
    print command1
    subprocess.call(command1,shell=True)

    command2 = './cam emgain='+str(emgain)
    print command2
    subprocess.call(command2,shell=True)
    
    command3 = './cam expose'
    print command3
    subprocess.call(command3,shell=True)

def HV_test():

    exptime_sky = 0, 1
    total_time = 2, 2
    emgain_sky = 0, 7269, 7584, 7898, 8212, 8526, 8841, 9155, 9469, 9783, 10097, 10412
    #emgain_sky = 0, 8526, 9155, 9783, 10412, 11040

    for j in range(0,12):
        for i in range(0,2):
            for k in range(0,total_time[i]): 
                expose(exptime_sky[i],emgain_sky[j])

# -----------------------------------------------------------------------------
# The main function starts here
# -----------------------------------------------------------------------------
if __name__ == "__main__":

	HV_test()




