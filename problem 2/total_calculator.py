print(f'--- Running Total Calculator ---')
total = 0
print(f'Enter numbers to add them up. Type `done` to see the total.')
while True:
    number = input('Enter a number or `done`: ')
    if number == 'done':
        break
    total += float(number)

print(f'--- Final Calculation ---')
print(f'The final sum of all numbers is: {total}')
