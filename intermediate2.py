import sys
import os.path

#command line arguments - 0 for filename 1 onwards arguments
filename = sys.argv[0]
print (filename)


#file handling
if os.path.exists(filename):
	wordDict = {}
	f = open(filename,'r')		# a-append , w-write, append'b' for binary
	wordList = f.read().split()
	
	for word in wordList:
		if word in wordDict.keys():
			wordDict[word] += 1
		else:
			wordDict[word] = 1
	
	f.close()					#always remember to close file
	newFilename = filename + ".wc"
	f = open(newFilename ,'w')
	for key,val in wordDict.items():
		f.write("%s ==> %d\n" % (key,val))
	f.close()
else:
	print(" NO such file found")
	sys.exit(1)