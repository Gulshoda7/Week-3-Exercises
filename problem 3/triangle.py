print(f'--- Triangle Pattern Printer ---')
height = int(input(f'Enter the desired height of the triangle: '))
for h in range(height):
    for j in range(h+1):
        print(f'*', end=' ' )

    print()
