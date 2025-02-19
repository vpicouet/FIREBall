import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
#ser = serial.Serial(
#    port='/dev/ttyUSB1',
#    baudrate=9600,
#    parity=serial.PARITY_ODD,
#    stopbits=serial.STOPBITS_TWO,
#    bytesize=serial.SEVENBITS
#)
ser = serial.Serial(
  port="/dev/ttyUSB2", # connection string uses /dev/ttyUSB0 for this example 
                       # /dev/ttySn may be more typical (where n is serial port number)
                       # "dmesg | grep usb" will show USB to serial converter address 
                       # using above command address should be apparent if recently plugged
  baudrate=9600, # baud rate is configurable on the controller 4020 defaults to 115200
  bytesize = serial.SEVENBITS,
  stopbits = serial.STOPBITS_ONE,
  parity=serial.PARITY_ODD, # Galil controllers do not use parity bits
  rtscts= True # Galil controllers use RTS/CTS flow control
)


#ser.open()
ser.isOpen()

print 'Enter your commands below.\r\nInsert "exit" to leave the application.'

input=1
while 1 :
    # get keyboard input
    input = raw_input(">> ")
        # Python 3 users
        # input = input(">> ")
    if input == 'exit':
        ser.close()
        exit()
    else:
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        ser.write(input + '\r\n')
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1)

        if out != '':
            print ">>" + out
