# This Program demonstrates List Comprehensions in Python


# We will invoke this function to cube numbers
def cube(n):
	return n**3

# Let us start by creating a list of numbers 1..10
originalList = range(1,11)
print ("Original (Starting) list of numbers (1 to 10)")
for x in originalList:
	print (x)

# Let us generate the cubes of 1..10 using the simple, standard for loop

print ("Displaying the Cubes of 1..10 using the standard for-loop notation")
for i in range(1,11):
	print(cube(i))

# Now let us use List Comprehensions to generate the cubes
print ("Displaying the cubes by using List Comprehensions")
cubesUsingListComprehensions = [cube(x) for x in originalList]
print (cubesUsingListComprehensions)