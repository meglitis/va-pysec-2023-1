text = '''Explore loops in Python and demonstrate use of them
Demonstrate use of all types of loops in Python:
•While Loop
•For Loop
•Range Loop
Make use of else statement where applicable.'''


# counting symbols ourselves, not using len()
symbol_count = 0

for symbol in text:
    symbol_count+=1

# finding first occurrence of symbol in text

first_occurrence = -1
counter = 0
search = 'a'

while counter < symbol_count:
    if text[counter] == search:
        first_occurrence = counter
        break
    counter += 1

if counter > -1:
    print('symbol ' + search + ' found at position ' + str(first_occurrence))
else:
    print('symbol ' + search + ' not found')

# while loop can be rewritten using range as counter is incremented linear

first_occurrence = -1

for counter in range(0, symbol_count):
    if text[counter] == search:
        first_occurrence = counter
        break

if counter > -1:
    print('symbol ' + search + ' found at position ' + str(first_occurrence))
else:
    print('symbol ' + search + ' not found')
