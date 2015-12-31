# Scramble Solver v0.1
# ====================

import solver
import os

# TODO: need to add *better* code to create a new solutionfile for each puzzle

class SolutionFile:
	def __init__(self):
		self.solutionfile = file('solution.txt', 'w')
		self.solutionfile.seek(0)
		
	def makefile(self):
		self.cwd = os.getcwd()
		datafiles = os.listdir(self.cwd)
		n = 0
		if len(datafiles) != 0:
			for file in datafiles:
				n += 1
		#fname = 'solution' + str(n) + '.txt'
		
		#print "[+] Created solution file %s" % fname
					
		
	def writedata(self, data):
		self.solutionfile.write(data)
		self.solutionfile.write('\n')
		
	def close(self):
		self.solutionfile.close()
		

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
		
		print_game(self.game)
		self.run()
		
		
	def run(self):
		self.worker = solver.Worker(self.dictionary, self.game)
		print "[+] Scramble solver starting!"
		for i in range(4):
			for j in range(4):
				work_coord = (i, j)
				work_letter = self.game[i][j]
				work = solver.ChainRoot(work_letter, work_coord)
				
				print "[+] Worker started, coords: %s, %s" % (i, j)
						
				self.worker.work.append(work)
				self.worker.process_work()
		
				print "[+] Worker complete!"
				print "Finished cell %s, %s" % (i, j)
				print "Found %s Words" % len(self.worker.found_words)
				
		# DEBUG
		dummy = raw_input('~] ')
				
		# need to either just do this once or flush workers found word 
		# list each time
		## Better to just do once (if its not a memory issue) to make
		## duplicate checking simpler for our worker 
							
		for chain in self.worker.found_words:
			data = chain[1]
			datastr = ""
			for c in data:
				datastr = datastr + str(c[0]) + ', ' + str(c[1]) + '-'
			self.solution.writedata(datastr)
	
		print "[+] Finalizing..."
		
		self.solution.close()			
		self.dictionary.close()	
		print "[+] All data files successfully closed!"
		print "Finished!"	
				
if __name__=='__main__':
	newgame = GameEngine()
	
