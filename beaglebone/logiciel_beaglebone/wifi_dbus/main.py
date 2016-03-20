import serial
from time import *
import sys
sys.path.append("../common_dbus")
from protocole import *
import os

os.system("echo BB-UART2 > /sys/devices/bone_capemgr.8/slots")
sleep(3)

ser = serial.Serial(port="/dev/ttyO2", baudrate=115200)

#ser.flushInput()
def enum(**enums):
    return type('Enum', (), enums)

Status = enum(ERR='ERROR', OK=['OK', 'ready', 'no change'], BUSY='busy')

def send_cmd(sCmd, waitTm=10, retry=5):
	print "Command send", sCmd
	lp = 0
	ret = ""
	for i in range(retry):
		ser.flushInput()
		ser.write( sCmd + "\r\n" )
		ret = ser.readline()	# Eat echo of command.
		sleep( 0.2 )
		while( lp < waitTm or 'busy' in ret):
			while( ser.inWaiting() ):
				ret = ser.readline().strip( "\r\n" )
				#logging.debug( ret )
				print ret
				lp = 0
			if( ret in Status.OK ): break
			#if( ret == 'ready' ): break
			if( ret == Status.ERR ): break
			sleep( 1 )
			lp += 1

		sleep(1)
		if( ret in Status.OK ): break

#
send_cmd("AT+RST")
send_cmd("AT+CWMODE=2")
send_cmd("AT+CWSAP=\"ESP8266\",\"1234567890\",5,3")
send_cmd("AT+CIPMUX=1")
send_cmd("AT+CIPSERVER=1,300")
send_cmd("AT+CIFSR")

p = Protocole()

while 1:
	a = ser.readline()
	d = a.split(":")
	e = d.split(",")
	print "Taille", e[:1]
	print "Message", d[1][int(e[:1]):]
	p.treatment(d[1][int(e[:1]):])