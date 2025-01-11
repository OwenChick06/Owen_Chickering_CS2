import random #imports random library
 
words = ["computer", "hangman", "code", "python", "dictionary", "library", "string", "list"] #This is the list of words used in the hangman game
frame = 0 #Sets the picture to 1

randword = list(random.choice(words)) #Picks a random word from the words list
blank = "" 
for letter in randword: #For every letter in random word
    blank += "_" #Every blank spot is a dash
dash_word = list(blank) #Sets word to dashed word
 
pics = [''' 
  +---+
  |   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
========='''] #List of hangman pictures (7 in total)

print(pics[frame]) #Prints the picture for the first turn

print(blank) #Prints dashed out word
guess = input("Make a guess? ") #Askes the user for a guess

step = 0
correct_guess = False
for letter in randword:#For every letter in random word
    if guess.lower() == randword[step]: #If guess is equal to a letter in the word
        dash_word[step] = guess.lower()
        correct_guess = True# Correct guess
    step += 1 #Retests for the next blank
if correct_guess == False: #If guess is wrong
    print(f"That letter is not in the word") 
    frame += 1 #Switches to next image
print(pics[frame]) #Print image 
print(''.join(dash_word)) #Prints updated dash word (Neatly)

while frame < 6: #Before the last image
    if dash_word == randword: #If every blank spot is filled
        print("You Win")
        break #stops code
    guess = input("Make another guess? ")
    
    step = 0
    correct_guess = False
    for letter in randword: #For every letter in random word
        if guess.lower() == randword[step]: #If guess is equal to a letter in the word
            dash_word[step] = guess.lower() 
            correct_guess = True #Correct guess
        step += 1 #Retests for the next blank
    if correct_guess == False: #If answer is false
        print("That letter is not in the word")
        frame += 1 #Switches to next image
    print(pics[frame]) #Print image
    print(''.join(dash_word)) #Prints updated dash word (Neatly)

if frame == 6: #If frame is on the 7th image
    print("You Lose") 