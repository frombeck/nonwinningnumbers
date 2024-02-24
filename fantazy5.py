import random

def generate_non_winning_fantasy_lotto():
    max_range = 40  # Maximum range for the fantasy lotto numbers
    num_numbers = 5  # Number of fantasy lotto numbers to generate

    numbers = set()

    while len(numbers) < num_numbers:
        random_number = random.randint(1, max_range)
        numbers.add(random_number)

    return sorted(numbers)

non_winning_numbers = generate_non_winning_fantasy_lotto()
print("Non-Winning Fantasy Lotto Numbers:", non_winning_numbers)
