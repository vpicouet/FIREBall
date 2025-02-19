import os.path
import os, sys
import numpy as np
from subprocess import call
import sys
import time
from datetime import datetime,timedelta

fn = '/home/fireball2/Code/'
dir = os.path.dirname(fn)	# fully qualified path

def expose_routine(indata):

    exptime, emgain = indata

    file_in = open(fn + '/file_num.txt', 'r')
    line = file_in.readline()
    file_in.close()

    print('\nThe previous image is image' + '{:06d}'.format(int(line)) + '.fits')

    os.remove(fn + '/file_num.txt')

    file_in = open(fn + '/file_num.txt','w')
    newline = str(int(line) + 1)
    file_in.write(newline)
    file_in.close()

    newimage = 'image' + '{:06d}'.format(int(newline))

    print('\nThe acquired image is image' + '{:06d}'.format(int(newline)) + '.fits')

    
    if emgain > 0:

        #do the c++ script by passing exptime and defined emgain value

    else:

	emgain = 0
	#do the c++ script by passing exptime and emgain=0

# -----------------------------------------------------------------------------
# The main function starts here
# -----------------------------------------------------------------------------
if __name__ == "__main__":
	usage = 'Usage: python %prog [options]'
	parser = OptionsParser()
	parser.add_option('-em', '--emgain', dest = 'emgain', metavar='EMGAIN',
			action='store', help='Default EmGain sent is 0', default=0
	)

	(options, args) = parser.parse_args()

    
        expose_routine(sys.argv[1], options.emgain)


