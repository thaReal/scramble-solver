# MonkeyRunner tool to input generated coordinate list
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import os


OK_BUTTON = (675, 275)	
RESUME_BUTTON = (395, 715)

cwd = os.getcwd()
datadir = cwd + "/solutiondata"
os.chdir(datadir)

sfile = open('solution.txt', 'r')
sfile.seek(0, 2)
endfile = sfile.tell()
sfile.seek(0)

print 'waiting for device'
device = MonkeyRunner.waitForConnection()

print '[+] device attached'
print '[+] All systems go!'

device.touch(RESUME_BUTTON[0], RESUME_BUTTON[1], MonkeyDevice.DOWN_AND_UP)
time.sleep(1)

print '[+] Blast off!!\n'

t_sleep1 = 0.2
t_sleep2 = 0.2
time_start = time.time()
letter_count = 0
word_count = 0

class TournamentMonkey:
	def __init__(self, sfile):
		while sfile.tell() != endfile:
			line = sfile.readline()
			data = line.split('-')
			data.pop()
	
		if len(data) <= 3:
			t_sleep1 = 0.05
			t_sleep2 = 0.05

		elif len(data) < 7:
			t_sleep1 = 0.1
			t_sleep2 = 0.1
		
		else:
			t_sleep1 = 0.15
			t_sleep2 = 0.15
	
	for point in data:
		coords = KEYMAP[point]
		device.touch(coords[0], coords[1], MonkeyDevice.DOWN_AND_UP)
		letter_count += 1
		
	word_count = word_count + 1
	if word_count % 10 == 0:
		print "Entered %s words so far" % word_count
		
	time.sleep(t_sleep1)
	device.touch(675, 275, MonkeyDevice.DOWN_AND_UP)
	time.sleep(t_sleep2)	

	time_n = time.time()
	if time_n - time_start > 120.0:
		print "Game's done... I think..."
		break
	
	
time_end = time.time()
run_time = time_end - time_start
wps = word_count / run_time
lps = letter_count / run_time

sfile.close()

print "\n[+] aaand we're done!\n"
print "Runtime: %s seconds" % run_time
print "Words per second: %s" % wps
print "Letters per second: %s" % lps

