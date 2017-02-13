a = 5				# integer
b = 2.0				# float

print (" 5 + 2 = " , 5+2)			# by default ends with new line
print (" 5 - 2 = " , 5-2)
print (" 5 * 2 = " , 5*2)
print (" 5 / 2 = " , 5/2)
print (" 5 // 2 = " , 5//2)
print (" 5 ** 2 = " , 5**2)
print (" 5 % 2 = " , 5%2)

print ("Hello", "World" , sep = '|')		#separation done by | instead of spaces
print ("Hello", end="|")						#end line with | instead of '\n'
print ("World")

# one way to check type of variables
print (type(a))
print (type(b))

# u can also typecast 
print (float(a))

# 3 methods of declaring strings
str1 = "shivani"
str2 = 'shivani'
str3 = '''shivani
junawane'''
		
print (str1)
print (str2)
print (str3)

# %6.3 f ==> 6 = total digits, 3 = digits after dot
result1 = 26.234378
result2 = 2.42

print ('%6.3f' % result1)
print ('%6.3f' % result2)

print ( '{1:6.3f} ,  {0:6.3f}'.format(result1,result2) )

a = "hello world"
print(a[::-1])			# reverse of string
print(a[1:4])			# excluding index 4
