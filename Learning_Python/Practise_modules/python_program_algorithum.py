__author__ = 'swati_dhoke'


import unittest
import smtplib
import random
import copy
class List_programe():

	test_string ="Swatii" ### Global Varibale
	def find_prime_number(self):
		# in a list find what number are prime and sane them to another list

		list1 =[[1, 2, 4], [7, 9, 90], [33, 3, 333]]
		#list1 =[[90, 17]]


		for i in range(len(list1)):
			for j in range(len(list1[0])):
				#print "----vale of i " ,i,"--------" ,j

				num = list1[i][j];
				isPrime = True
				#prime numbers are greater than 1
				if (num >= 0):
					#print "=======Verified that the number is positive interger====",list1[i][j]
					for x in range(2,num):
						#print "inside for loop, i is:" + str(i);
						if (num % x == 0):
							print "==== number is NOT prime, num:",num ,", x:", x
							isPrime = False
							break;
						# else:
							#print "==== number is not divisible by "+str(x)+" =========="

					# 	print "outside if"
					# print "outside for"

					if (isPrime == True):
						print "----number is prime---", num

	#list1 =[2, 233, 5,610,89 ,4181,102]
	list1=[7, 6, 5, 4, 3, 2, 1]
	def test_sort_acs_list_of_list(self, list):
		for j in range(len(list)-1):
			for i in range(len(list)-1-j):
					if (list[i] > list[i+1]):
						temp = list[i]
						list[i] =list[i+1]
						list[i+1]=temp
			print list

	def isPrime(self,list):
		for i in range(len(list)):
			for j in range(len(list[i])):
				isprime = True
				num = list[i][j]
				if(num <= 0):
					print "----number is negative:" , num
					continue
				for x in range (2, num):
				    if((num % x) == 0):
						print "number is not prime:" ,num
						isprime = False
						break
				if(isprime== True):
					print "prime num:" ,num

	def generate_fibonocci(self):
		# 1+1 =2
		# 1+2 =3
		# 2+3 =5
		# 3+5 =8
		#
		c1=1
		c2 =1
		for x in range(1, 20):
			sum =c1+c2
			c1 = c2
			c2 = sum
			print c1, ":", c2, "sum-------->" ,sum

	def unique_char_test(self):

				print test_string
				for i in range(0,len(test_string)):
					print test_string[i]
					for j in range(i+1 , len(test_string)):
						if test_string[i] == test_string[j]:
							print "not unique"
							return False
				print "unique"
				print "=================End of unique_char_test==================="
				return True


class otherSmallProg():
#	list111 = [1, 3, 6, 8, 89, 0 , -3,156464644456454564654]
	list111 = [1,156464644456454564654]

	def smtp_mailsent(self):

				SERVER = smtplib.SMTP("smtp.gmail.com")
				FROM = ["swatidhoke@gmail.com"]
				TO = ["meghadhoke.88@gmail.com"] # must be a list
				SUBJECT = "Hello! SMTP SCRIPT"
				TEXT = "This message was sent with Python's smtplib."
				# Main message
				message = """
				From: Sarah Naaz < sender@mail.com >
				To: CarreerRide user@mail.com
				Subject: SMTP email msg
				This is a test email. Acknowledge the email by responding.
				""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
				server = smtplib.SMTP(SERVER)
				server.sendmail(FROM, TO, message)
				server.quit()

	def generate_random_num(self):
				i = random.randint(1,99)# i randomly initialized by integer between range 1 & 99
				j= random.uniform(1,999)# j randomly initialized by float between range 1 & 999
				k= random.random()# k randomly initialized by float between range 0 & 1
				print("i ================:" ,i)
				print("j ================:" ,j)
				print("k ================:" ,k)

	def deep_copy(self):
		#copy.deepcopy()
		pass

	def shallow_copy(self):
		copy.copy(test_string)
		pass

	def find_even_odd(self):
		# mylist = [1,2, 3, 4, 23 , 33, 44, 55]
		mylist = [x*x for x in range(2, 100, 1)]
		print mylist


		for i in range(len(mylist)-1, -1, -1):

			print i
			if ((mylist[i] % 2)==0):

				print " even" , mylist[i]
			else:
				print "removing odd:", mylist[i]
				mylist.remove(mylist[i])
				print "after removing: ", mylist

		print mylist

	def test_find_substring(self):
		str1 = "waterbottlee"
		rotation_str = "terbottlewa"

		#use pattern matching to find substring:
	#	m = re.search(rotation_str, str1)
	#	print m.group(0)
		match = (rotation_str + rotation_str).find(str1)
		print match

		if (match == -1):
			print "Not a substring "
			return False
		return True

	def List_of_List_Matrix(self):
		mylist  = [[7, 9, 0],
	           [8, 5, 1],
	           [4, 7, 6],
	           [7, 8, 9]];
		mylist1 = copy.deepcopy(mylist)
		# m = 3;
		# n = 4;
		for i in range(len(mylist)):
			for j in range(len(mylist[0])):
				if (mylist[i][j] ==0):

					for x in range(len(mylist)):
						print "-------test-----", mylist[x][j]
						mylist1[x][j] =0

					for y in range(len(mylist[0])):
						print "-------test-----", mylist[x][j]
						mylist1[i][y] =0

		print "============",mylist1

	def Remove_duplicate_char(self):
		dup_test =list("AAAAAAA")

		dup_test_new =list ("")
		for i in range (len(dup_test)):
			Flag = False
			for j in range(i+1,len(dup_test)):
				print  dup_test[i] ,"==========", dup_test[j]
				if(dup_test[i]==dup_test[j]):

					Flag = True

			if (Flag == False):
				print"--------Appending-----------" +dup_test[i]
				dup_test_new.append(dup_test[i])
		###Test cases
		# null
		# numeric
		# Alplha number
		# extra space
		# special charter
		# duplicate

		print dup_test_new

	def anagram(self):
		#Write a method to decide if two strings are anagrams or not

		Str1=  list("SWATI")
		Str2 = list("WAIST")
		# compare lengh

		if (len(Str1) != len(Str2)):
			print"lengh of string is not same"
			exit(0)
		# compare char
		for i in range(len(Str1)):

			for j in range(len(Str2)):

				if Str1[i] == Str2[j]:
					Str2.pop(j)
					break;
		if (len(Str2) == 0) :
			print("=====IT'S ANAGRAM====") ,Str2

# L = List_programe();
# L.generate_fibonocci()



#generate_fibonocci()
#sort_acs_list_of_list(list1)
#print "output is:" + str(isPrime(list1))
#find_prime_number()
#sort_acs_list_of_list()

	def find_min_dis(self):
		minm = (self.list111[0]-self.list111[1]);
		if (minm <0)  :
			minm  = -(minm)
		for x in range(len(self.list111)):
			for y in range (x+1 , len(self.list111)):
				diff = (self.list111[x]-self.list111[y])
				if (diff <0)  :
					diff  = -(diff)
				if ((diff>0) and (minm >diff)):
					minm  = diff
		print minm

S = otherSmallProg();
S.find_min_dis()


if __name__ == '__main__':
    ''' Add test cases in suite to keep the order of running'''
    from xmlrunner import XMLTestRunner
    import HTMLTestRunner
    suite1 = unittest.TestLoader().loadTestsFromTestCase(List_programe)
    suite = unittest.TestSuite([suite1])
    unittest.main(testRunner=XMLTestRunner()).run(suite)
    HTMLTestRunner.main()





























