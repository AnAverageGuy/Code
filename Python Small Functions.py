def findFirstRepeatedOccurrence(string):
	temp = []
	for char in string:
		if char in temp:
			return char
		else:
			temp = temp + [char]

# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
def sleep_in(weekday, vacation):
  if not(weekday) or (vacation):
    return True
  else:
    return False
	
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. 
# We are in trouble if they are both smiling or if neither of them is smiling. 
# Return True if we are in trouble.
def monkey_trouble(a_smile, b_smile):
  if (a_smile and b_smile) or (not a_smile and not b_smile):
    return True
  else:
    return False


# Given two int values, return their sum. Unless the two values are the same, then return double their sum.
def sum_double(a, b):
	if a == b:
		return (a + b) * 2
	else:
		return a + b
	
	
# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
def diff21(n):
	if n > 21:
		return 2 * abs(21 - n)
	else:
		return abs(21 - n)
	
# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. 
# Return True if we are in trouble.
	
def parrot_trouble(talking, hour):
  if talking:
    if (hour < 7) or (hour > 20):
      return True
    else:
      return False
  else:
    return False
	
def absoluteValue(n):
	return n * ((n>0) - (n<0))
	
	
# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
def makes10(a, b):
	if (a == 10) or (b == 10):
		return True
	elif (a + b) == 10:
		return True
	else:
		return False
	
# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
def near_hundred(n):
	if n < 0:
		return False
	diff = abs(100 - n)
	if diff <= 10:
		return True
	diff = abs(200 - n)
	if diff <= 10:
		return True
	return False

# Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if both are negative.
def pos_neg(a, b, negative):
	if negative:
		if (a < 0) and (b < 0):
			return True
	else:
		if (a > 0) and (b < 0):
			return True
		if (a < 0) and (b > 0):
			return True
	return False
  
 # Given a string, return a new string where "not " has been added to the front. 
 # However, if the string already begins with "not", return the string unchanged. 
def not_string(str):
	if "not" in str[:4]:
		return str
	else:
		return "not " + str
# Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
# The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
def missing_char(str, n):
	return str[:n] + str[n+1:]
	
# Given a string, return a new string where the first and last chars have been exchanged.	
def front_back(str):
	if len(str) == 1:
		return str
	return str[len(str)-1:]  + str[1:len(str)-1] + str[:1]
	
# Given a string, we'll say that the front is the first 3 chars of the string. 
# If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
def front3(str):
	if len(str) < 3:
		return str + str + str
	return str[:3] + str[:3] + str[:3]

# Return n copies of the front	
 def front_times(str, n):
  return str[:3]*n		
  
# Given a string and a non-negative int n, return a larger string that is n copies of the original string.		
 def string_times(str, n):
  return str*n
 
# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
	skip = False
	result = ""
	for char in str:
		if skip:
			skip = False
    else:
      result += char
      skip = True
  return result

# Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
	i = 0
	result = ""
	for char in str:
		result += str[:i]
		i += 1
	return result + str 
	
# Given a string, return the count of the number of times that a substring length 2 appears in the string
# and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).	
def last2(str):
	count = 0
	sub = str[len(str)-2:len(str)]
	prev = ""
	for char in str:
		if (prev + char) == sub:
			count += 1
		prev = char
	count -= 1
	if count < 0:
		count = 0
	return count
	
# Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
	count = 0
	for num in nums:
		if num == 9:
			count += 1
	return count

# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.	
def array_front9(nums):
	i = 0
	for num in nums:
		if i < 4:
			if num == 9:
				return True
		i += 1
	return False
