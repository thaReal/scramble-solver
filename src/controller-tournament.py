from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
from sys import argv

# Keymappings for Nexus 7 Tablet (2012)
# Nexus 7 Screen: 800 x 1200


KEYMAP = {
		'0, 0': (180, 560),
		'0, 1': (420, 560),
		'0, 2': (660, 560),
		'0, 3': (900, 560),
		'1, 0': (180, 800),
		'1, 1': (420, 800),
		'1, 2': (660, 800),
		'1, 3': (900, 800),
		'2, 0': (180, 1040),
		'2, 1': (420, 1040),
		'2, 2': (660, 1040),
		'2, 3': (900, 1040),
		'3, 0': (180, 1280),
		'3, 1': (420, 1280),
		'3, 2': (660, 1280),
		'3, 3': (900, 1280)
}

# Gameflow button mappings
PLAY_GAME = (800, 1700)
POWERUP_FREEZE = (150, 750)
POWERUP_PLAY = (540, 1590)
OK_BUTTON = (800, 150)	# is this used?
RESUME_BUTTON = (750, 1000)
PAUSE_BUTTON = (1000, 100)
TOURNAMENT_PLAY= (540, 1590) # same as powerup_play?

#-----

class ScrambleController:
	def __init__(self):
		self.initConnection()
	

	def initConnection(self):
		print '[+] Controller started, waiting for device...'
		self.device = MonkeyRunner.waitForConnection()
		print '[+] Device attached!'
		
		
	def take_screenshot(self):
		self.screenshot = self.device.takeSnapshot()
		

	def save_screenshot(self):
		self.screenshot.writeToFile('screencaptures/capture.png','png')
		

	def tap(self, coords):
		x, y = coords
		self.device.touch(x, y, MonkeyDevice.DOWN_AND_UP)

		
	def start_sequence(self):
		print "pressing play"
		self.tap(PLAY_GAME)
		time.sleep(3)
	
		print "pressing freeze"
		self.tap(POWERUP_FREEZE)
		time.sleep(3)
	
		print "starting game"
		self.tap(POWERUP_PLAY)
		time.sleep(5)
	
		print "taking screenshot"
		self.take_screenshot()
	
		print "pressing pause"
		self.tap(PAUSE_BUTTON)
	
		print "saving screenshot..."
		self.save_screenshot()
		
		print 'Done!'



	def tournament_start_sequence(self):
		print "pressing freeze"
		self.tap(POWERUP_FREEZE)
		time.sleep(3)
		
		print "starting"
		self.tap(TOURNAMENT_PLAY)
		time.sleep(5)

		print "taking screenshot"
		self.take_screenshot()
	
		print "pressing pause"
		self.tap(PAUSE_BUTTON)
	
		print "saving screenshot..."
		self.save_screenshot()


if __name__=='__main__':
	n7 = ScrambleController()
	# only difference between standard 'controllor' is the specific start
	# sequence commands
	n7.tournament_start_sequence()

