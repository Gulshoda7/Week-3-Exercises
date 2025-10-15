# --- Example 5: The while Loop ---
# print("\n--- T-Minus Countdown ---")

# counter = 5

# while counter > 0:
#     print(f"{counter}...")
#     # IMPORTANT: Update the loop variable to avoid an infinite loop.
#     counter = counter - 1  # or counter -= 1

# print("Blast off!")\

counter = 16
while counter > 0:
    print(f'{counter}')
    counter /= 2

print('okay!')