def display_clue(word, guessed_letters):
    
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def main():
    word_to_guess = "EVAPORATE"
    guessed_letters = set()
    
    print("Welcome to Hangman!")
    
    while True:
        clue = display_clue(word_to_guess, guessed_letters)
        print(clue)
        
        if '_' not in clue:
            print("Congratulations! You've guessed the word correctly!")
            break

        guess = input("Guess your letter: ").upper()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in word_to_guess:
            print("Incorrect!")
    
if __name__ == "__main__":
    main()
