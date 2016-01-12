import subprocess
import os
import time

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
		

def solveBoard(inputstr):
	retcode = subprocess.call(['python', 'scramble_core.py', inputstr])
	print retcode
		

def playGame():
	retcode = subprocess.call(['./monkeyrunner', 'monkey_manager.py'])
	print retcode


# Need to add a new entry point into scramble_core so I can pass a string as 
# input rather than enter it manually.


if __name__=='__main__':
	print "\n[STARTING GAME]\n"
	startNewGame()
	
	time1 = time.time()
	print "[+] Timer Started!"
	
	print "\n[PROCESSING SCREEN]\n"
	processScreenshot()
	
	print "\n[EXTRACTING LETTERS]\n"
	letters = makeInputString()
	
	print '\n-> ' + letters + '\n'
	
	print "\n[SOLVER STARTING]\n"
	solveBoard(letters)
	
	time2 = time.time()
	
	print "\n[WINNING]\n"
	playGame()
	
	time3 = time.time()
	timer1 = time2 - time1
	timer2 = time3 - time1
	
	print "[+] Timer(s) Ended!"
	print "\nTime to solve: %s" % timer1
	print "\nTime to complete: %s" % timer2
	
