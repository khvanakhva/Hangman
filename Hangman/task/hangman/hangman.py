import random

print("H A N G M A N")

while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')

    if menu == "exit":
        exit()
    elif menu == 'play':
        word_list = ['python', 'java', 'kotlin', 'javascript']
        secret_word = random.choice(word_list)
        guessed_word = list("-" * len(secret_word))
        named_letters = set()
        mistakes = 0

        while mistakes != 8:
            print()
            print(''.join(guessed_word))
            if secret_word == ''.join(guessed_word):
                print("""You guessed the word!\nYou survived!""")
                break

            letter = input("Input a letter: ")

            if letter in named_letters:
                print('You already typed this letter')
                continue
            elif len(letter) != 1:
                print('You should print a single letter')
                continue
            elif not letter.isalpha() or not letter.islower():
                print('It is not an ASCII lowercase letter')
                continue

            if letter in secret_word:
                for j in range(len(secret_word)):
                    if secret_word[j] == letter:
                        guessed_word[j] = letter
            else:
              print('No such letter in the word')
              mistakes += 1
            named_letters.add(letter)
        else:
            print('You are hanged!')