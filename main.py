#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word= random.choice(word_list)

#making hidden word in shape of _ _ _ _ _ _ 
number_of_letters=len(chosen_word)
hidden=list()
for i in range(0,number_of_letters):
  hidden.append("_")
print(hidden)
print(number_of_letters)
chosen_word.split()
print(chosen_word)


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess=input("Choose the letter: \n")
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
aim=0
for n in range(0,number_of_letters):
  if chosen_word[n]==guess:
    hidden[n]=guess
    aim+=1



unhidden=""
for i in range(0, number_of_letters):
  unhidden+=hidden[i]+" "
print(unhidden)

