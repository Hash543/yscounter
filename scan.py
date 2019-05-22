import sys
import serial
import pprint
import re
import os
import pycurl
import time
comf = open('public/comport.txt', 'r');
host = "http://61.220.182.219/";
ser = serial.Serial('COM'+comf.read(),timeout=21)  # open serial port
comf.close()
now = time.time();
loop = True;
while loop:
	buffer = ser.read(7)
	if(time.time()-now >=20 ):
		ser.close();
		loop = False;
	if(buffer != ""):
		result = re.search('^([A-Z0-9]+)',buffer)
		if(result != None):
			print(result.group(0));
			break;
		# if(len(result.groups()) >= 2):
		# 	print(result.group(1));
		# 	print(result.group(2));
		# 	if(result.group(1) == "CUS"):
		# 		f = open('/tmp/cust.txt', 'w+')
		# 		f.write(result.group(2))
		# 		#f = open('/tmp/point.txt', 'w+')
		# 	if(result.group(1) == "POI"):
		# 		f = open('/tmp/point.txt', 'w+')
		# 		f.write(result.group(2)+result.group(3))
		# 		print(result.group(3));
		# 	if(result.group(1) == "EMP"):
		# 		f = open('/tmp/cust.txt', 'r')
		# 		cusId = f.read();
		# 		f = open('/tmp/point.txt', 'r')
		# 		pointId = f.read();
		# 		print(host+"barcode/checkin/"+cusId+"/"+pointId+"/"+result.group(2));
		# 		url = host+"barcode/checkin/"+cusId+"/"+pointId+"/"+result.group(2)
		# 		c = pycurl.Curl()
		# 		c.setopt(c.URL, url )
		# 		c.perform()
		# 		c.close()
