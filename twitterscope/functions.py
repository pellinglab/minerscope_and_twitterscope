import json
from time import sleep as s 
import picamera
import scaleBar as scale
from flkr import uploadFlickr
from os import remove as rm
from PIL import Image as img
from math import sqrt,pow		
from focus import up, down,on,off
from PIL import ImageDraw as imgD
from PIL import ImageFont as imgF


def singleSnap(tweet,ti):
	
	#Single picture capture
	on()
	c = picamera.PiCamera()
	c.resolution = (1600,900)
	s(1)
	c.capture(ti+'.png')
	c.close()
	scale.scaleB(ti+'.png')
	off()
	
#Timelaspe control	
def timeLapse(tweet,ti):
	fonT = imgF.truetype('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf',60)
	frequency = 1
	duration = 1
	#Looking for the requested duration
	if (u'duration' in tweet):
		indexD = tweet.index('duration')+9
		duration = u''
		while tweet[indexD] != u' ':
			duration = duration+tweet[indexD]
			indexD = indexD+1
			if indexD > len(tweet)-1:
				break
		duration = int(duration)
	#Looking for the frequency
	if (u'frequency' in tweet):
		indexF = tweet.index('frequency')+10
		frequency = u''
		while tweet[indexF] != u' ': # and indexF <len(tweet) ?
			frequency = frequency+tweet[indexF]
			indexF = indexF+1
			if indexF > len(tweet)-1:
				break
		frequency = int(frequency)
	nImg = int(frequency*duration)
	on()
	#Timelapse loop
	for ix in range(0,nImg):
		
		c = picamera.PiCamera()
		c.resolution = (1600,900)
		s(1)	
		c.capture(str(ix)+'.png')
		c.close()
		s(60/frequency)
	off()
	tempIm = img.new('RGB',(800,900))
	for k in range(0,nImg):
		img2open = img.open(str(k)+'.png')
		imgD.Draw(img2open).text((1530,830),str(k+1),font=fonT,fill=(0,0,0,255))
		img2open.save(str(k)+'.png')
		uploadFlickr(str(k)+'.png','Image '+str(k+1)+' of timelapse initiated on '+ti)	
	image1 = img.open('0.png').resize((800,450))
	image2 = img.open(str(nImg-1)+'.png').resize((800,450))
	tempIm.paste(image1,(0,0))
	tempIm.paste(image2,(0,450))
	tempIm.save(ti+'.png')
			

#Focus control
def focusImg(tweet,ti):
	if (u'further' in tweet):
		indexUp = tweet.index('further')+8
                nUp = u''
                if indexUp < len(tweet):
			try:
				while tweet[indexUp] != u' ':
                        		nUp = nUp+tweet[indexUp]
                        		indexUp = indexUp+1
                        		if indexUp > len(tweet)-1:
                                		break
			except IndexError,TypeError:
				nUp = 1
		if nUp == u'':
			nUp = 1
		else:
			nUp = int(nUp)
		up(nUp)
		on()
		c = picamera.PiCamera()
	        s(1)
		c.capture(ti+'.png')
        	c.close()
		off()

	if (u'closer' in tweet):
                indexDn = tweet.index('closer')+7
                nDn = u''
		if indexDn < len(tweet):
			try:
                		while tweet[indexDn] != u' ':
                        		nDn = nDn+tweet[indexDn]
                        		indexDn = indexDn+1
                        		if indexDn > len(tweet)-1:
                                		break
			except IndexError,TypeError:
				nDn = 1
                if nDn == u'':
			nDn = 1
		else:
			nDn = int(nDn)
		
		down(nDn)
		c = picamera.PiCamera()
		s(1)
        	c.capture(ti+'.png')
       		c.close()
		off()


	
	if (u'dofocus' in tweet):
		fonT = imgF.truetype('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf',30)
		imgArray = []
		indexF = tweet.index('dofocus')+8
		nFocus = u''
		if indexF < len(tweet):
			try:
                		while tweet[indexF] != u' ':
                        		nFocus = nFocus+tweet[indexF]
                        		indexF = indexF+1
                        		if indexF > len(tweet)-1:
                                		break
			except IndexError,TypeError:
				nFocus = 1
                if nFocus == u'':
                        nFocus = 1
                else:
                        nFocus = int(nFocus)

		on()
		for i in range(0,2):
		        down(nFocus)
			c = picamera.PiCamera()
			s(1)
               		c.capture(str(i)+'.png')
                	imgAddNumber = img.open(str(i)+'.png').resize((400,400))
			imgD.Draw(imgAddNumber).text((360,360),str(i+1),font=fonT)
			imgAddNumber.save(str(i)+'.png')
			imgArray.append(img.open(str(i)+'.png'))
			c.close()
		up(nFocus*3)

		for i in range(2,4):
			up(nFocus)
			c = picamera.PiCamera()
			s(1)
                        c.capture(str(i)+'.png')
                        imgAddNumber = img.open(str(i)+'.png').resize((400,400))
                        imgD.Draw(imgAddNumber).text((360,360),str(i+1),font=fonT)
                        imgAddNumber.save(str(i)+'.png')
                        imgArray.append(img.open(str(i)+'.png'))
                        c.close()
		off()
 	
		down(nFocus*3)
		tempIm = img.new('RGB',(900,900))
		k = 0
		for i in range(25,900,450):
                	for j in range(25,900,450):
                                tempIm.paste(imgArray[k],(j,i))
                                k = k+1
		
		tempIm.save(ti+'.png')
		for i in range(0,4):
			rm(str(i)+'.png')

#Change and return the sample name
def sampleName(tweet):
	sampName = u''
	if (u'sampleName' in tweet):
                indexD = tweet.index('sampleName')+11
		try:
			tweet[indexD]
			while tweet[indexD] != u' ':
				sampName = sampName+tweet[indexD]
                        	indexD = indexD+1
                        	if indexD > len(tweet)-1:
                                	break
		except IndexError,TypeError:
			sampleName = u''

	return sampName
