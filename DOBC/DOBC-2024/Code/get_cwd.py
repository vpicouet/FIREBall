import os.path
import os, sys
import numpy as np
from subprocess import call
import sys
import time
from datetime import datetime,timedelta

fn = '/home/fireball2/Code/'
dir = os.path.dirname(fn)	# fully qualified path


def get_cwd(cwd):

    if os.path.exists(fn + 'cwd.txt'):          # create data directory if needed
        os.remove(fn + 'cwd.txt')

    file_in = open(fn + 'cwd.txt', 'w')
    line = '/home/fireball2/data/' + cwd + '/'
    file_in.write(line)
    file_in.write('\n')
    file_in.close()

# -----------------------------------------------------------------------------
# The main function starts here
# -----------------------------------------------------------------------------
if __name__ == "__main__":
	    
        get_cwd(sys.argv[1])


