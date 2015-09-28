
from requests.packages import urllib3
urllib3.disable_warnings()

import json
import tweepy
from tweepy.streaming import StreamListener as streaM
from tweepy import Stream
from time import sleep as s 
from flkr import uploadFlickr
import picamera
import functions #change file name
from os import remove as rm

#Enter yout API key (key), API secret (sec), access token (token) and secret token (tokenS) here.

key = 'your api key'
sec = 'your api secret'
token = 'your access token'
tokenS = 'your secret token'

#Authenticathe with the twitter's API
auth = tweepy.OAuthHandler(key,sec)
auth.set_access_token(token,tokenS)

api = tweepy.API(auth)

def sendTweet(msg):
	#Send a single "tweet" from the authenticated account
	api.update_status(status = msg)
	

def postPicture(path,msg):
	#Post a picture from the authenticated account
	api.update_with_media(path,status = msg)

#Name of the sample is set empty as default
theSampleName = u''
	
class X (streaM):
	
	
	#Filters the recived data from the twitter feed		
	def on_data(self,data):
		global theSampleName
		#Convert the JSon object to unicode
		y = json.loads(data)
		name = y['user']['name']
		at = y['user']['screen_name']
		tweet = y['text']
		loc = y['user']['location']
		ti = y['created_at']
		#Terminal data display
		print at,'	',name,'	',tweet,'	',loc,'	',ti
		print
	
		#Filter the returned tweet for a specific user		
		if((u'@your_account_name' in tweet):	#The user name need to be blanked before uploading
			#Condition for single image acquisition
			if(u'singleImage' in tweet):
				functions.singleSnap(tweet,ti)
				postPicture(ti+'.png','@'+at+' scale bar is 200 micrometers '+theSampleName)
				uploadFlickr(ti+'.png',name+'. '+tweet+'. '+theSampleName+' '+ti)
				rm(ti+'.png')
			
			#Condition for setting a timelapse
			if( u'diytimelapse' in tweet):
				functions.timeLapse(tweet,ti)
				postPicture(ti+'.png','@'+at)
				uploadFlickr(ti+'.png',name+'. '+tweet+'. '+theSampleName+' '+ti)
				rm(ti+'.png')
			#Condition for controlling the focus
			if (u'diyfocus' in tweet):
				functions.focusImg(tweet,ti)
				postPicture(ti+'.png','@'+at+' '+theSampleName)  
				uploadFlickr(ti+'.png',name+'. '+tweet+'. '+theSampleName+' '+ti)
                        	rm(ti+'.png')

			#Condition for help request
			if(u'diyhelp' in tweet):
				msgHelp = '@'+at+' Please read the README file at ' #include the github link
				sendTweet(msgHelp) #include help commands in this finction
			#Condition to change the sample name
			if(u'samplename' in tweet):
				theSampleName = functions.sampleName(tweet)

	def on_error(self,status):
		print(status)


print '@','     ' 'Name','      ','Tweet','     ','Location','  ','Time'



Stream(auth,X()).filter(track =['singleImage','diytimelapse','diyfocus','diyhelp','samplename'])



