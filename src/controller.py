from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import os

# Nexus 7 Screen: 800 x 1200

PLAY_GAME = (400, 1160)
POWERUP_FREEZE = (110, 600)
POWERUP_PLAY = (400, 1050)

OK_BUTTON = (675, 275)	
RESUME_BUTTON = (395, 715)
PAUSE_BUTTON = (750, 105)

class ScrambleController:
	def __init__(self):
		print '[+] Controller started, waiting for device...'
		self.device = MonkeyRunner.waitForConnection()
		print '[+] Device attached!'
		
	def take_screenshot(self):
		result = self.device.takeSnapshot()
		result.writeToFile('screencaptures/shot1.png','png')
		
	def tap(self, coords):
		x, y = coords
		self.device.touch(x, y, MonkeyDevice.DOWN_AND_UP)
		
def prompt():
	dummy = raw_input('\n->\n')	

'''
cwd = os.getcwd()
datadir = cwd + "/solutiondata"
os.chdir(datadir)
'''

if __name__=='__main__':
	n7 = ScrambleController()
	time.sleep(3)
	print "pressing play"
	n7.tap(PLAY_GAME)
	time.sleep(3)
	print "pressing freeze"
	n7.tap(POWERUP_FREEZE)
	time.sleep(3)
	print "starting game"
	n7.tap(POWERUP_PLAY)
	time.sleep(5)
	print "taking screenshot"
	n7.take_screenshot()
	print "pressing pause"
	n7.tap(PAUSE_BUTTON)
	print 'Done!'
