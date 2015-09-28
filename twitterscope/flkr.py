import flickrapi
from time import localtime as l

#Enter api key and api secret here
key = 'your api key'
secret = 'your api secret'
#Authenticate to Flick's API
flickr = flickrapi.FlickrAPI(key,secret)
flickr.authenticate_via_browser(perms='write')

#Upload a picture to flickr with a description
def uploadFlickr(path,descri):
	flickr.upload(filename=path, description=descri)

