import random

def generate_number():
    """Generates a random 4-digit number with unique digits."""
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))

def count_cows_and_bulls(secret, guess):
    """Counts the number of cows and bulls in the guess compared to the secret."""
    cows = sum(s == g for s, g in zip(secret, guess))
    bulls = sum(min(secret.count(g), guess.count(g)) for g in set(guess)) - cows
    return cows, bulls

def main():
    secret_number = generate_number()
    guess_count = 0
    
    print("Welcome to the Cows and Bulls Game!")
    
    while True:
        guess = input("Enter a 4-digit number: ")
        
        # Validate guess
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a 4-digit number.")
            continue
        
        guess_count += 1
        cows, bulls = count_cows_and_bulls(secret_number, guess)
        
        if cows == 4:
            print(f"Congratulations! You've guessed the number {secret_number} in {guess_count} guesses.")
            break
        else:
            print(f"{cows} cow(s), {bulls} bull(s)")

if __name__ == "__main__":
    main()
