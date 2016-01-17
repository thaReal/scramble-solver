import subprocess
import os
import time
from sys import argv

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
	

def verifyInput(inputstr):
	print '\n-> ' + inputstr + '\n'
	verify = raw_input("Is this correct? [y/n] ")
	if verify != 'y':
		print "Enter correct puzzle letters: "
		letters = raw_input('> ')
	else:
		letters = inputstr
	return letters
	
	
def startNewGame(tournament=False):
	if tournament:
		retcode = subprocess.call(['./monkeyrunner', 'controller-tournament.py'])
	else:	
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



if __name__=='__main__':
	if len(argv) > 1:
		if argv[1] == 't':
			print "\n[STARTING TOURNAMENT ROUNG]\n"		
			startNewGame(tournament=True)
	else:
		print "\n[STARTING GAME]\n"
		startNewGame()
	
	time1 = time.time()
	print "[+] Timer Started!"
	
	print "\n[PROCESSING SCREEN]\n"
	processScreenshot()
	
	print "\n[EXTRACTING LETTERS]\n"
	
	inputstr = makeInputString()
	letters = verifyInput(inputstr)
	
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
	
