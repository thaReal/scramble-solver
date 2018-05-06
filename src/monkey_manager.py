# MonkeyRunner tool to input generated coordinate list
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import os


# Keymap for Nexus 7 Tablet
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

OK_BUTTON = (920, 265)	# is this used?
RESUME_BUTTON = (750, 1000)

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

while sfile.tell() != endfile:
	line = sfile.readline()
	data = line.split('-')
	data.pop()
	
	if len(data) <= 3:
		t_sleep1 = 0.125
		t_sleep2 = 0.125
	
	elif len(data) < 6:
		t_sleep1 = 0.125
		t_sleep2 = 0.15
	
	elif len(data) < 8:
		t_sleep1 = 0.15
		t_sleep2 = 0.2
	
	else:
		t_sleep1 = 0.2
		t_sleep2 = 0.2
	
		
	for point in data:
		coords = KEYMAP[point]
		device.touch(coords[0], coords[1], MonkeyDevice.DOWN_AND_UP)
		letter_count += 1
		
	word_count = word_count + 1
	if word_count % 10 == 0:
		print "Entered %s words so far" % word_count
		
	time.sleep(t_sleep1)
	device.touch(OK_BUTTON[0], OK_BUTTON[1], MonkeyDevice.DOWN_AND_UP)
	time.sleep(t_sleep2)	
	
time_end = time.time()
run_time = time_end - time_start
wps = word_count / run_time
lps = letter_count / run_time

sfile.close()

print "\n[+] aaand we're done!\n"
print "Runtime: %s seconds" % run_time
print "Words per second: %s" % wps
print "Letters per second: %s" % lps

