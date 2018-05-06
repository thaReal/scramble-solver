# Module to process screencaptures and perform OCR Recognition
#-----
from PIL import Image

GAME_REGION = (60, 440, 1040, 1400)

BLACK = (0, 0, 0, 255)
WHITE  = (255, 255, 255, 255)

class ScreenCapture:
	def __init__(self):
		self.screen = Image.open('screencaptures/capture.png')
		self.screen.load()
			
			
	def cropScreen(self):
		self.letters = self.screen.crop(box=GAME_REGION)
		
		
	def cleanColor(self):
		x = 960
		y = 960
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
				x0 = (i * 248) + 175
				y0 = (j * 248)
				x1 = x0 + 45
				y1 = y0 + 45
				print "clearing %s, %s, %s, %s" % (x0, y0, x1, y1)
				self.whiteoutRegion(x0, y0, x1, y1)
		self.letters.save('screencaptures/capture-1.png')
		print "[+] Numbers scrubbed!"
		
		
	def splitCells(self):
		for i in range(4):
			for j in range(4):
				x0 = (i * 240) 
				y0 = (j * 240)
				x1 = x0 + 240
				y1 = y0 + 240
			
				region = (x0, y0, x1, y1)
				img = self.letters.crop(box=region)
			
				dest_str = 'screencaptures/cell-'
				dest_str += "%s-%s" % (str(i+1), str(j+1))
				dest_str += '.png'
			
				img.save(dest_str)
				print "[+] Saved image: %s-%s" % (str(i+1), str(j+1))
				#img.close()
				
			
	def makePreview(self):
		size = (200, 200)
		img_preview = self.letters.resize(size)
		img_preview.save('screencaptures/preview.png')
		#img_preview.close()
		print "[+] Preview thumbnail created!"
		
	
	def showPreview(self):
		preview_img = Image.open('screencaptures/preview.png')
		preview_img.load()
		preview_img.show()
		
	def makeRows(self):
		print "[+] Concatenating rows..."
		
		for i in range(4):
			row_img = Image.open('screencaptures/template_row.png')
			for j in range(4):
				imgstr = 'screencaptures/cell-%s-%s.png' % (str(j+1), str(i+1))
				letter_img = Image.open(imgstr)
				offset_x = j * 240
				row_img.paste(letter_img, (offset_x, 0))
				#letter_img.close()
			savestr = 'screencaptures/row-%s.png' % str(i+1)
			row_img.save(savestr)
			#row_img.close()
			print "[+] Finished row %s" % str(i+1)
		print "[+] Finished"
		
		
		
if __name__=='__main__':
	img = ScreenCapture()
	img.cropScreen()
	
	print "[+] Cleaning background colors"
	img.cleanColor()
	
	print "[+] Clearing numbers"
	img.eraseNumbers()
	
	print "[+] Splitting cells"
	img.splitCells()
	
	print "[+] Recombining"
	img.makeRows()
	
	img.makePreview()
	img.showPreview()
