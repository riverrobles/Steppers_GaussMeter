import serial 
import logging
import time 

class ArduinoBoard: 
	def __init__(self,port='COM4',interval=1500):
		self.ser = serial.Serial(port,9600,timeout=10)
		self.step_interval = interval 

	def step(self,stepper,steps):
		logging.debug("Stepping board {} {:.2} times".format(stepper,steps))
		time.sleep(1.0)
		self.ser.write(b'%s'%(stepper))
		time.sleep(1.0)

		goal_step_loc = steps
		step_loc = 0

        while(not step_loc==goal_step_loc):
            logging.debug('Looping ')
            if (abs(goal_step_loc - step_loc) < self.step_interval):
                self.ser.write(b'%i'%(goal_step_loc - step_loc))
                step_loc += goal_step_loc - step_loc
            elif (goal_step_loc - step_loc < 0):
                self.ser.write(b'%i'%-self.step_interval)
                step_loc += -self.step_interval
            elif (goal_step_loc - step_loc > 0):
                self.ser.write(b'%i'%self.step_interval)
                step_loc += self.step_interval

        logging.debug("Displacement complete")

    def close(self):
    	self.ser.close()