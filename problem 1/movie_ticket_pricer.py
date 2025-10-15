print(f'--- Movie Ticket Pricer ---')
age = int(input('Please enter your age: '))
if age <= 12:
    print(f"You fall into the `Children` category.")
    print(f'Your ticket price is: $8')
elif 13 >= age >= 64:
    print(f'You fal into the `Adult` category.')
    print(f'Your ticket price is: $15')
else:
    print(f'Yu fall into the `Seniors` category.')
    print(f'Your ticket price is: $10')