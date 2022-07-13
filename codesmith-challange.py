# // If you're having trouble, use lines 12-14 for expected inputs and outputs
from asyncio.windows_events import NULL
from queue import Empty


CONST_PHONEBOOK = {};
CONST_NAMES = ['Mira', 'Royce', 'Kathie'];
CONST_NUMBERS = ['3234958675', '9164059384', '4154958675']

# // Write your code below this line
for name in CONST_NAMES:
    print(name)
    if CONST_PHONEBOOK is Empty:
        CONST_PHONEBOOK = name
    else:
        CONST_PHONEBOOK += name



# //Uncomment the lines below to test your code
