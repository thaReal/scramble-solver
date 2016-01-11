import subprocess
import os


def makeInputString():
	instr = ""
	basepath = "screencaptures/row-"
	
	for n in range(4):
		imgpath = basepath + str(n+1) + ".png"
		output = subprocess.Popen(["tesseract", imgpath, "-"], 
		stdout=subprocess.PIPE).communicate()[0]
		instr += output[0:4]
		print "[+] Finished row %s" % str(n+1)
	
	return instr
	
	
def startNewGame():
	retcode = subprocess.call(['./monkeyrunner', 'controller.py'])
	print retcode
	
	
def processScreenshot():
	retcode = subprocess.call(['python', 'imageprocessor.py'])
	if retcode == 0:
		print "[+] Screenshot processed!"
	else:
		print retcode
		

def playGame()
	retcode = subprocess.call(['./monkeyrunner', 'monkey_manager.py'])
	print retcode


# Need to add a new entry point into scramble_core so I can pass a string as 
# input rather than enter it manually.


if __name__=='__main__':
	startNewGame()
	processScreenshot()
	letters = makeInputString()
	print letters
	
