def palindrome_using_reverse_string(str): 
    print ('when string reverse is same as string its a plaindrome')
    return str==str[::-1]
       
def palindrome_using_index(str):
    print ('when string reverse is same as string its a plaindrome') 
    str_list = list(str)
    isPalindrome =True
    for letter in str_list:
        if letter ==  str_list[-1]:
            str_list.pop(-1)
            print (str_list[-1])
        else:
            isPalindrome= False
            break 
    return isPalindrome
## if you are editing the the list dont loop across list length

def is_Anagram(str1, str2):
    print("Anagram is word made from shuffling of char")
    from collections import Counter
    return (Counter(str1) == Counter(str2))
    
def isAnagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()
    return (str1_list == str2_list)

def find_anagrams(x):
    import collections
    anagrams = [''.join(sorted(list(i))) for i in x]
    print(anagrams)
    anagrams_counts = [item for item, count in collections.Counter(anagrams).items()       if count > 1]
    print(anagrams_counts)
    return [i for i in x if ''.join(sorted(list(i))) in anagrams_counts]

def rotate_array(arr, k):
    """  
    #Given an array, rotate the array to the right by k steps, where k is non-negative.
    """
    arr[:] = (arr[len(arr)-k:])+(arr[:len(arr)-k])

def duplicate_in_array(s):
    """
    Given an array, find the first duplicate elements index
    """
    import collections
    c = collections.Counter(s)
    for x in s:
        if c[x]>1:
            return s.index(x)
    return -1

def remove_dup_sorted_array(arr):
    import collections
    c = collections.Counter(arr)
    for x in arr:
        if c[x]>1:
            arr.remove(x)
    return arr
    
def first_unique_char(s):
    """
    write a function that would return the first non repeating character in a string. 
    So “Total” would return 0.
    """
    order = []
    counts = {}
    for x in s:
        if x in counts:
          counts[x] += 1
        else:
          counts[x] = 1 
          order.append(x)
    for x in order:
        if counts[x] == 1:
          return x
    return None
    
def find_max_in_array(arr, k):
    """
    #Write an efficient program for printing k largest elements in an array. Elements  in array can be in any         order.
    """
    print(" Amazon interview question")
    arr[:] = sorted(arr)
    return ((arr[len(arr)-k]))
    
    
def isstringIs_substring(str1, str2):
    """
    Write a function that takes two strings and returns true if one string is the substring of other
    string.find("substring")  can also be used
    """
    if str1 in str2:
        return True
    else:
        False

def generate_single_sorted_array(nums1, nums2): 
    """
    # Given input as k sorted arrays, generate a single sorted list as output
    #written with assumption its sorted array with no duplicates
    """
    nums3= nums1+nums2
    # sort and add to resultant 
    # add array and sort 
    temp = 0
    print("nums3 at start %s :" %nums3)
    for x in range(len(nums3)): 
        y=x+1
        for y in range(y,len(nums3)): 
            if nums3[x]> nums3[y]:
                print("nums3 before %s :" %nums3)
                temp = nums3[x]
                nums3[x]= nums3[y]
                nums3[y]= temp
                print("nums3 after %s :" %nums3)
    return(nums3)

#Given a string, find the longest substring which is palindrome.-leet code
def second_largest_element(arr):
    if len(arr) <2:
        print("Atleast two elements are needed in array")
        return None
    largest = arr [1]
    seclargest = arr[0]
    if seclargest > largest:
       largest, seclargest = arr [0], arr [1]
    for x in range(2,len(arr)-1):
        if arr[x] > seclargest:
            if arr[x] > largest:
                seclargest ,largest  = largest,arr[x]
            else:
                seclargest = arr[x]
    return seclargest

print(is_Anagram('car', 'rac'))
test_array =[
            [20,67,3,2.6,7,74,2,2, 2,2],
            [8,90,8,52.8,4,3,2,5,7],
            [1,2,5,5],
            [0,1, 2, -1,-2, 3],
            [0],
            [-1, 1] 
            ]

