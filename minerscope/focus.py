import RPi.GPIO as gpio
from time import sleep as s
#Sleep time betweet steps for the miscrostepper
t = 8.0/1000.0
#Setting the Raspberry pi GPIOs
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(12,gpio.OUT)
gpio.setup(16,gpio.OUT)
gpio.setup(11,gpio.OUT)

#Moving the platform upwards
def up():
	gpio.output(16,1)
	for i in range(0,8):
		gpio.output(12,1)
		s(t)
		gpio.output(12,0)
		s(t)
	gpio.output(16,0)
#Moving the platform downwards
def down():
	gpio.output(16,0)
	for i in range(0,8):
		gpio.output(12,1)
		s(t)
		gpio.output(12,0)
		s(t)
	gpio.output(16,0)
#Turning the LED on
def on():
	gpio.output(11,1)
#Turning thr LED off
def off():
	gpio.output(11,0)
