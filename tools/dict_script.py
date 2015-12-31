# Dictionary Key-Lookup Table Maker Script
# ---

dictfile = open('dictionary.txt','r')
dictfile.seek(0)

letters = "abcdefghijklmnopqrstuvwxyz"
for letter in letters:
	marker = dictfile.tell()
	word = dictfile.readline()
	sletter = word[0]
	while letter != sletter:
		marker = dictfile.tell()
		word = dictfile.readline()
		sletter = word[0]
	print "%s: %s," % (sletter, marker)