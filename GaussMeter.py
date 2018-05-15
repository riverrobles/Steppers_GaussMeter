import serial
import time

class Meter:
	def __init__(self,com,baud):
		self.ser = serial.Serial(com,baud=9600)
		self.conversions = {'°':'0','®':'.','µ':'5','³':'3','¶':'6','¹':'9','\xad':'-','«':'+','Ç':'G'}
		
	def measure(self):
		msg = self.query("FIELD?\n").decode('unicode escape').split(' \r')[0]
		return self.fix_message(msg)

	def get_mult(self):
		return self.query("FIELDM?\n").decode('unicode escape')[0]

	def get_unit(self):
		msg = self.query("UNIT?\n").decode('unicode escape')[0]
		return self.fix_message(msg)

	def zero_probe(self):
		self.ser.write(b"ZCAL\n")

	def unit_gauss(self):
		self.ser.write(b"UNIT G\n")

	def unit_tesla(self):
		self.ser.write(b"UNIT T\n")
	
	def query(self,command):
		self.ser.write(command.encode())
		time.sleep(0.2)
		message = self.ser.read(self.ser.inWaiting())
		return message

	def fix_message(self,message):
		for char in self.conversions.keys():
			message = message.replace(char,self.conversions[char])
		return message

	def close(self):
		self.ser.close()