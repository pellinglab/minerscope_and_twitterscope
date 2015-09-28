import RPi.GPIO as gpio
from time import sleep as s
#Setting the timestep for microstepping
t = 8.0/1000.0
#Setting the raspberry pi GPIOS
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(12,gpio.OUT)
gpio.setup(16,gpio.OUT)
gpio.setup(11,gpio.OUT)
#Move the sample stage by X steps upwards
def up(x):
	gpio.output(16,0)
	for n in range(0,x):
		for i in range(0,8):
			gpio.output(12,1)
			s(t)
			gpio.output(12,0)
			s(t)
	gpio.output(16,0)
#Move the sample stage by X downwards
def down(x):
	gpio.output(16,1)
	for n in range(0,x):
		for i in range(0,8):
			gpio.output(12,1)
			s(t)
			gpio.output(12,0)
			s(t)
	gpio.output(16,0)
#Turn the LED on
def on():
	gpio.output(11,1)
#Turn the LED off
def off():
	gpio.output(11,0)



