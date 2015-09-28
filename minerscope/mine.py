
from mcpi import minecraft as m
import picamera as cam 
import focus
#Generate a minecraft instance and place the player in front of the virtual laboratory
mc = m.Minecraft.create()
mc.player.setPos(-18,1,60.5)
mc.events.clearAll()
i =0
prevOn = False

#Main loop
while True:
	#Look for specific events
	png = '.png'
	e = mc.events.pollBlockHits()
	if (len(e) != 0):
		p = e[0].pos
		#Move the sample stage down
		if (p.x == -34  and p.y == 1 and p.z == 63):
			mc.events.clearAll()
			focus.down()
		#Capture an image from the picamera.
		if (p.x == -34 and p.y == 1 and p.z == 61):
			#Verify if the preview window is on.	
			if prevOn:
				c.stop_preview()
				c.close()
				prevOn = False
				focus.off()
			mc.postToChat('Picture taken')
			mc.events.clearAll()
			focus.on()
			c = cam.PiCamera()
			c.capture(str(i)+png)
			c.close()
			focus.off()
			i = i+1
		#Open/close the preview window.
		if (p.x == -34  and p.y == 1 and p.z == 59):
			if prevOn:
				focus.off()
				c.stop_preview()
				c.close()
				prevOn = False
			elif not prevOn:
				focus.on()
				c = cam.PiCamera()
				c.start_preview()
				c.preview_fullscreen = False
				c.preview_window = (0,0,640,640)
				prevOn = True
		#Move the sample stage up		
		if (p.x == -34 and p.y == 1 and p.z == 57):
			mc.events.clearAll()
			focus.up()
			

