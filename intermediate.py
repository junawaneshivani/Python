
# a comma seperated list of objects is identified by python as a tuple

def compute(a,b,operation='sum'):
	if operation == 'sum' :
		return a + b
	elif operation == 'difference' :
		return a - b
	elif operation == 'product' :
		return a * b
	elif operation == 'division' :
		return a / b;
	else:	
		return " Undefined operaton"
	
#*arg = tuple
#**arg = dict 

def highly_flexible(*args , **dargs):
	print (args)
	print (dargs)
	
highly_flexible(1,2,3,{'name':'shivani','age':20})