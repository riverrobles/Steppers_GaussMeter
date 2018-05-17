from GaussMeter import Meter 

''' 
simple code to initialize communication with the meter (connected at COM3 in this case), zero the probe, then take a measurement, find out the field multiplier, and the field units after setting the units to Tesla
then repeat setting units to Gauss.  
'''

gm = Meter('COM3',9600)

gm.unit_tesla() #changes units to tesla

value = gm.measure() 
mult = gm.get_mult()
units = gm.get_unit()

measurement = "{}{}{}".format(value,mult,units)
print(measurement)

gm.unit_gauss()

valueg = gm.measure()
multg = gm.get_mult()
unitsg = gm.get_unit()

measurementg = "{}{}{}".format(valueg,multg,unitsg)
print(measurementg)

gm.close()