# A string variable defination

import unittest, sys

class read_write_file:

	"read line by line integer from one file and print suare of same integer in another"

	def Main():
		file_name = "Test_result.txt"
		try:
		  file = open(file_name, "r+")
		except IOError:
		  print "There was an error writing to", file_name
		for x in range(0, 12):
			file.write( str(x) +"\n" );
		linesoffile = file.readlines()
		file1 =open("outputfile.txt","w")
		for y in range(len(linesoffile)):
			file1.write( str(int(linesoffile[y].replace("\n","")) ** 2 )+"\n")
		file.close()
		file1.close()

	if __name__ == '__main__':
            Main()