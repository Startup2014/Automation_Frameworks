__author__ = 'swati_dhoke'

class test_class: # define class

	class_variable = "globalvarible_dummy"

	print "----class is defined----", class_variable

	def __init__(self, name, age):
		print "----class is defined----", self.class_variable
		self.name = name
		self.age = age
