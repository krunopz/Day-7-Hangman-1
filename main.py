#Step 1 
import random
import art
import words
import rijeci
from replit import clear

print(art.logo)

choice=int(input("If you like to continue on English press 1. \n Ako želite nastaviti na hrvatskom pritisnite 2. \n"))


if choice==1:
  print("\n Welcome to D game! The aim is to guess all the letters before you loose all of your lives. Don't left the man hanging!")
  word_list = words.word_list

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
  chosen_word= random.choice(word_list)

#making hidden word in shape of _ _ _ _ _ _ 
  number_of_letters=len(chosen_word)
  hidden=list()
  for i in range(0,number_of_letters):
    hidden.append("_")
  #print(hidden)
  #print(number_of_letters)
  chosen_word.split()
  #print(chosen_word)


  aim=0
  end=0
  dead=0
  print(art.stages[6])
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
  while end!=number_of_letters and dead!=6:
    end=0
    guess=input("Which letter would You like to try: \n").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    clear()  #clear the screen (imported from replit in preambula)
    for n in range(0,number_of_letters):
      if chosen_word[n]==guess:
        hidden[n]=guess
        aim+=1
    #print(f"aim={aim}")
#TODO 5 If wrong choice:
    if aim==0:
      print("You missed the letter!")
      dead+=1
    aim=0
    #print(f"aim={aim}")
    #print(f"dead={dead}")
    print(art.stages[6-dead])
 
    unhidden=""
    for i in range(0, number_of_letters):
      unhidden+=hidden[i]+" "
    print(unhidden)
#TODO 4 Check if the user guessed all the letters:
    for n in range(0,number_of_letters):
      if hidden[n]!="_":
        end+=1
    print(end)


  if end==number_of_letters:
    print("You WON!")
  elif dead==6:
    print(f"You're DEAD! The word was {chosen_word}")


#____________________________________________________________
# --------------- OVO JE HRVATSKA VERZIJA--------------------
#_______________________________________________________________________
else:
  print("\n Dobro došli u igru! Cilj igre je pogoditi sva slova u skrivenoj riječi prije nego nacrtate cijelog čovjeka. Svaki put kada pogriješite bit će nacrtan još jedan dio čovjeka. Imate pravo na samo 6 grešaka. Nemojte ostaviti čovjeka da visi!")
word_list = rijeci.word_list

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word= random.choice(word_list)
clear()
#making hidden word in shape of _ _ _ _ _ _ 
number_of_letters=len(chosen_word)
hidden=list()
for i in range(0,number_of_letters):
  hidden.append("_")
#print(hidden)
#print(number_of_letters)
chosen_word.split()
#print(chosen_word)


aim=0
end=0
dead=0
print(art.stages[6])
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while end!=number_of_letters and dead!=6:
  end=0
  guess=input("S kojim slovom želite pokušati: \n").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

  for n in range(0,number_of_letters):
    if chosen_word[n]==guess:
      hidden[n]=guess
      aim+=1
  #print(f"aim={aim}")
#TODO 5 If wrong choice:
  if aim==0:
    print("Nema toga slova u riječi!")
    dead+=1
  aim=0
  #print(f"aim={aim}")
  #print(f"dead={dead}")
  print(art.stages[6-dead])
 
  unhidden=""
  for i in range(0, number_of_letters):
    unhidden+=hidden[i]+" "
  print(unhidden)
#TODO 4 Check if the user guessed all the letters:
  for n in range(0,number_of_letters):
    if hidden[n]!="_":
      end+=1
  print(end)


if end==number_of_letters:
  print("POBIJEDA!")
elif dead==6:
  print(f"K vrapcu! Čovjek je predugo visio. Skrivena riječ je bila  {chosen_word.upper()}")
