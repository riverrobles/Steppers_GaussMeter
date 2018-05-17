import serial
import time

class Meter:
	def __init__(self,com,baud=9600):
		self.ser = serial.Serial(com,baud)
		self.conversions = {'°':'0','®':'.','µ':'5','³':'3','¶':'6','¹':'9','\xad':'-','«':'+','Ç':'G'}
		
	def measure(self): #measures field
		msg = self.query("FIELD?\n").decode('unicode escape').split(' \r')[0]
		return self.fix_message(msg)

	def get_mult(self): #indicates multiplier for field values e.g. k = 1000 
		return self.query("FIELDM?\n").decode('unicode escape')[0]

	def get_unit(self): #indicates units of field values, G for Gauss and T for Tesla 
		msg = self.query("UNIT?\n").decode('unicode escape')[0]
		return self.fix_message(msg)

	def zero_probe(self): #zeros probe to current measurement
		self.ser.write(b"ZCAL\n")

	def unit_gauss(self): #sets units to Gauss
		self.ser.write(b"UNIT G\n")
		time.sleep(0.2)

	def unit_tesla(self): #sets units to Tesla 
		self.ser.write(b"UNIT T\n")
		time.sleep(0.2)
	
	def query(self,command):
		self.ser.write(command.encode())
		time.sleep(0.2)
		message = self.ser.read(self.ser.inWaiting())
		return message

	def fix_message(self,message):
		for char in self.conversions.keys():
			message = message.replace(char,self.conversions[char])
		return message

	def close(self): #ends serial communications 
		self.ser.close()