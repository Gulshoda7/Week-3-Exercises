print(f'\n*** THE FIBONACCI SEQUENCE GENERATOR ***\n')
n=int(input('How many numbers do you want to show? '))
a=0
b=1
counter=0
while counter < n:
    print(f'{a}', end=' ')
    next_number = a + b
    a = b
    b = next_number
    counter += 1