#BOOK - learning python by mark louis

'''#even or odd
num = int(input(" Enter number: "))
if num%2==0:
	print (" Even")
else:
	print (" Odd")
'''

'''# avg of N numbers
print (" Enter your numbers, enter 'stop' when done ")
li = []
while(True):
	user_input = input(" Enter number ")
	if user_input.lower()!='stop':
		li.append(int(user_input))
	else:
		break
sum = 0
for x in li:
	sum += x
print( " Average of %d numbers is %f" % (len(li) , sum/len(li) ) )
'''

# general form of range is range(start = 0,end+1,step=1)
# range in python 3 is a generator functon

'''#enumerate
numbers = [11,22,33,44]
for i,num in enumerate(numbers):
	print(" list[%d] = %d" % (i,num) )
'''

'''#zip with same length
seq1 = [1,2,3,4]
seq2 = [11,22,33,44]
for i,j in zip(seq1,seq2):
	print("%d %d" % (i,j))
'''

'''#zip with different length
seq1 = [1,2,3,4]
seq2 = [11,22,33,44,55,66]
for i,j in zip(seq1,seq2):
	print("%d %d" % (i,j))
'''

#dictionary
a = {'name':'shivani','age':20}
print (a)