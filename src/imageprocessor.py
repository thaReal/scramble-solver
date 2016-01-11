# Module to process screencaptures and perform OCR Recognition
#-----

from PIL import Image

GAME_REGION = (60, 360, 740, 1040)

BLACK = (0, 0, 0, 255)
WHITE  = (255, 255, 255, 255)

class ScreenCapture:
	def __init__(self):
		self.screen = Image.open('screencaptures/capture.png')
		self.screen.load()
			
			
	def cropScreen(self):
		self.letters = self.screen.crop(box=GAME_REGION)
		
		
	def cleanColor(self):
		x = 680
		y = 680
		for i in range(x):
			for j in range(y):
				pixel = self.letters.getpixel((i, j))
				if pixel != BLACK and pixel != WHITE:
					self.letters.putpixel((i, j), WHITE)
		print "Finished!"
		self.letters.save('screencaptures/capture-1.png')
		
		
	def showImage(self):
		self.letters.show()
		
		
	def whiteoutRegion(self, x0, y0, x1, y1):
		range_x = x1 - x0
		range_y = y1 - y0
		for i in range(range_x):
			for j in range(range_y):
				x = x0 + i
				y = y0 + j
				self.letters.putpixel((x, y), WHITE)	
	
	def eraseNumbers(self):
		for i in range(4):
			for j in range(4):
				x0 = (i * 170) + 120
				y0 = (j * 170)
				x1 = x0 + 50
				y1 = y0 + 50
				print "clearing %s, %s, %s, %s" % (x0, y0, x1, y1)
				self.whiteoutRegion(x0, y0, x1, y1)
		self.letters.save('screencaptures/capture-3.png')
		print "[+] Numbers scrubbed!"
		
	def splitRows(self):
		for n in range(4):
			x0 = 0
			y0 = (n * 170)
			x1 = 680
			y1 = y0 + 170
			region = (x0, y0, x1, y1)
			img = self.letters.crop(box=region)
			dest_str = 'screencaptures/row-' + str(n + 1) + '.png'
			img.save(dest_str)
			print "[+] Saved image: %s" % str(n +1)
			
			
		
		
		
if __name__=='__main__':
	img = ScreenCapture()
	img.cropScreen()
	
	print "[+] Cleaning background colors"
	img.cleanColor()
	
	print "[+] Clearing numbers"
	img.eraseNumbers()
	
	img.splitRows()
	
	img.showImage()
