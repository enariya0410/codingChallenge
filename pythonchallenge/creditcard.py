import re

def is_valid_credit_card(card_number):
    # Regular expression pattern to check if the card number is valid
    pattern = r'^(4|5|6)\d{3}(-?\d{4}){3}$'
    repeat_pattern = r'(\d)\1{3,}'
    
    # Check if the credit card number matches the pattern and does not have consecutive repeated digits
    if re.match(pattern, card_number) and not re.search(repeat_pattern, card_number.replace('-', '')):
        return True
    else:
        return False

# Get the number of credit card numbers as input
n = int(input())

# Get the credit card numbers as input
credit_card_numbers = []
for _ in range(n):
    card_number = input()
    credit_card_numbers.append(card_number)

# Validate and print the results
for card_number in credit_card_numbers:
    if is_valid_credit_card(card_number):
        print("Valid")
    else:
        print("Invalid")