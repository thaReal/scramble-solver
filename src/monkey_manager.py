# MonkeyRunner tool to input generated coordinate list
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import os


# Keymap for Nexus 7 Tablet
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

OK_BUTTON = (675, 275)	
RESUME_BUTTON = (395, 715)

cwd = os.getcwd()
datadir = cwd + "/solutiondata"
os.chdir(datadir)

sfile = open('solution.txt', 'r')
sfile.seek(0, 2)
endfile = sfile.tell()
sfile.seek(0)
words_entered = 0

print 'waiting for device'
device = MonkeyRunner.waitForConnection()

print '[+] device attached'
print '[+] All systems go!'

device.touch(RESUME_BUTTON[0], RESUME_BUTTON[1], MonkeyDevice.DOWN_AND_UP)
time.sleep(1)

print '[+] Blast off!!\n'

t_sleep1 = 0.2
t_sleep2 = 0.2
#time_start = time.time()

while sfile.tell() != endfile:
	line = sfile.readline()
	data = line.split('-')
	data.pop()
	
	if len(data) <= 3:
		t_sleep1 = 0.1
		t_sleep2 = 0.1
	elif len(data) < 7:
		t_sleep1 = 0.1
		t_sleep2 = 0.2
	else:
		t_sleep1 = 0.2
		t_sleep2 = 0.2
	
		
	for point in data:
		coords = KEYMAP[point]
		device.touch(coords[0], coords[1], MonkeyDevice.DOWN_AND_UP)
		
	words_entered = words_entered + 1
	if words_entered % 10 == 0:
		print "Entered %s words so far" % words_entered
		
	time.sleep(t_sleep1)
	device.touch(675, 275, MonkeyDevice.DOWN_AND_UP)
	time.sleep(t_sleep2)	
	
#time_end = time.time()
#run_time = time_end - time_start
#wps = words_entered / run_time

print "\n[+] aaand we're done!\n"
#print "Runtime: %s seconds" % run_time
#print "Words per second: %s" % wps

sfile.close()
