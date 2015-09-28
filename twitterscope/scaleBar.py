# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw


def scaleB(path):
	pic = Image.open(path)
	bar = ImageDraw.Draw(pic)
	#The Default value for the scale bar is 190 pixels, which is the equivalent of 200 micrometers on a 1600 by 900 pixels image.
	#To change the default value, change the difference in the tuples in X inside "bar.rectangle()" 
	bar.rectangle([(1330,810),(1520,830)],fill=(255,255,255))
	pic.save(path,'PNG')

def mySize(path):
	pic = Image.open(path)
	print pic.size
