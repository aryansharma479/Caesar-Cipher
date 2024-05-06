import random, os

from hangmanart import logo, stages

print(logo)

word_list = []
wordslen = int(input('Enter How Many Words You Want To Enter: '))
for words in range(wordslen):
    word = input("Enter Word: ").lower()
    word_list.append(word)
os.system('clear')
chosen_word = random.choice(word_list)
word_len = len(chosen_word)
lives = 6
#guess letter
print(f"The Chosen Word Is : ", chosen_word)
display = []
for blank in chosen_word:
    display += "_"
print(display)
end_of_game = False
while not end_of_game:
    guess = input('Guess A Letter: ').lower()
    if guess not in chosen_word:
        lives -= 1

        print(f"You Guessed {guess}, That's Not In The Word. You Lost A Life")
        if lives == 0:
            end_of_game = True
            print("You Lost The Game !")
    if guess in display:
        print(f"You Already Guessed {guess}")

    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print(f"You Win!")

    print(stages[lives])  #printing hangman art
