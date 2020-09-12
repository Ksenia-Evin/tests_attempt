import random

WORDS = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
tries = 4

def get_word():
    word = random.choice(WORDS)
    return word.lower()


def play(word, tries):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []

    print("Let's play Hangman!")
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        try:
            guess = input("Please, guess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You have already guessed the letter", guess)
                elif guess not in word:
                    print(guess, "is not in the word")
                    tries -= 1
                    guessed_letters.append(guess)
                else: 
                    print("Good job", guess, "is in the word!")
                    guessed_letters.append(guess)
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "_" not in word_completion:
                        guessed = True
            else: 
                raise ValueError
                print("Not a valid guess!")
        except(Exception) as e:
            raise ValueError
        print(word_completion)
        print("\n")
    if guessed: 
        print("Congrats! You guessed the word! You Win!")
    else:
        print("Sorry, you are out of tries. The word was " + word)
        return False

def main():
    word = get_word()
    play(word, tries)
    while input("Are you want to play again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word, tries)


if __name__ == "__main__":
    main()