# Example how to use MAP function 
print(list(map(second_largest_element, test_array)))
print(list(map(first_unique_char, test_array)))
print(list(map(duplicate_in_array, test_array)))
print(list(map(remove_dup_sorted_array, test_array)))

#This will remove all zero ('','0', 0.0, [],{},() ,False )form a list
print(list(filter(None,test_array[3])))

# Example how to use LAMBDA function 
s = lambda x: x+2
print(s(2))
string_reverese = lambda x: x[::-1]
print(string_reverese('swa'))

# Example for generators #######
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        How to find all pairs of elements in an integer array, whose sum is equal to a given number?
        """
        print("---find pair that sum %s in %s---" %(target, nums ))
        r = []
        for x in range(len(nums)-1):
            y =x+1
            for y in range(y, len(nums)): 
                print("adding %s and %s" %(nums[x], nums[y]))
                if (nums[x] +nums[y] == target):
                    yield [x, y]
        #                 r.append([x, y]) // regular way   
        # return r
        
s = twoSum(test_array[3], 3)
print(next(s))
print(next(s)) ### call number of times you want to see result

# Example for decorators

# Linked List

#Find the union of two strings
# From a given list of array (Not sorted) find the second largest value
# Find the prime numbers from the given list of array (1 -100)
#reverse s string IN PLACE
 
# String Replace
oldstring = 'I like Guru99' 
newstring = oldstring.replace('like', 'love')
print(newstring)

#Using "join" function for the string
print("Add a colon after every character in the string %s" % ":".join("Python"))    


word="guru99 career guru99"




word.replace("guru99", "test")
#Output 'test career test'

# enumerate , collection , counter , iteritem

# map lamda filter reduce

def getCountries(str, P):
    import requests, json
    URL ='https://jsonmock.hackerrank.com/api/countries/search'
    PARAMS = {'name' :str}
    response = requests.get(url=URL,params=PARAMS )
    #####post call###
    #URL= 'https://api.gemini.com/v1/order/new'
    # payload = {'name' :str}
    # post_response = requests.post(url=URL,data=payload )
    #####post call###
    resp =response.json()
    print(json.dumps(resp, indent =4))
    # print(json.dumps(resp['page'], indent =4))
    # print(json.dumps(resp['per_page'], indent =4))
    # print(json.dumps(resp['total'], indent =4))                     
    # print(json.dumps(resp['total_pages'], indent =4))
    #print(json.dumps(resp['data'], indent =4)) 

    print([x['name'] for x in resp['data']])
    response.raise_for_status()



getCountries('un', 10)

# Assumption you are in trder role assigement to run this Api



def NewOrder_client_order_id_test():
    '''
    Test with all postive values in payload
    '''
    import requests
    base_url ='https://api.gemini.com'
    url = base_url + '/v1/order/new'
    request_headers = { 'Content-Type': "text/plain",
                        'Content-Length': "0",
                        'X-GEMINI-APIKEY': api_key,
                        'X-GEMINI-PAYLOAD': base64.b64encode(encoded_payload),
                        'X-GEMINI-SIGNATURE': hmac.new(secret_key, b64, hashlib.sha384).hexdigest(),
                        'Cache-Control': "no-cache" }

    response = requests.post(url,
                             data=None,
                             headers=request_headers,
                             timeout=timeout,
                             verify=False)
    assert response.status_code == 200
    return response.content


 
    
# NewOrder_client_order_id_test()
    
# Todo:math (+ -*/ % // **)
    
# regex:http:
# //www.pyregex.com/
# https://pythex.org/
    
# binary trees, linkedlist,
# Todo:java, slenium, api modules

    
def regexpression(regex_string_email):
    return True
        
def palindrome_of_integer():
    num = int(input("enter a number: "))
    temp = num
    rev = 0
    while temp != 0:
        rev = (rev * 10) + (temp % 10)
        temp = temp // 10
        print(rev, temp)
    if num == rev:
        print("number is palindrome")
    else:
        print("number is not palindrome")

palindrome_of_integer()




