__author__ = 'swati_dhoke'

import math
class reverse_string:
	test_str = list('AAkashS')
	test_reverse_string = ""

	def _init_( ):
		for i in range(len(self.test_str) , 0, -1):
			print self.test_str[i-1]
			self.test_reverse_string = self.test_reverse_string + self.test_str[i-1]
		print self.test_reverse_string

	# ## second
	#
	def _reverse_string_2_(self):
		for i in range(len(self.test_str)):
			j = len(self.test_str)-1-i
			print j
			test_reverse_string = test_reverse_string + self.test_str[j]

		print  test_reverse_string


	## Swap char
	def reverse_string3(self):

		print "------IN reverse_string3----"
		for i in range(len(self.test_str)/2):
			temp = self.test_str[i]
			self.test_str[i] = self.test_str[(len(self.test_str)-1-i)]
			self.test_str[(len(self.test_str)-1-i)] = temp

		print ''.join(self.test_str)



### Calling a class ######
def Main():
	class_intializaton  = reverse_string()

	print class_intializaton.test_str

	class_intializaton.reverse_string3()

if __name__ ==  '__main__':
	Main()
