from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
#import imageprocessor
import time

# Keymappings for Nexus 7 Tablet (2012)
# Nexus 7 Screen: 800 x 1200


KEYMAP = {
		'0, 0': (140, 450),
		'0, 1': (310, 450),
		'0, 2': (480, 450),
		'0, 3': (650, 450),
		'1, 0': (140, 625),
		'1, 1': (310, 625),
		'1, 2': (480, 625),
		'1, 3': (650, 625),
		'2, 0': (140, 800),
		'2, 1': (310, 800),
		'2, 2': (480, 800),
		'2, 3': (650, 800),
		'3, 0': (140, 975),
		'3, 1': (310, 975),
		'3, 2': (480, 975),
		'3, 3': (650, 975)
}

# Gameflow button mappings
PLAY_GAME = (400, 1160)
POWERUP_FREEZE = (110, 600)
POWERUP_PLAY = (400, 1050)
OK_BUTTON = (675, 275)	
RESUME_BUTTON = (395, 715)
PAUSE_BUTTON = (750, 105)


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


if __name__=='__main__':
	n7 = ScrambleController()
	n7.start_sequence()
	'''
	screencap = imageprocessor.ScreenCapture()
	
	screencap.cropScreen()
	screencap.cleanColor()
	screencap.showImage()
	'''
