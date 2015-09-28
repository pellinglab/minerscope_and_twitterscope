Minerscope and Twitterscope: Interfaces to control the DIY microscope
======

Twitterscope: 
======

API keys and tokens
------------
Before instaling the *Twitterscope* package, you will need to get an API key, an API secret, a token and a secret token from [Twitter](https://dev.twitter.com/).  Then you need to update theses values in the script.

	cd /usr/local/lib/python2.7/dist-packages/twitterscope-1.0-py2.7.egg/twitterscope

Now change the value of *key*, *sec*, *token* and *tokenS*, inside the *main.py* script:

	key = [your api key]
	sec = [your api secret]
	token = [your access token]
	token = [your secret access token]

You will also need to change the system account in the *main.py* script to your *Twitter's* account:

	...
	#Filter the returned tweet for a specific user          
        if((u'@yout_account_name' in tweet):       #The user name need to be blanked before uploading
        #Condition for single image acquisition
	...


Now you need to get an access token from [Flickr](https://www.flickr.com/services/apps/create/) and allow your application to *delete* and upload pictures. Then you need to change these values in the *flkr.py* script

	key = [your api key]
	secret = [yout api secret]


Installation
------------
First install the required dependencies:

	sudo apt-get install python-setuptools python-dev python-pip

Then close this repository and install the *Twitterscope* package:

	git clone https://github.com/pellinglab/minerscope_and_twitterscope.git
	cd minerscope_and_twitterscope
	python setup_twitterscope.py install

First run
-------------
Open a new Python terminal window and import the main script from twitterscope:

	from twitterscope import main

The program will promt a browser window to *Yahoo!*. Enter your credentials. *Yahoo!* will ask your permission to access the application.
Once you recieved the approval message, you can close the bowser and return to the Python terminal.  This step is only required once.

Documentation
-------------
To run the program, open a new Python terminal window and import the main script from twitterscope:

	from twitterscope import main

You should see the folling on the screen:

	@ Name Tweet Location Time

Now the program is running.  To acquire image with the microscope, you have to use the keywords inside a *tweet* refered the the microscope account:

	singleImage
	diyfocus
	diytimelapse  

*singleImage* will return a live image of the sample.  Correct usage:

	@DIYmicrospe singleImage

*diyfocus* will allow the user to control the focus of the system.  If the current focus level is unknown, the user can use the keyword *dofocus*, followed by an integer.  This will return an cluster of 4 images.  Each images correspond to a different positon of the sample stage (requested by the user, 2 closer and 2 further relative to the initial position).  Correct usage:

	@DIYmicrospe diyfocus dofocus 1

If the user needs to change the sample position along the optical axis, the keywords *closer/further* followed by an interger will move the sample up or down, by a desired amount.  Correct usage:

	@DIYmicoscope diyfocus closer 3
	
	or

	@DIYmicoscope diyfocus further 2

*diytimelapse* follwed by *duration* (in minutes) and *frequency* (in images per minutes) will initiated a timelapse.  All the images from the timelapse are saved onto *Flickr*, but only the first and the last images are returned via *Twitter*.  Correct usage:

	@DIYmicroscope diytimelapse duration 4 frequency 5

The user can also remotely change the name of the sample by using the *samplename* keyword.  Correct usage:

	@DIYmicroscope samplename [...]

The user can also remolely ask for help, using the *diyhelp*.  This will return this webpage as a link.  Correct usage:

	@DIYmicroscope diyhelp
 


Minerscope:
======

Installation
------------
Prior to installation, make sur you have minecraft installed on the Rasperry pi (more info at https://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/software/):    
	
	sudo apt-get update
	sudo apt-get install minecraft-pi

Clone the repository and install the *Minerscope* package:
	
	git clone https://github.com/pellinglab/minerscope_and_twitterscope.git
	cd minerscope_and_twitterscope
	python setup_minerscope.py install


First run
-------------
Open minecraft and create a new world.
Open a new Python terminal window and wait for the world to be generated.
In the terminal, import the "generateWorld" script:
		
		from minerscope import generateWorld
	
Wait a few seconds, you should see the world been generated.
If the player is stucted or the world is not correctly generated, return to the menu, start a new game and run "generateWorld" again.

Play
-------------
Now when the world is generated, run the "mine" script from the Python terminal:
		
		from minerscope import mine

Documentation
-------------
Depending on your wire configuration, the left (white) and right (black) blocks will control the focus (up or down).
The blue block will capture an image from the camera. The yellow block will display a preview image.

About
---------
-[Pellinglab](http://www.pellinglab.net/)
