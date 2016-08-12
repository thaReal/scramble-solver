# Scramble puzzle-solving logic engine
# -----

'''
# Windows Version
DICT_KEYSEARCH = {
	'a': 7,
	'b': 117605,
	'c': 213278,
	'd': 397722,
	'e': 512468,
	'f': 593990,
	'g': 664977,
	'h': 722552,
	'i': 792313,
	'j': 881168,
	'k': 894265,
	'l': 910395,
	'm': 962003,
	'n': 1070321,
	'o': 1122276,
	'p': 1189734,
	'q': 1357841,
	'r': 1366720,
	's': 1479366,
	't': 1685601,
	'u': 1779231,
	'v': 1839092,
	'w': 1868335,
	'x': 1905094,
	'y': 1906537,
	'z': 1911161
}
'''

# Linux Version
DICT_KEYSEARCH = {
	'a': 0,
	'b': 107307,
	'c': 193777,
	'd': 362031,
	'e': 466734,
	'f': 541254,
	'g': 605295,
	'h': 657302,
	'i': 720846,
	'j': 802799,
	'k': 814589,
	'l': 829112,
	'm': 875785,
	'n': 974498,
	'o': 1022038,
	'p': 1083710,
	'q': 1237565,
	'r': 1245736,
	's': 1348341,
	't': 1535676,
	'u': 1620630,
	'v': 1675476,
	'w': 1702075,
	'x': 1735242,
	'y': 1736549,
	'z': 1740675
}

SEARCH_KEY = [(-1, -1), (0, -1), (1, -1),
			  (-1, 0), (1,0), # skip root cell
			  (-1, 1), (0, 1), (1, 1)]


class ChainRoot:
	def __init__(self, letter, coord):
		self.coord = coord
		self.rootstr = letter
		self.coord_list = []
		self.coord_list.append(self.coord)
		
		# BUGFIX for case where letter is "Qu"
		if letter == "Q":
			self.rootstr.append("U")
		

class WordChain:
	def __init__(self, parent, coord, letter):
		self.coord = coord
		self.coord_list = parent.coord_list + [(self.coord)]
		self.rootstr = parent.rootstr + letter
		
		# BUGFIX for case where letter is "Qu"
		# -> Doesn't work, not sure why...
		if letter == "Q":
			self.rootstr.append("U")
		
		
class Worker:
	def __init__(self, dictionary_file, game):
		self.dictionary = dictionary_file
		self.game = game
		self.work = []
		self.found_words = []
		self.workcount = 0
		
		
		
	def process_work(self):
		while len(self.work) != 0:
			chain = self.work.pop()
			self.workcount += 1
			
			check = self.lookup(chain)
			if check == True:
				self.find_adjacent(chain)
			
			if self.workcount % 100 == 0:
				print "Processed %s chains so far." % str(self.workcount)


	def find_adjacent(self, chain):
		root_cell = chain.coord
		adjacent_cells = []
		for i in SEARCH_KEY:
			cellx = root_cell[0] + i[0]
			celly = root_cell[1] + i[1]
			new_coord = (cellx, celly)
			adjacent_cells.append(new_coord)
		
		# check each cell for OOB
		valid_cells1 = []
		for cell in adjacent_cells:
			if cell[0] >= 0 and cell[1] >= 0 and cell[0] <= 3 and cell[1] <= 3:
				valid_cells1.append(cell)
		
		# check if cell is already used in word-chain
		valid_cells2 = []
		for j in valid_cells1:
			itr = 0
			for coord in chain.coord_list:
				if j == coord:
					itr = itr + 1		
			if itr == 0:
				valid_cells2.append(j)
		
		# create new chains with each valid cell and push back to work queue
		for newcoord in valid_cells2:
			row = newcoord[0]
			col = newcoord[1]
			letter = self.game[row][col]
			newchain = WordChain(chain, newcoord, letter)	
			self.work.append(newchain)
			
				
	def lookup(self, chain):
		lookup_string = chain.rootstr
		first_char = lookup_string[0]
		index = DICT_KEYSEARCH[first_char]
		self.dictionary.jump(index)
		
		while True:
			dword = self.dictionary.getword() 
			
			# check for a match starting at 2 letter words
			if len(lookup_string) >= 2:
				if lookup_string == dword:
					af = 0
					for word in self.found_words:
						if lookup_string == word[0]:
							af = af + 1
							
					if af == 0:
						self.found_words.append((lookup_string,
						chain.coord_list))
						#print "[+] Found word: %s!" % lookup_string
					
			# NOTE: can be optimized by saving a search index with chain object
			
			try:
				if dword[0] != first_char:
					return False
				elif dword.startswith(lookup_string):
					return True
			
			except:
				print "[-] Chain Ended; Out of Range Error"
				return False
		
		
if __name__=='__main__':
		pass
