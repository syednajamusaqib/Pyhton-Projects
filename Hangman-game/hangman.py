import random
f = open("word.txt",'r')
data = f.readline()
# This will create a list of all words present in words.txt file
words = data.split()
word = random.choice(words).upper()


total_chances = 8
guesses_word = "_"*len(word)
print(guesses_word)
while total_chances!=0:
    letter = input("Enter a letter: ").upper()

    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guesses_word = guesses_word[:index]+letter+guesses_word[index+1:]
                print(guesses_word)
        if guesses_word == word:
            print("Congrats! You Guessed it Right!!")
            break
    else:
        total_chances -= 1
        print("Incorrect Guess")
        print(f"Remaining chances are {total_chances}")
else:
    print("You lost!!")
print(f"Correct word is {word}")

