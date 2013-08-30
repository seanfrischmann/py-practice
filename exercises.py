# Practice with printing strings and Variables

print ('\nWelcome to Python\n')

# Exercise 2.3

width = 17
height = 12.0
delimiter = '.'

print width/2
print 8
print height/3
print 4.0
print 1+2*5
print 11
print delimiter*5
print '.....'

# Exercise 3.3

print ('\n')

def right_justify(s):
	length = 70 - len(s)
	space = ' ' * length
	print (space + s)

right_justify('Sean')

# Exercise 3.4

print ('\n')

def twice(f,s):
	f(s)
	f(s)

def show(s):
	print s 

twice(show, 'Gabe')

# Exercise 3.5

print ('\n')

def four(s):
	print s
	print s
	print s
	print s

def grid():
	dashes = ' -' * 4
	plus = '+' + dashes + ' +' + dashes + ' +'
	spaces = ' ' * 8
	line = '|' + spaces + ' |' + spaces + ' |'
	print plus
	four(line)
	print plus
	four(line)
	print plus	

grid()

# Exercise 

print ('\n')

name = raw_input('\nWhat is your name?\n')

print ('\nWelcome ' + name + ', to where dreams come true!')

def anythingIsPossible_response():
	anythingIsPossible = raw_input('\nDid you know anything is possible!?\n')
	if anythingIsPossible == 'yes':
		print ('\nThe journey starts here!')
	elif anythingIsPossible == 'no':
		print ('\nWell ' + name + ', the world is at your fingertips!')
	else:
		print ('\nPlease enter a simple yes or no.')
		anythingIsPossible_response()

anythingIsPossible_response()

# Exercise 5.1

print ('\n')

def check_fermat(a, b, c, n):
	if a**n + b**n == c**n:
		if n > 2:
			print ('Holy smokes, Fermat was wrong!')
		else:
			print ('Femat is correct.')
	else:
		print("No, that doesn't work")

def prompt_fermat():
	print ('Please enter a value for:')
	a = raw_input('a=')
	b = raw_input('b=')
	c = raw_input('c=')
	n = raw_input('n=')
	print ('If your value for n was greater than two than according to Fermat, a^n + b^n should not equal c^n.\n Let us see if it works!')
	check_fermat(int(a), int(b), int(c), int(n))

prompt_fermat()

# Exercise 5.2

print ('\n')

def is_triangle(a, b, c):
	if a + b < c:
		print ("\nNo, that doesn't work\n")
	elif a + c < b:
		print ("\nNo, that doesn't work\n")
	elif b + c < a:
		print ("\nNo, that doesn't work\n")
	else:
		print ('\nHoOrAy, that makes a triangle!\n')

def prompt_triangle():
	print ('\nPlease enter a value for:')
	a = raw_input('a=')
	b = raw_input('b=')
	c = raw_input('c=')
	print ('\nIf any of the three lengths are greater than the two, there is no triangle.\n Let us see if this is true with the number you entered!')
	try:
		is_triangle(int(a), int(b), int(c)) 	
	except:
		print ('\nPlease make sure you enter a number value for each')
		prompt_triangle()

prompt_triangle()



