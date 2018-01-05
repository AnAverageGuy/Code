# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
def hello_name(name):
  return "Hello " + name +"!"

# Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
def make_abba(a, b):
  return a+b+b+a

# Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"

# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>". 
def make_out_word(out, word):
  return out[:2] + word + out[2:]

# Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
def extra_end(str):
  return str[len(str)-2:]*3

# Given a string, return the string made of its first two chars, so the String "Hello" yields "He".
def first_two(str):
  if len(str) < 2:
    return str
  else:
    return str[:2]

# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
def first_half(str):
  return str[:len(str)/2]

# Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
def without_end(str):
  return str[1:len(str)-1]

# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. 
# The strings will not be the same length, but they may be empty (length 0).
def combo_string(a, b):
  if len(a) < len(b):
    return a+b+a
  else:
    return b+a+b

# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
def non_start(a, b):
  return a[1:]+b[1:]

# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.
def left2(str):
  return str[2:]+str[:2]
  
############## 

# Given a string, return a string where for every char in the original, there are two chars.
def double_char(str):
  returnStr = ""
  for char in str:
    returnStr = returnStr + char*2
  return returnStr
  
# Return the number of times that the string "hi" appears anywhere in the given string.
def count_hi(str):
  count = 0
  prev = ""
  for char in str:
    if (prev+char) == "hi":
      count+=1
    prev = char
  return count

# Return True if the string "cat" and "dog" appear the same number of times in the given string.
def cat_dog(str):
  if len(str) < 3:
    return True
  catCount = 0
  dogCount = 0
  i = 0
  j = 3
  while True:
    if str[i:j] == "cat":
      catCount+=1
    if str[i:j] == "dog":
      dogCount+=1  
    if j == len(str):
      break
    i+=1
    j+=1

  if catCount == dogCount:
    return True
  else:
    return False
	
# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd',
# so "cope" and "cooe" count.
def count_code(str):
  if len(str) < 4:
    return 0
  i = 0
  j = 2
  k = 3
  l = 4
  count = 0
  while True:
    if (str[i:j]+str[k:l]) == "coe":
      count+=1
    if l == len(str):
      break
    i+=1
    j+=1
    k+=1
    l+=1
  return count

# Given two strings, return True if either of the strings appears at the very end of the other string, 
# ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").  
  
def end_other(a, b):
  if len(a) < len(b):
    if b[len(b)-len(a):].lower() == a.lower():
      return True
    else:
      return False
  else:
    if a[len(a)-len(b):].lower() == b.lower():
      return True    
    else:
      return False
  
# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period
# (.). So "xxyz" counts but "x.xyz" does not.  
def xyz_there(str):
  if len(str) < 3:
    return False
  elif len(str) == 3:
    if str == "xyz":
      return True
    else:
      return False
  
  i = 0
  dotFlag = 0
  
  while True:
    if str[i:i+1] == ".":
      i+=1
      dotFlag = 1
    if str[i:i+3] == "xyz" and dotFlag == 0: 
      return True
    if dotFlag == 1:
      dotFlag = 0
    if i == len(str):
      break
    i+=1
  return False  
  