import itertools
# Define the letters involved in Problem
letters = 'SENDMORY'
# Define a Range for all set of digit combinations (0-9)
digits = range(10)
solution=False # Solution by default is set to False,if found then will set to be True

# Since S and M cannot be zero, we can exclude 0 from the permutations for those from (0 to 9-1=8)
for range in itertools.permutations(digits, 8):
    # Create a mapping of letters to digits
    letter_to_digit = dict(zip(letters, range))
    
    # Check if the leading digits are not zero
    if letter_to_digit['S'] == 0 or letter_to_digit['M'] == 0:
        continue

    # Convert SEND, MORE, and MONEY from letters to digits
    send = 1000 * letter_to_digit['S'] + 100 * letter_to_digit['E'] + 10 * letter_to_digit['N'] + letter_to_digit['D']
    more = 1000 * letter_to_digit['M'] + 100 * letter_to_digit['O'] + 10 * letter_to_digit['R'] + letter_to_digit['E']
    money = 10000 * letter_to_digit['M'] + 1000 * letter_to_digit['O'] + 100 * letter_to_digit['N'] + 10 * letter_to_digit['E'] + letter_to_digit['Y']
    
    # Check if the equation SEND + MORE == MONEY holds
    if send + more == money:
        solution=True
        print("Solution found.")
        print(f"SEND: {send}")
        print(f"MORE: {more}")
        print(f"MONEY: {money}")
        print(f"Mapping: \n{letter_to_digit}")
        print(f"Verification: {send} + {more} = {money}")
        break
if not solution:
    print("No solution found.")