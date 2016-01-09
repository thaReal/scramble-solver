# Scramble Solver v0.1
# ====================

import solver
import os
import time
import csv

LOG_STATS = True

class StatGetter:
	def __init__(self):
		self.sourcedir = os.getcwd()
		self.datadir = self.sourcedir + "/solutiondata/"
		os.chdir(self.datadir)
		self.statfile = open('stats.csv', 'a')
		self.csv_writer = csv.writer(self.statfile)
		os.chdir(self.sourcedir)
		
	def logstats(self, data):
		self.csv_writer.writerow(data)
		
	def close(self):
		self.statfile.close()
		

class SolutionFile:
	def __init__(self):
		self.makefiles()
		
	def makefiles(self):
		self.maindir = os.getcwd()
		self.datadir = self.maindir + "/solutiondata/"
		os.chdir(self.datadir)
		
		#create output files
		self.wordsbig = file('words-big.txt' , 'w')
		self.wordsmed = file('words-med.txt', 'w')
		self.wordssml = file('words-sml.txt', 'w')
		
		files = os.listdir(self.datadir)
		for f in files:
			if f == 'solution.txt':
				os.remove(self.datadir + "solution.txt")
				print "Old solution file removed"
		
		# change back to src directory
		os.chdir(self.maindir)
		
		
	def writedata(self, data):
		self.solutionfile.write(data)
				
	# Functions to write found words to respective files based on size
	# NOTE: probably want to eventually move this all to a post processing step
	# that can do a finer sort, collect stats, randomize, etc.
		
	def writebig(self, data):
		self.wordsbig.write(data)
		self.wordsbig.write('\n')
		
	def writemed(self, data):
		self.wordsmed.write(data)
		self.wordsmed.write('\n')
		
	def writesml(self, data):
		self.wordssml.write(data)
		self.wordssml.write('\n')
		
	def catwords(self):
		# close and reopen output files in read mode & create solutionfile
		self.close()
		os.chdir(self.datadir)
		
		self.solutionfile = file('solution.txt', 'w')
		self.wordsbig = file('words-big.txt' , 'r')
		self.wordsmed = file('words-med.txt', 'r')
		self.wordssml = file('words-sml.txt', 'r')
		
		self.wordsbig.seek(0, 2)
		bigend = self.wordsbig.tell()
		self.wordsbig.seek(0)
		
		self.wordsmed.seek(0, 2)
		medend = self.wordsmed.tell()
		self.wordsmed.seek(0)
		
		self.wordssml.seek(0, 2)
		smlend = self.wordssml.tell()
		self.wordssml.seek(0)
		
		while self.wordsbig.tell() < bigend:
			data = self.wordsbig.readline()
			data.rstrip('\n')
			self.writedata(data)
		
		while self.wordsmed.tell() < medend:
			data = self.wordsmed.readline()
			data.rstrip('\n')
			self.writedata(data)
			
		while self.wordssml.tell() < smlend:
			data = self.wordssml.readline()
			data.rstrip('\n')
			self.writedata(data)
		
		self.close()
		self.solutionfile.close()
		
		# lets remove the intermediate files here
		try:
			os.remove('words-big.txt')
			os.remove('words-med.txt')
			os.remove('words-sml.txt')
			print "[+] All files succesfully closed"
		except:
			print "[-] Intermediate file delete FAILED!"
				
	# Close all output files in one clean shot
	def close(self):
		self.wordsbig.close()
		self.wordsmed.close()
		self.wordssml.close()
		

class WordDictionary:
	def __init__(self):
		self.dictfile = file('dictionary.txt', 'r')
		
	def getword(self):
		word = self.dictfile.readline()
		return word.rstrip('\n')
		
	def jump(self, index):
		self.dictfile.seek(index)
	
	def close(self):
		self.dictfile.close()
		

def get_input():
	print ""
	input_letters = raw_input("Enter Letters: ")
	input_letters.upper()
	return input_letters


def check_letters(letter_string):
	if len(letter_string) != 16:
		return False
	else:
		return True


def make_game_array(input_letters):
	game = []
	count = 0
	for i in range(4):
		row = []
		for j in range(4):
			row.append(input_letters[count])
			count = count + 1
		game.append(row) 
	return game


def print_game(game_array):
	print ""
	print " ------------------"
	for row in game_array:
		print row
	print " ------------------"
	print ""

#-----

class GameEngine:
	def __init__(self):
		self.user_input = get_input()
		
		if check_letters(self.user_input) != True:
			print "[-] Input Error!"
			exit()
		else:
			self.game = make_game_array(self.user_input)
			print "[+] Game array created!"
		
		self.dictionary = WordDictionary()
		print "[+] Dictionary Loaded!"
		self.solution = SolutionFile()
		print "[+] Solution file loaded!"
		if LOG_STATS:
			self.stats = StatGetter()
			print "[+] Stats file loaded!"
		
		print_game(self.game)
		self.run()
		
		
	def run(self):
		self.worker = solver.Worker(self.dictionary, self.game)
		print "[+] Scramble solver starting!"
		
		for i in range(4):
			for j in range(4):
				time_start = time.time()
				
				work_coord = (i, j)
				work_letter = self.game[i][j]
				work = solver.ChainRoot(work_letter, work_coord)
				
				self.worker.work.append(work)
				self.worker.process_work()

				n = (i * 4) + j + 1				
				progress = (n / 16.0) * 100.0

				outstr = "[+] %3.1f" % progress
				outstr += "%"
				outstr += " done"
				
				time_done = time.time()
				time_elapsed = time_done - time_start
				
				print outstr
				print "Found %s Words" % len(self.worker.found_words)
				print "Cell time: %4.2f" % time_elapsed
				print "%s chains processed\n" % self.worker.workcount
				
				if LOG_STATS:
					self.stats.logstats([n, len(self.worker.found_words), 
					self.worker.workcount, time_elapsed])
				
							
		big_count = 0
		med_count = 0 
		sml_count = 0

		for chain in self.worker.found_words:
			data = chain[1]
			datastr = ""
			wordlength = 0
			
			for c in data:
				datastr = datastr + str(c[0]) + ', ' + str(c[1]) + '-'
				wordlength += 1
			
			if wordlength > 6:
				self.solution.writebig(datastr)
				big_count += 1
			
			elif wordlength > 3:
				self.solution.writemed(datastr)
				med_count += 1
			
			else:
				self.solution.writesml(datastr)
				sml_count += 1
				
		print "Found %s big words, %s medium words, and %s small words" % (big_count, med_count, sml_count)
		
		print "[+] Finalizing..."
		self.solution.catwords()
		
		self.solution.close()			
		self.dictionary.close()
		self.stats.close()
	
		print "[+] All solution files successfully written!"
		print "Finished!"	
		
				
if __name__=='__main__':
	newgame = GameEngine()
