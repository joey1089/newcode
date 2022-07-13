# // If you're having trouble, use lines 12-14 for expected inputs and outputs
CONST_PHONEBOOK = {};
CONST_NAMES = ['Mira', 'Royce', 'Kathie'];
CONST_NUMBERS = ['3234958675', '9164059384', '4154958675']

# // Write your code below this line
for name,numbers in zip(CONST_NAMES,CONST_NUMBERS):
    CONST_PHONEBOOK[name] = numbers

print(CONST_PHONEBOOK)


# //Uncomment the lines below to test your code
print(CONST_PHONEBOOK['Mira'])
print(CONST_PHONEBOOK['Royce'])
print(CONST_PHONEBOOK['Kathie'])

