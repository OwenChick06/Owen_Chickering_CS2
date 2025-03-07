'''
Owen Chickering
Whats in a name
Help:Harrison Servedia
'''

import random

def get_name_input():
    '''
    Takes in name, only returns name if it does not contain numbers
    '''

    while True:
        user_input = input("Enter your name ")
        if all(char.isalpha() or char in ' -!@#$%^&*()_+={}|[]:;,.<>?/~' for char in user_input):
            return user_input
        else:
            print("Invalid input")

origname = get_name_input()  
name = origname.split(" ")
names = str(origname)

def firstname(name):
    '''
    Takes in name, returns first name  
    '''
    return(name[0])   

def reversename(origname):
    '''
    Takes in name, returns the reversed name
    '''
    stringlength=len(origname) 
    reversed_name=origname[stringlength::-1]
    return(reversed_name)

def middlename(name):
    '''
    Takes in the name, and removes the first and last name (if applicable) and returns the middle name or false
    '''
    num_names = len(name)
    if num_names >= 3:
        middle_name = name[1:-1]
        return middle_name

def lastname(name):
    '''
    Takes in name, and only returns the last name
    '''
    length = len(name)
    return(name[length-1])

def scramble(name):
    '''
    Takes in name, and scrambles it twice (it breaks when i only do once)
    '''
    random.shuffle(name)  
    newname = ''.join(name)
    random.shuffle(newname)
    return ''.join(newname)

def vowels(names):
    '''
    Takes in name, and cycles through the letters to find vowels
    '''
    vowels = "aeiouAEIOU"
    count = len([char for char in names if char in vowels])
    return count

def consonant(origname):
    '''
    Takes in word, and counts the frequency of each consinant
    '''
    notallowed = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U", " "] 
    chars = []
    for i in origname:
        if i not in notallowed:
            chars.append(i)
    newname = "".join(chars)
    iteration = {}
    for c in newname:
        if c in iteration:
            iteration[c] += 1
        else:
            iteration[c] = 1
    return iteration

def lowecase(origname):
    '''
    Takes in word, and cycles through converting uppercase to lowercase
    '''
    result_string = ''
    for char in origname:
        if 'A' <= char <= 'Z':
            result_string += chr(ord(char) + 32)
        else:
            result_string += char
    return result_string

def uppercase(origname):
    '''
    Takes in word, and cycles through converting lowercase to uppercase
    '''
    result = ''
    for char in origname:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def booleancheck(origname):
    '''
    Takes in word, checks for dash, and returns true or false
    '''
    if "-" in origname:
        result = True
    else:
        result = False
    return result

def shuffleword(origname):
    '''
    Takes in word, shuffles the characters, and rejoins them and returns shuffled word
    '''
    characters = list(origname)
    random.shuffle(characters)
    return ''.join(characters)

def initials(origname):
    '''
    Takes in word, splits it, and returns the first letter of each word
    '''
    intial = (origname)
    namelist = intial.split()
    initials = ""
    for letter in namelist:  
        initials += letter[0]
    return initials

def display_menu():
    '''
    Prints menu to selct function
    '''
    print("\nSelect an option:")
    print("1. First Name")
    print("2. Middle Name")
    print("3. Last Name")
    print("4. Reversed Name")
    print("5. Vowels Count")
    print("6. Consonant Frequency")
    print("7. Convert to Lowercase")
    print("8. Convert to Uppercase")
    print("9. Check for Hyphen")
    print("10. Scramble Name")
    print("11. Initials")
    print("12. Exit")

def main():
    '''
    Takes in user input to select function
    '''
    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ")

        if choice == '1':
            print("First Name:", firstname(name))
        elif choice == '2':
            print("Middle Name:", middlename(name))
        elif choice == '3':
            print("Last Name:", lastname(name))
        elif choice == '4':
            print("Reversed Name:", reversename(origname))
        elif choice == '5':
            print("Vowels Count:", vowels(names))
        elif choice == '6':
            print("Consonant Frequency:", consonant(origname))
        elif choice == '7':
            print("Lowercase:", lowecase(origname))
        elif choice == '8':
            print("Uppercase:", uppercase(origname))
        elif choice == '9':
            print("Hyphen Present:", booleancheck(origname))
        elif choice == '10':
            print("Scrambled Name:", scramble(list(origname)))
        elif choice == '11':
            print("Initials:", initials(origname))
        elif choice == '12':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

main()